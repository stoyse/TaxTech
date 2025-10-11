"""
AI Service Module for Doc2Flow
Handles all AI provider interactions (OpenAI, Anthropic, Gemini)
"""

import logging
import os
from config import get_active_config, load_system_prompt, AI_PROVIDER
from openai import OpenAI
import httpx
from ai_cleaner_service import get_ai_cleaner_service

# Set up logger
logger = logging.getLogger(__name__)


def load_bpmn_schemas():
    """Load BPMN schema files to provide complete context to the AI (optimized for token usage)"""
    schemas = {}
    
    try:
        # Load BPMN 2.0 Model Schema (reduced for efficiency)
        bpmn_path = "BPMN20.cmof.xml"
        if os.path.exists(bpmn_path):
            with open(bpmn_path, "r", encoding="utf-8") as f:
                full_content = f.read()
                # Take first 2000 chars - enough to show structure without overwhelming the API
                schemas["bpmn20"] = full_content[:2000]
            logger.info(f"Loaded BPMN 2.0 schema excerpt: {len(schemas['bpmn20'])} characters")
        else:
            logger.warning(f"BPMN 2.0 schema file not found: {bpmn_path}")
    except Exception as e:
        logger.error(f"Error loading BPMN 2.0 schema: {str(e)}")
    
    try:
        # Load BPMN DI Schema (reduced for efficiency)
        bpmndi_path = "BPMNDI.cmof.xml"
        if os.path.exists(bpmndi_path):
            with open(bpmndi_path, "r", encoding="utf-8") as f:
                full_content = f.read()
                # Take first 2000 chars - enough to show structure without overwhelming the API
                schemas["bpmndi"] = full_content[:2000]
            logger.info(f"Loaded BPMN DI schema excerpt: {len(schemas['bpmndi'])} characters")
        else:
            logger.warning(f"BPMN DI schema file not found: {bpmndi_path}")
    except Exception as e:
        logger.error(f"Error loading BPMN DI schema: {str(e)}")
    
    return schemas


