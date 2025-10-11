import streamlit as st
import streamlit.components.v1 as components
import json

# Page configuration
st.set_page_config(
    page_title="Doc2Flow",
    page_icon="📄",
    layout="wide"
)

# Main Title
st.title("📄 Doc2Flow")
st.markdown("### Transform your documents into clear BPMN workflows")

# Create main layout with two columns
left_col, right_col = st.columns([1, 1])

# Left column - File Upload and Controls
with left_col:
    st.markdown("#### Upload Your Documents")
    st.markdown("Supported formats: PDF, DOCX, TXT, MD")
    
    # File uploader
    uploaded_files = st.file_uploader(
        "Choose files",
        accept_multiple_files=True,
        type=['pdf', 'docx', 'txt', 'md'],
        help="Upload one or more documents to analyze"
    )
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully!")
        
        # Display uploaded files
        with st.expander("View uploaded files"):
            for file in uploaded_files:
                st.write(f"📄 {file.name} ({file.size} bytes)")
        
        # Generate BPMN button
        if st.button("🚀 Generate BPMN", type="primary", use_container_width=True):
            with st.spinner("Analyzing documents and generating BPMN..."):
                # Simulate processing time
                import time
                time.sleep(2)
                
                st.success("✅ BPMN workflow generated successfully!")
                
                # Store a sample BPMN XML workflow in session state for the viewer
                st.session_state.generated_workflow = '''<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_1" targetNamespace="http://bpmn.io/schema/bpmn">
  <bpmn:process id="Process_1" isExecutable="false">
    <bpmn:startEvent id="start" name="Document Received">
      <bpmn:outgoing>flow1</bpmn:outgoing>
    </bpmn:startEvent>
    <bpmn:exclusiveGateway id="validate" name="Validate Document">
      <bpmn:incoming>flow1</bpmn:incoming>
      <bpmn:outgoing>flow2</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="process" name="Process Content">
      <bpmn:incoming>flow2</bpmn:incoming>
      <bpmn:outgoing>flow3</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="extract" name="Extract Information">
      <bpmn:incoming>flow3</bpmn:incoming>
      <bpmn:outgoing>flow4</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="review" name="Manual Review">
      <bpmn:incoming>flow4</bpmn:incoming>
      <bpmn:outgoing>flow5</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="approve" name="Approve Process">
      <bpmn:incoming>flow5</bpmn:incoming>
      <bpmn:outgoing>flow6</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="end" name="Process Complete">
      <bpmn:incoming>flow6</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="flow1" sourceRef="start" targetRef="validate"/>
    <bpmn:sequenceFlow id="flow2" sourceRef="validate" targetRef="process"/>
    <bpmn:sequenceFlow id="flow3" sourceRef="process" targetRef="extract"/>
    <bpmn:sequenceFlow id="flow4" sourceRef="extract" targetRef="review"/>
    <bpmn:sequenceFlow id="flow5" sourceRef="review" targetRef="approve"/>
    <bpmn:sequenceFlow id="flow6" sourceRef="approve" targetRef="end"/>
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_1">
    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_1">
      <bpmndi:BPMNShape id="start_di" bpmnElement="start">
        <dc:Bounds x="152" y="102" width="36" height="36"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="144" y="145" width="52" height="27"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="validate_di" bpmnElement="validate" isMarkerVisible="true">
        <dc:Bounds x="245" y="95" width="50" height="50"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="239" y="152" width="62" height="27"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="process_di" bpmnElement="process">
        <dc:Bounds x="360" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="extract_di" bpmnElement="extract">
        <dc:Bounds x="520" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="review_di" bpmnElement="review" isMarkerVisible="true">
        <dc:Bounds x="680" y="95" width="50" height="50"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="665" y="152" width="80" height="14"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="approve_di" bpmnElement="approve">
        <dc:Bounds x="790" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="end_di" bpmnElement="end">
        <dc:Bounds x="952" y="102" width="36" height="36"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="947" y="145" width="46" height="27"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="flow1_di" bpmnElement="flow1">
        <di:waypoint x="188" y="120"/>
        <di:waypoint x="245" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow2_di" bpmnElement="flow2">
        <di:waypoint x="295" y="120"/>
        <di:waypoint x="360" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow3_di" bpmnElement="flow3">
        <di:waypoint x="460" y="120"/>
        <di:waypoint x="520" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow4_di" bpmnElement="flow4">
        <di:waypoint x="620" y="120"/>
        <di:waypoint x="680" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow5_di" bpmnElement="flow5">
        <di:waypoint x="730" y="120"/>
        <di:waypoint x="790" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow6_di" bpmnElement="flow6">
        <di:waypoint x="890" y="120"/>
        <di:waypoint x="952" y="120"/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn:definitions>'''
    else:
        st.info("👆 Please upload documents to get started")
    
    # Add some spacing
    st.markdown("---")
    
    # Compact info section
    with st.expander("ℹ️ How it works & Features"):
        st.markdown("""
        **How it works:**
        1. Upload documents → 2. AI Analysis → 3. BPMN Generation → 4. Review
        
        **Features:** 🤖 AI extraction • 📊 Interactive diagrams • 📤 Export • 🔄 Multi-document
        """)

