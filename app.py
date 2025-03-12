import os
import streamlit as st
from get_texts import extract_text_from_pdf, extract_text_from_docx
from prompt import analyze_contract

def save_uploaded_file(uploaded_file, save_folder):
    """Saves uploaded file to a specified folder."""
    os.makedirs(save_folder, exist_ok=True)
    file_path = os.path.join(save_folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def process_uploaded_contract(file_path):
    """Extracts text from uploaded contract and analyzes it."""
    if file_path.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        extracted_text = extract_text_from_docx(file_path)
    else:
        st.error("Unsupported file format. Please upload a PDF or DOCX file.")
        return None, None
    
    analysis_result = analyze_contract(extracted_text)
    return extracted_text, analysis_result

# Streamlit UI
st.title("📜 Automated Supply Chain Contract Analysis")
st.write("Upload a contract file (.pdf or .docx) to analyze potential loopholes and risks.")

uploaded_file = st.file_uploader("Upload Contract", type=["pdf", "docx"])

if uploaded_file:
    with st.spinner("Processing file..."):
        file_path = save_uploaded_file(uploaded_file, "Data/uploads/")
        extracted_text, analysis_result = process_uploaded_contract(file_path)
    
    if extracted_text:
        st.subheader("Extracted Contract Text")
        st.text_area("Extracted Text", extracted_text, height=200)
        
        if analysis_result:
            st.subheader("🧐 Contract Analysis (Loopholes & Risks)")
            st.write(analysis_result)

st.markdown("---")
st.write("Developed using open-source AI & NLP for contract analysis.")