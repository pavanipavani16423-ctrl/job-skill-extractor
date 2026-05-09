from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["job_description"],
    template="""
You are an expert HR analyst. Extract the following from the job description below:
- Job Title
- Required Skills (list)
- Experience Required
- Education
- Tools & Technologies
- Soft Skills

Job Description:
{job_description}

Return ONLY valid JSON. No extra text.
"""
)