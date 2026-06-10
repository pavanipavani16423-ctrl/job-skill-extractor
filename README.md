# 🚀 Job Skill Extractor

An AI-powered application that intelligently analyzes job descriptions and extracts key information such as job title, experience requirements, education qualifications, technical skills, tools & technologies, and soft skills.

Built using Generative AI and Large Language Models (LLMs), this project helps job seekers, recruiters, and students quickly understand the requirements of a job posting without manually reading lengthy descriptions.

---

## ✨ Features

✅ Extracts Job Title Automatically
✅ Identifies Required Experience
✅ Detects Education Qualifications
✅ Extracts Technical Skills
✅ Identifies Tools & Technologies
✅ Extracts Soft Skills
✅ Structured Output Using Pydantic
✅ Interactive Streamlit Web Interface
✅ AI-Powered Skill Analysis

---

## 🛠️ Tech Stack

* **Python** – Core Programming Language
* **LangChain** – AI Workflow Management
* **Groq LLM (Llama 3.3 70B Versatile)** – Large Language Model
* **Pydantic** – Structured Output Validation
* **Streamlit** – Interactive Web Application
* **Langfuse** – LLM Monitoring & Tracking
* **AWS EC2** – Cloud Deployment

---

## 🔄 System Workflow

1. User enters a Job Description.
2. LangChain processes the input.
3. Groq LLM analyzes the content.
4. Pydantic structures the extracted information.
5. Streamlit displays the results in an easy-to-read format.

---

## 📊 Information Extracted

* Job Title
* Experience Required
* Education Qualification
* Technical Skills
* Tools & Technologies
* Soft Skills

---

## 🎯 Use Cases

* Resume Optimization
* ATS Keyword Analysis
* Recruitment Automation
* Career Guidance
* Skill Gap Analysis
* Job Requirement Understanding

---

## 📁 Project Structure

```text
Job-Skill-Extractor/
│
├── app.py
├── model.py
├── prompt.py
├── parser.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

```bash
git clone <repository-url>
cd Job-Skill-Extractor
pip install -r requirements.txt
streamlit run app.py
```

---

## 🚀 Future Enhancements

* Resume Matching with Job Descriptions
* ATS Score Prediction
* Skill Recommendation System
* Multi-Language Support
* Download Results as PDF/Excel

---

## 👩‍💻 Author

**Pavani**

Passionate about Artificial Intelligence, Machine Learning, Generative AI, and building intelligent applications that solve real-world problems.
