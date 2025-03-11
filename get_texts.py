import os
import fitz  # PyMuPDF for PDF extraction
import docx

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
    return text

def extract_text_from_docx(docx_path):
    """Extracts text from a DOCX file."""
    text = ""
    try:
        doc = docx.Document(docx_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error extracting text from {docx_path}: {e}")
    return text

def save_text_to_file(text, output_path):
    """Saves extracted text to a .txt file."""
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted text saved to: {output_path}")
    except Exception as e:
        print(f"Error saving text file {output_path}: {e}")

def process_contracts(input_folder, output_folder):
    """Processes all PDF and DOCX contracts in a folder and saves extracted text."""
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        
        if file_name.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file_name.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            continue
        
        if text.strip():
            output_file_name = os.path.splitext(file_name)[0] + ".txt"
            output_path = os.path.join(output_folder, output_file_name)
            save_text_to_file(text, output_path)
        else:
            print(f"No text extracted from {file_name}")

if __name__ == "__main__":
    input_folder = "Data/sample_contracts/"  # Folder containing contracts
    output_folder = "Data/extracted_texts/"  # Folder to store extracted text
    process_contracts(input_folder, output_folder)
