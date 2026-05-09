import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from prompt import prompt
from parser import JobExtraction

load_dotenv()  # ← THIS LINE WAS MISSING

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
parser = PydanticOutputParser(pydantic_object=JobExtraction)

def extract_skills(job_description: str):
    chain = prompt | llm
    response = chain.invoke({"job_description": job_description})
    text = response.content.strip()
    clean = text.replace("```json", "").replace("```", "").strip()
    return json.loads(clean)