class AIService:
    """Service class for AI provider interactions"""
    
    def __init__(self):
        """Initialize AI service with configured provider"""
        self.provider = AI_PROVIDER
        self.config = get_active_config()
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the AI client based on the configured provider"""
        logger.info(f"Initializing AI client for provider: {self.provider}")
        
        if not self.config.get("api_key"):
            logger.error(f"No API key found for provider: {self.provider}")
            raise ValueError(f"No API key found for provider: {self.provider}")
        
        logger.info(f"API key found (length: {len(self.config['api_key'])})")
        
        if self.provider == "openai":
            # Set a timeout of 300 seconds for all operations (gpt-5 needs more time for reasoning)
            # Must specify all timeout types explicitly
            timeout_config = httpx.Timeout(
                connect=30.0,    # 30 seconds to connect
                read=300.0,      # 5 minutes to read response (critical for gpt-5)
                write=30.0,      # 30 seconds to write request
                pool=30.0        # 30 seconds for pool operations
            )
            self.client = OpenAI(
                api_key=self.config["api_key"],
                timeout=timeout_config
            )
            logger.info("OpenAI client initialized successfully with 300s read timeout")
        elif self.provider == "anthropic":
            # TODO: Add Anthropic support
            logger.warning(f"Provider {self.provider} not yet fully supported")
            raise NotImplementedError(f"Provider {self.provider} not yet implemented")
        elif self.provider == "gemini":
            # TODO: Add Gemini support
            logger.warning(f"Provider {self.provider} not yet fully supported")
            raise NotImplementedError(f"Provider {self.provider} not yet implemented")
        else:
            logger.error(f"Unknown provider: {self.provider}")
            raise ValueError(f"Unknown provider: {self.provider}")
    
    def _prepare_api_params(self, system_prompt, user_prompt):
        """Prepare API parameters based on provider and model configuration"""
        logger.info("Preparing API parameters...")
        
        # Base parameters common to all providers
        api_params = {
            "model": self.config["model"],
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        }
        
        # Handle temperature parameter
        # Some models (like o1-preview, o1-mini, gpt-5) don't support temperature
        #if "temperature" in self.config:
        #   temperature = self.config["temperature"]
        #    # Only add temperature if it's not 1.0 (default) or if model supports it
        #    model_name = self.config["model"].lower()
            
            # List of models that don't support temperature parameter
        #    no_temp_models = ["o1-preview", "o1-mini", "gpt-5"]
            
        #    if any(model in model_name for model in no_temp_models):
        #        logger.info(f"Model {self.config['model']} does not support 'temperature'; omitting parameter.")
        #    else:
        #       api_params["temperature"] = temperature
        #       logger.info(f"Added temperature parameter: {temperature}")

        # Handle token limit parameters (different providers use different names)
        # GPT-4o, gpt-5 use max_completion_tokens
        # O1-series models (o1-preview, o1-mini) use max_tokens
        if "max_completion_tokens" in self.config:
            api_params["max_completion_tokens"] = self.config["max_completion_tokens"]
            logger.info(f"Added max_completion_tokens: {self.config['max_completion_tokens']}")
        elif "max_tokens" in self.config:
            api_params["max_tokens"] = self.config["max_tokens"]
            logger.info(f"Added max_tokens: {self.config['max_tokens']}")
        elif "max_output_tokens" in self.config:
            api_params["max_output_tokens"] = self.config["max_output_tokens"]
            logger.info(f"Added max_output_tokens: {self.config['max_output_tokens']}")
        
        return api_params
    
    def generate_bpmn_from_text(self, document_text, file_names=None):
        """
        Generate BPMN workflow from document text using AI
        
        Args:
            document_text (str): Combined text from all documents
            file_names (list): Optional list of source file names
            
        Returns:
            tuple: (bpmn_xml, success_message) or (None, error_message)
        """
        logger.info("="*80)
        logger.info("STARTING BPMN GENERATION PROCESS")
        
        try:
            if not document_text.strip():
                logger.error("No text provided for BPMN generation")
                return None, "No text provided for BPMN generation."
            
            logger.info(f"Document text length: {len(document_text)} characters")
            
            # Load system prompt from file
            logger.info("Loading system prompt...")
            system_prompt = load_system_prompt()
            logger.info(f"System prompt loaded from file: {len(system_prompt)} characters")
            
            # Load BPMN schemas for complete context (optimized)
            logger.info("Loading BPMN schema files...")
            schemas = load_bpmn_schemas()
            
            # Enhance system prompt with schema information (condensed for efficiency)
            if schemas:
                schema_context = "\n\n## BPMN Schema Reference (Excerpts)\n\n"
                schema_context += "Use these schema excerpts to ensure valid BPMN structure:\n\n"
                
                if "bpmn20" in schemas:
                    schema_context += "**BPMN 2.0 Model Schema:**\n```xml\n"
                    schema_context += schemas["bpmn20"]
                    schema_context += "\n... (truncated)\n```\n\n"
                
                if "bpmndi" in schemas:
                    schema_context += "**BPMN DI Schema:**\n```xml\n"
                    schema_context += schemas["bpmndi"]
                    schema_context += "\n... (truncated)\n```\n\n"
                
                system_prompt += schema_context
                logger.info(f"Enhanced system prompt with schemas: {len(system_prompt)} characters total")
            
            # Create the prompt for BPMN generation
            # Limit to 8000 characters to stay within token limits
            text_preview = document_text[:8000]
            logger.info(f"Using first {len(text_preview)} characters for API call")
            
            user_prompt = f"""Based on the following document content, analyze the business process described and generate a complete BPMN 2.0 XML workflow.

Document Content:
{text_preview}

