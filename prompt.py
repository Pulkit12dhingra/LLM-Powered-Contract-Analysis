import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# Load OpenAI GPT-4 Model
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

def analyze_contract(contract_text):
    """Analyzes contract text to identify loopholes and inconsistencies using OpenAI GPT-4."""
    prompt_template = PromptTemplate(
        input_variables=["contract"],
        template="""
        Given the following supply chain contract:
        
        {contract}
        
        Identify any potential loopholes, vague clauses, missing penalties, or compliance risks. 
        Provide a structured analysis of the risks found.
        """
    )
    
    prompt = prompt_template.format(contract=contract_text)
    response = llm.predict(prompt)
    return response

def process_extracted_texts(input_folder, output_folder):
    """Processes all extracted text files and generates loophole analysis using GPT-4."""
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(input_folder):
        if not file_name.endswith(".txt"):
            continue
        
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name.replace(".txt", "_analysis.txt"))
        
        with open(input_path, "r", encoding="utf-8") as f:
            contract_text = f.read()
        
        analysis_result = analyze_contract(contract_text)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(analysis_result)
        
        print(f"Analysis saved to: {output_path}")

if __name__ == "__main__":
    input_folder = "Data/extracted_texts/"  # Folder containing extracted texts
    output_folder = "Data/results/"  # Folder to store analysis results
    process_extracted_texts(input_folder, output_folder)