import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

prompt = PromptTemplate(
    input_variables=["job_description"],
    template="""
You are an expert HR analyst. Extract information from the job description below.

Return ONLY this exact JSON format, nothing else:
{{
    "job_title": "extracted job title here",
    "experience": "extracted experience here",
    "education": "extracted education here",
    "required_skills": ["skill1", "skill2", "skill3"],
    "tools_technologies": ["tool1", "tool2"],
    "soft_skills": ["soft skill1", "soft skill2"]
}}

Job Description:
{job_description}
"""
)

def extract_skills(job_description: str):
    chain = prompt | llm
    response = chain.invoke({"job_description": job_description})
    text = response.content.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    start = text.find("{")
    end = text.rfind("}") + 1
    json_str = text[start:end]
    return json.loads(json_str)