Please create a BPMN workflow that:
1. Identifies the main process steps
2. Includes start and end events
3. Adds decision points (gateways) where applicable
4. Uses clear, descriptive labels
5. Includes complete diagram interchange (DI) information for proper visual rendering

Return ONLY the BPMN XML without any additional explanation or markdown formatting."""
            
            logger.info(f"System prompt preview: {system_prompt[:200]}...")
            logger.info(f"User prompt preview: {user_prompt[:500]}...")
            
            # Prepare API parameters
            api_params = self._prepare_api_params(system_prompt, user_prompt)
            
            # Call AI API
            logger.info(f"Calling {self.provider} API...")
            response = self.client.chat.completions.create(**api_params)
            
            # Log response details
            logger.info("API call successful!")
            logger.info(f"Response ID: {response.id}")
            logger.info(f"Model used: {response.model}")
            logger.info(f"Tokens used - prompt: {response.usage.prompt_tokens}, completion: {response.usage.completion_tokens}, total: {response.usage.total_tokens}")
            
            # Extract BPMN XML from response
            bpmn_xml = response.choices[0].message.content
            
            # Handle None or empty response
            if bpmn_xml is None:
                logger.error("Response content is None!")
                return None, "Error: AI returned empty response. The model may have used all tokens for reasoning. Try increasing max_completion_tokens."
            
            bpmn_xml = bpmn_xml.strip()
            logger.info(f"Raw response length: {len(bpmn_xml)} characters")
            logger.info(f"Raw response preview (first 500 chars):\n{bpmn_xml[:500]}")
            
            # Clean up the response (remove markdown code blocks if present)
            bpmn_xml = self._clean_bpmn_xml(bpmn_xml)
            
            # Clean the BPMN XML using the cleaner service
            ai_cleaner = get_ai_cleaner_service()
            cleaned_bpmn_xml = ai_cleaner.clean_bpmn_xml(bpmn_xml)

            logger.info(f"Cleaned BPMN XML length: {len(cleaned_bpmn_xml)} characters")
            logger.info(f"BPMN XML preview (first 500 chars):\n{cleaned_bpmn_xml[:500]}")
            logger.info("BPMN GENERATION COMPLETED SUCCESSFULLY")
            logger.info("="*80)
            
            return cleaned_bpmn_xml, "Successfully generated and cleaned BPMN workflow!"
            
        except Exception as e:
            logger.error(f"ERROR generating BPMN: {str(e)}", exc_info=True)
            logger.info("="*80)
            return None, f"Error generating BPMN: {str(e)}"
    
    def _clean_bpmn_xml(self, bpmn_xml):
        """Remove markdown formatting from BPMN XML response"""
        if bpmn_xml.startswith("```xml"):
            logger.info("Removing ```xml markdown wrapper")
            bpmn_xml = bpmn_xml[6:]
        if bpmn_xml.startswith("```"):
            logger.info("Removing ``` markdown wrapper")
            bpmn_xml = bpmn_xml[3:]
        if bpmn_xml.endswith("```"):
            logger.info("Removing trailing ``` markdown wrapper")
            bpmn_xml = bpmn_xml[:-3]
        return bpmn_xml.strip()
    
    def get_config_info(self):
        """Get current configuration information for display"""
        config_info = {
            "provider": self.provider,
            "model": self.config["model"],
            "api_key_length": len(self.config.get("api_key", ""))
        }
        
        # Add temperature if available
        #if "temperature" in self.config:
        #    config_info["temperature"] = self.config["temperature"]
        
        # Add token limit info
        for key in ["max_completion_tokens", "max_tokens", "max_output_tokens"]:
            if key in self.config:
                config_info[key] = self.config[key]
                break
        
        return config_info


# Create a singleton instance
_ai_service_instance = None

def get_ai_service():
    """Get or create the AI service singleton instance"""
    global _ai_service_instance
    if _ai_service_instance is None:
        _ai_service_instance = AIService()
    return _ai_service_instance
