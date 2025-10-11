import streamlit as st
import graphviz
import json

# Page configuration
st.set_page_config(
    page_title="Doc2Flow",
    page_icon="📄",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Doc2Flow Navigation")
page = st.sidebar.selectbox("Choose a page", ["Dashboard", "Workflow Viewer"])

if page == "Dashboard":
    # Main Dashboard Page
    st.title("📄 Doc2Flow Dashboard")
    st.markdown("### Transform your documents into clear BPMN workflows")
    
    # Create columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
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
                    st.info("💡 Switch to the 'Workflow Viewer' page to see your generated workflow.")
                    
                    # Store a sample workflow in session state for the viewer
                    st.session_state.generated_workflow = {
                        "title": "Document Processing Workflow",
                        "nodes": [
                            {"id": "start", "label": "Document Received", "type": "event"},
                            {"id": "validate", "label": "Validate Document", "type": "decision"},
                            {"id": "process", "label": "Process Content", "type": "action"},
                            {"id": "extract", "label": "Extract Information", "type": "action"},
                            {"id": "review", "label": "Manual Review", "type": "decision"},
                            {"id": "approve", "label": "Approve Process", "type": "action"},
                            {"id": "end", "label": "Process Complete", "type": "event"}
                        ],
                        "edges": [
                            ["start", "validate"],
                            ["validate", "process"],
                            ["process", "extract"],
                            ["extract", "review"],
                            ["review", "approve"],
                            ["approve", "end"]
                        ]
                    }
        else:
            st.info("👆 Please upload documents to get started")
    
    with col2:
        st.markdown("#### How it works")
        st.markdown("""
        1. **Upload** your documents
        2. **AI Analysis** extracts processes
        3. **BPMN Generation** creates visual workflows
        4. **Review & Export** your results
        """)
        
        st.markdown("#### Features")
        st.markdown("""
        - 🤖 AI-powered process extraction
        - 📊 Interactive BPMN diagrams
        - 📤 Export capabilities
        - 🔄 Multi-document processing
        """)

elif page == "Workflow Viewer":
    st.title("🧠 Doc2Flow Viewer")

    # Check if we have a generated workflow from the dashboard
    if 'generated_workflow' in st.session_state:
        st.info("📄 Displaying workflow generated from your uploaded documents")
        default_workflow = json.dumps(st.session_state.generated_workflow, indent=2)
    else:
        default_workflow = '''{
  "title": "Loan Approval Process",
  "nodes": [
    {"id": "start", "label": "Receive Loan Request", "type": "event"},
    {"id": "check_eligibility", "label": "Check Eligibility", "type": "decision"},
    {"id": "evaluate_risk", "label": "Evaluate Risk Level", "type": "decision"},
    {"id": "approve", "label": "Approve Loan", "type": "action"},
    {"id": "reject", "label": "Reject Application", "type": "action"},
    {"id": "end", "label": "Send Response", "type": "event"}
  ],
  "edges": [
    ["start", "check_eligibility"],
    ["check_eligibility", "evaluate_risk"],
    ["evaluate_risk", "approve"],
    ["evaluate_risk", "reject"],
    ["approve", "end"],
    ["reject", "end"]
  ]
}'''

    # Control buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        if st.button("🚀 Generate Workflow", type="primary"):
            generate_workflow = True
        else:
            generate_workflow = False
    
    with col2:
        if st.button("🔄 Load Sample Workflow"):
            st.session_state.generated_workflow = {
                "title": "Sample Business Process",
                "nodes": [
                    {"id": "start", "label": "Start Process", "type": "event"},
                    {"id": "input", "label": "Receive Input", "type": "action"},
                    {"id": "validate", "label": "Validate Data", "type": "decision"},
                    {"id": "process", "label": "Process Request", "type": "action"},
                    {"id": "end", "label": "End Process", "type": "event"}
                ],
                "edges": [
                    ["start", "input"],
                    ["input", "validate"],
                    ["validate", "process"],
                    ["process", "end"]
                ]
            }
            st.rerun()
    
    with col3:
        show_json = st.toggle("📝 Show/Edit JSON", value=False)
    
    # Workflow JSON input (hidden behind toggle)
    if show_json:
        llm_output = st.text_area("Workflow JSON", height=120, value=default_workflow)
    else:
        llm_output = default_workflow

    if generate_workflow or 'generated_workflow' in st.session_state:
        try:
            data = json.loads(llm_output)
            
            # Display workflow title
            if "title" in data:
                st.subheader(f"📊 {data['title']}")
            
            dot = graphviz.Digraph()
            dot.attr(rankdir='TB', size='8,6')
            dot.attr('node', fontname='Arial', fontsize='9')
            dot.attr('edge', fontname='Arial', fontsize='8')
            
            # Add nodes with different shapes and colors based on type
            for node in data["nodes"]:
                shape = "ellipse"
                color = "lightblue"
                
                if node["type"] == "decision":
                    shape = "diamond"
                    color = "lightyellow"
                elif node["type"] == "action":
                    shape = "box"
                    color = "lightgreen"
                elif node["type"] == "event":
                    shape = "ellipse"
                    color = "lightcoral"
                
                dot.node(node["id"], node["label"], shape=shape, style="filled", fillcolor=color)
            
            # Add edges
            for edge in data["edges"]:
                dot.edge(edge[0], edge[1])
            
            st.graphviz_chart(dot, use_container_width=False)
            
            # Display workflow statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Nodes", len(data["nodes"]))
            with col2:
                st.metric("Total Connections", len(data["edges"]))
            with col3:
                decisions = len([n for n in data["nodes"] if n["type"] == "decision"])
                st.metric("Decision Points", decisions)
                
        except Exception as e:
            st.error(f"Error parsing JSON: {e}")
            st.info("Please check your JSON format and try again.")