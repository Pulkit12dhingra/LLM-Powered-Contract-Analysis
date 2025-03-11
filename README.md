# 📜 Automated Supply Chain Contract Analysis

This project is an **AI-powered contract analysis tool** that processes **legal supply chain contracts**, extracts key terms, and identifies potential risks or inconsistencies. It utilizes **OpenAI GPT-4 via LangChain** for intelligent contract analysis.

## 🚀 Features
- **Upload Contracts**: Supports PDF & DOCX formats.
- **Extract Key Clauses**: Retrieves SLAs, penalties, compliance terms, pricing details, and more.
- **Analyze Loopholes**: Uses **GPT-4** to detect vague clauses, missing penalties, and potential disputes.
- **User-Friendly Interface**: Built using **Streamlit** for easy interaction.

---

## 🏗️ Project Structure

```
📂 automated_contract_analysis/
│── 📂 Data/
│   ├── 📂 sample_contracts/        # Stores generated sample contracts (.pdf, .docx)
│   ├── 📂 extracted_texts/         # Stores extracted .txt files from contracts
│   ├── 📂 results/                 # Stores analysis outputs
│── 📜 generate.py                  # Generates sample contracts for testing
│── 📜 get_txt.py                    # Extracts text from PDF/DOCX contracts
│── 📜 prompt.py                      # Uses GPT-4 to analyze contract loopholes
│── 📜 app.py                         # Streamlit UI for user interaction
│── 📜 README.md                      # Documentation
│── 📜 requirements.txt                # List of dependencies
│── 📜 .gitignore                      # Ignore unnecessary files
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/automated_contract_analysis.git
cd automated_contract_analysis
```

### 2️⃣ Install Dependencies
Make sure you have Python **3.8+** installed, then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up OpenAI API Key
This project uses OpenAI's GPT-4. Set up your API key:
```bash
export OPENAI_API_KEY="your_openai_api_key"
```
Or, create a `.env` file and add:
```bash
OPENAI_API_KEY=your_openai_api_key
```

---

## 🛠️ Usage

### 📌 Run the Streamlit App
```bash
streamlit run app.py
```
- Upload a **contract (.pdf or .docx)**.
- View the **extracted text**.
- Click **Analyze Contract** to get AI-generated insights.

### 📌 Generate & Analyze Sample Contracts (CLI)
```bash
python generate.py     # Generates sample contracts
python get_txt.py      # Extracts text from contracts
python prompt.py       # Runs GPT-4 contract analysis
```

---

## 🏆 Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python (FastAPI/Flask optional)
- **AI/NLP**: OpenAI GPT-4 via LangChain
- **Text Extraction**: PyMuPDF, python-docx
- **Storage**: SQLite (optional for database support)

---

## 🤝 Contributing
Feel free to fork and submit a PR! 🚀

---

## 📄 License
MIT License © 2024 Automated Contract Analysis

---

Happy coding! 📝✨

