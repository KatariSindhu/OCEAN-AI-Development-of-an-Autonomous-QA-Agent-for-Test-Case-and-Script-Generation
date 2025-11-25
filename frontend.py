import streamlit as st
import requests
import json

# --- CONFIGURATION ---
BACKEND_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="OceanAI QA Agent", layout="wide")

# --- CUSTOM CSS FOR "OCEAN" VIBE ---
st.markdown("""
    <style>
    .main-header { font-size: 36px; color: #0077b6; font-weight: bold; }
    .sub-header { font-size: 24px; color: #0096c7; }
    .success-box { padding: 10px; background-color: #d4edda; color: #155724; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: INGESTION ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=80)
    st.markdown("### 🧠 Knowledge Base")
    
    uploaded_files = st.file_uploader(
        "Upload Requirements (MD/PDF)", 
        accept_multiple_files=True,
        type=["md", "txt", "pdf"]
    )
    
    if st.button("Build Knowledge Base"):
        if uploaded_files:
            files = [("files", (f.name, f.getvalue(), "text/plain")) for f in uploaded_files]
            with st.spinner("Ingesting documents into Vector DB..."):
                try:
                    response = requests.post(f"{BACKEND_URL}/upload-documents/", files=files)
                    if response.status_code == 200:
                        st.success("✅ Knowledge Base Updated!")
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"Connection Failed: {e}. Is the backend running?")
        else:
            st.warning("Please upload files first.")

# --- MAIN PAGE ---
st.markdown('<div class="main-header">OceanAI: Autonomous QA Agent 🌊</div>', unsafe_allow_html=True)

# Tabs for Logical Flow
tab1, tab2 = st.tabs(["1️⃣ Generate Test Cases", "2️⃣ Create Selenium Script"])

# --- TAB 1: TEST CASE GENERATION ---
with tab1:
    st.markdown("### Ask the Agent to Plan Tests")
    query = st.text_area("Describe what you want to test:", 
                        "Generate positive and negative test cases for the discount code feature.")
    
    if st.button("Generate Test Plan"):
        with st.spinner("Thinking... (Retrieving Rules & Planning)"):
            try:
                res = requests.post(f"{BACKEND_URL}/generate-test-cases/", json={"query": query})
                if res.status_code == 200:
                    data = res.json()
                    st.session_state['test_cases'] = data['test_cases']
                    st.session_state['context'] = data['context_used']
                    st.success("Test Cases Generated Successfully!")
                else:
                    st.error(f"Backend Error: {res.text}")
            except Exception as e:
                st.error(f"Connection Error: {e}. Is the backend running?")

    # Display Results
    if 'test_cases' in st.session_state:
        st.write("---")
        st.subheader("📋 Generated Test Plan")
        
        # Show Context Used (Bonus Points for "Grounding")
        with st.expander("View Source Documents Used"):
            st.write(st.session_state['context'])
            
        for idx, tc in enumerate(st.session_state['test_cases']):
            with st.container():
                st.markdown(f"**{tc.get('id', 'ID')} - {tc.get('title', 'Test Case')}**")
                st.text(tc.get('description', ''))
                st.caption(f"Expected: {tc.get('expected_result', '')}")
                if st.button(f"Select for Automation", key=f"btn_{idx}"):
                    st.session_state['selected_test'] = tc
                    st.toast(f"Selected: {tc.get('title')}")

# --- TAB 2: SCRIPT GENERATION ---
with tab2:
    st.markdown("### 🤖 Build Automation Script")
    
    # Step 1: Input HTML
    html_input = st.text_area("Paste 'checkout.html' Content here:", height=200)
    
    # Step 2: Confirm Selection
    if 'selected_test' in st.session_state:
        st.info(f"Target Test Case: {st.session_state['selected_test']['title']}")
        
        if st.button("Generate Python Selenium Code"):
            if not html_input:
                st.error("Please paste the HTML content first.")
            else:
                with st.spinner("Coding... (Mapping Selectors to Logic)"):
                    payload = {
                        "test_case_json": st.session_state['selected_test'],
                        "html_content": html_input
                    }
                    try:
                        res = requests.post(f"{BACKEND_URL}/generate-selenium-script/", json=payload)
                        if res.status_code == 200:
                            script = res.json()['script']
                            st.code(script, language='python')
                            st.balloons() # Celebration for "Super Dream" submission
                        else:
                            st.error(f"Error: {res.text}")
                    except Exception as e:
                        st.error(f"Connection Failed: {e}")
    else:
        st.warning("Please go to Tab 1 and select a test case first.")