# Right column - Workflow Viewer
with right_col:
    st.markdown("#### BPMN Workflow Viewer")

    # Check if we have a generated workflow from the dashboard
    if 'generated_workflow' in st.session_state:
        st.info("📄 Displaying workflow generated from your uploaded documents")
        default_workflow = st.session_state.generated_workflow
    else:
        default_workflow = '''<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_1" targetNamespace="http://bpmn.io/schema/bpmn">
  <bpmn:process id="Process_1" isExecutable="false">
    <bpmn:startEvent id="start" name="Receive Loan Request">
      <bpmn:outgoing>flow1</bpmn:outgoing>
    </bpmn:startEvent>
    <bpmn:exclusiveGateway id="gateway1" name="Check Eligibility">
      <bpmn:incoming>flow1</bpmn:incoming>
      <bpmn:outgoing>flow2</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:exclusiveGateway id="gateway2" name="Evaluate Risk">
      <bpmn:incoming>flow2</bpmn:incoming>
      <bpmn:outgoing>flow3</bpmn:outgoing>
      <bpmn:outgoing>flow4</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="approve" name="Approve Loan">
      <bpmn:incoming>flow3</bpmn:incoming>
      <bpmn:outgoing>flow5</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="reject" name="Reject Application">
      <bpmn:incoming>flow4</bpmn:incoming>
      <bpmn:outgoing>flow6</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="end" name="Send Response">
      <bpmn:incoming>flow5</bpmn:incoming>
      <bpmn:incoming>flow6</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="flow1" sourceRef="start" targetRef="gateway1"/>
    <bpmn:sequenceFlow id="flow2" sourceRef="gateway1" targetRef="gateway2"/>
    <bpmn:sequenceFlow id="flow3" sourceRef="gateway2" targetRef="approve"/>
    <bpmn:sequenceFlow id="flow4" sourceRef="gateway2" targetRef="reject"/>
    <bpmn:sequenceFlow id="flow5" sourceRef="approve" targetRef="end"/>
    <bpmn:sequenceFlow id="flow6" sourceRef="reject" targetRef="end"/>
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_1">
    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_1">
      <bpmndi:BPMNShape id="start_di" bpmnElement="start">
        <dc:Bounds x="152" y="102" width="36" height="36"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="139" y="145" width="62" height="27"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="gateway1_di" bpmnElement="gateway1" isMarkerVisible="true">
        <dc:Bounds x="245" y="95" width="50" height="50"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="244" y="152" width="52" height="27"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="gateway2_di" bpmnElement="gateway2" isMarkerVisible="true">
        <dc:Bounds x="355" y="95" width="50" height="50"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="345" y="152" width="70" height="14"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="approve_di" bpmnElement="approve">
        <dc:Bounds x="470" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="reject_di" bpmnElement="reject">
        <dc:Bounds x="470" y="200" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="end_di" bpmnElement="end">
        <dc:Bounds x="632" y="162" width="36" height="36"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="611" y="205" width="78" height="14"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="flow1_di" bpmnElement="flow1">
        <di:waypoint x="188" y="120"/>
        <di:waypoint x="245" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow2_di" bpmnElement="flow2">
        <di:waypoint x="295" y="120"/>
        <di:waypoint x="355" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow3_di" bpmnElement="flow3">
        <di:waypoint x="405" y="120"/>
        <di:waypoint x="470" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow4_di" bpmnElement="flow4">
        <di:waypoint x="380" y="145"/>
        <di:waypoint x="380" y="240"/>
        <di:waypoint x="470" y="240"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow5_di" bpmnElement="flow5">
        <di:waypoint x="570" y="120"/>
        <di:waypoint x="601" y="120"/>
        <di:waypoint x="601" y="180"/>
        <di:waypoint x="632" y="180"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow6_di" bpmnElement="flow6">
        <di:waypoint x="570" y="240"/>
        <di:waypoint x="601" y="240"/>
        <di:waypoint x="601" y="180"/>
        <di:waypoint x="632" y="180"/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn:definitions>'''

    # Control buttons
    btn_col1, btn_col2 = st.columns([1, 1])
    
    with btn_col1:
        if st.button("🚀 Generate Workflow", type="primary", use_container_width=True):
            generate_workflow = True
        else:
            generate_workflow = False
    
    with btn_col2:
        if st.button("🔄 Load Sample", use_container_width=True):
            st.session_state.generated_workflow = '''<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_1" targetNamespace="http://bpmn.io/schema/bpmn">
  <bpmn:process id="Process_1" isExecutable="false">
    <bpmn:startEvent id="start" name="Start Process">
      <bpmn:outgoing>flow1</bpmn:outgoing>
    </bpmn:startEvent>
    <bpmn:task id="input" name="Receive Input">
      <bpmn:incoming>flow1</bpmn:incoming>
      <bpmn:outgoing>flow2</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="validate" name="Validate Data">
      <bpmn:incoming>flow2</bpmn:incoming>
      <bpmn:outgoing>flow3</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="process" name="Process Request">
      <bpmn:incoming>flow3</bpmn:incoming>
      <bpmn:outgoing>flow4</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="end" name="End Process">
      <bpmn:incoming>flow4</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="flow1" sourceRef="start" targetRef="input"/>
    <bpmn:sequenceFlow id="flow2" sourceRef="input" targetRef="validate"/>
    <bpmn:sequenceFlow id="flow3" sourceRef="validate" targetRef="process"/>
    <bpmn:sequenceFlow id="flow4" sourceRef="process" targetRef="end"/>
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_1">
    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_1">
      <bpmndi:BPMNShape id="start_di" bpmnElement="start">
        <dc:Bounds x="152" y="102" width="36" height="36"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="137" y="145" width="66" height="14"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="input_di" bpmnElement="input">
        <dc:Bounds x="250" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="validate_di" bpmnElement="validate" isMarkerVisible="true">
        <dc:Bounds x="415" y="95" width="50" height="50"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="400" y="152" width="80" height="14"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="process_di" bpmnElement="process">
        <dc:Bounds x="530" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="end_di" bpmnElement="end">
        <dc:Bounds x="692" y="102" width="36" height="36"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds x="677" y="145" width="66" height="14"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="flow1_di" bpmnElement="flow1">
        <di:waypoint x="188" y="120"/>
        <di:waypoint x="250" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow2_di" bpmnElement="flow2">
        <di:waypoint x="350" y="120"/>
        <di:waypoint x="415" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow3_di" bpmnElement="flow3">
        <di:waypoint x="465" y="120"/>
        <di:waypoint x="530" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="flow4_di" bpmnElement="flow4">
        <di:waypoint x="630" y="120"/>
        <di:waypoint x="692" y="120"/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn:definitions>'''
            st.rerun()
    
    # Toggle for XML editor
    show_xml = st.toggle("📝 Show/Edit BPMN XML", value=False)
    
    # Workflow XML input (hidden behind toggle)
    if show_xml:
        bpmn_xml = st.text_area("BPMN XML", height=150, value=default_workflow)
    else:
        bpmn_xml = default_workflow

    # Display workflow if generated or sample loaded
    if generate_workflow or 'generated_workflow' in st.session_state:
        try:
            # Create the bpmn-js viewer HTML component
            # Replace backticks in XML to avoid breaking JavaScript template literal
            bpmn_xml_safe = bpmn_xml.replace('`', '\\`').replace('${', '\\${')
            
            bpmn_viewer_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <link rel="stylesheet" href="https://unpkg.com/bpmn-js@17.2.0/dist/assets/bpmn-js.css">
                <link rel="stylesheet" href="https://unpkg.com/bpmn-js@17.2.0/dist/assets/diagram-js.css">
                <link rel="stylesheet" href="https://unpkg.com/bpmn-js@17.2.0/dist/assets/bpmn-font/css/bpmn-embedded.css">
                <style>
                    body {{
                        margin: 0;
                        padding: 0;
                        font-family: Arial, sans-serif;
                    }}
                    #canvas {{
                        height: 400px;
                        width: 100%;
                        border: 1px solid #e0e0e0;
                        border-radius: 4px;
                        background-color: white;
                    }}
                    .download-btn {{
                        margin: 10px 0;
                        padding: 8px 16px;
                        background-color: #0066cc;
                        color: white;
                        border: none;
                        border-radius: 4px;
                        cursor: pointer;
                        font-size: 14px;
                    }}
                    .download-btn:hover {{
                        background-color: #0052a3;
                    }}
                </style>
            </head>
            <body>
                <div id="canvas"></div>
                <button class="download-btn" onclick="downloadDiagram()">📥 Download BPMN as SVG</button>
                
                <script src="https://unpkg.com/bpmn-js@17.2.0/dist/bpmn-modeler.development.js"></script>
                <script>
                    var modeler = new BpmnJS({{
                        container: '#canvas',
                        keyboard: {{
                            bindTo: document
                        }}
                    }});
                    
                    var bpmnXML = `{bpmn_xml_safe}`;
                    
                    modeler.importXML(bpmnXML).then(function(result) {{
                        const canvas = modeler.get('canvas');
                        canvas.zoom('fit-viewport');
                    }}).catch(function(err) {{
                        console.error('Error rendering BPMN diagram:', err);
                    }});
                    
                    function downloadDiagram() {{
                        modeler.saveSVG().then(function(result) {{
                            var svg = result.svg;
                            var blob = new Blob([svg], {{ type: 'image/svg+xml' }});
                            var url = URL.createObjectURL(blob);
                            var a = document.createElement('a');
                            a.href = url;
                            a.download = 'workflow.svg';
                            document.body.appendChild(a);
                            a.click();
                            document.body.removeChild(a);
                            URL.revokeObjectURL(url);
                        }});
                    }}
                </script>
            </body>
            </html>
            """
            
            # Display the BPMN viewer
            components.html(bpmn_viewer_html, height=500)
                
        except Exception as e:
            st.error(f"Error rendering BPMN: {e}")
    else:
        st.info("👆 Upload documents and generate BPMN, or load a sample workflow to get started")