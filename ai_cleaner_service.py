"""
AI Cleaner Service Module for Doc2Flow
Handles the cleaning of generated BPMN XML using a separate AI call.
"""

import logging
import httpx
from openai import OpenAI
from cleaner_config import get_cleaner_config, load_cleaner_system_prompt

# Set up logger
logger = logging.getLogger(__name__)


class AICleanerService:
    """Service class for cleaning BPMN XML."""

    def __init__(self):
        """Initialize AI cleaner service."""
        self.config = get_cleaner_config()
        self.client = None
        self._initialize_client()

    def _initialize_client(self):
        """Initialize the AI client for the cleaner service."""
        logger.info("Initializing AI cleaner client...")
        
        if not self.config.get("api_key"):
            logger.error("No API key found for cleaner service.")
            raise ValueError("No API key found for cleaner service.")

        timeout_config = httpx.Timeout(300.0)
        self.client = OpenAI(
            api_key=self.config["api_key"],
            timeout=timeout_config
        )
        logger.info("AI cleaner client initialized successfully.")

    def clean_bpmn_xml(self, dirty_xml):
        """
        Cleans the given BPMN XML using an AI call.

        Args:
            dirty_xml (str): The BPMN XML to be cleaned.

        Returns:
            str: The cleaned BPMN XML.
        """
        if not dirty_xml or not dirty_xml.strip():
            logger.warning("No BPMN XML provided to clean.")
            return ""

        logger.info("="*80)
        logger.info("STARTING BPMN XML CLEANING PROCESS")

        try:
            system_prompt = load_cleaner_system_prompt()
            
            api_params = {
                "model": self.config["model"],
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": dirty_xml}
                ],
                "temperature": self.config["temperature"],
                "max_tokens": self.config["max_completion_tokens"],
            }

            logger.info("Calling cleaner API...")
            response = self.client.chat.completions.create(**api_params)
            
            cleaned_xml = response.choices[0].message.content
            if cleaned_xml is None:
                logger.error("Cleaner API returned an empty response.")
                return dirty_xml # Return original if cleaning fails

            cleaned_xml = self._strip_markdown(cleaned_xml.strip())
            
            logger.info("BPMN XML cleaning successful.")
            logger.info("="*80)
            
            return cleaned_xml

        except Exception as e:
            logger.error(f"ERROR during BPMN cleaning: {str(e)}", exc_info=True)
            # Return the original XML if cleaning fails
            return dirty_xml

    def _strip_markdown(self, xml_string):
        """Removes markdown code block formatting."""
        if xml_string.startswith("```xml"):
            xml_string = xml_string[6:]
        if xml_string.endswith("```"):
            xml_string = xml_string[:-3]
        return xml_string.strip()


# Singleton instance for the cleaner service
_ai_cleaner_service_instance = None

def get_ai_cleaner_service():
    """Get or create the AI cleaner service singleton instance."""
    global _ai_cleaner_service_instance
    if _ai_cleaner_service_instance is None:
        _ai_cleaner_service_instance = AICleanerService()
    return _ai_cleaner_service_instance
