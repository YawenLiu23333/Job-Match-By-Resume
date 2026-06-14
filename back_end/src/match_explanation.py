from openai import OpenAI
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ.get("OPENROUTER_API_KEY"),
)
# 
def generate_match_explanation(resume_text, job_description):
    completion = client.chat.completions.create(
        extra_body={},
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "system",
                "content":  "You are a career assistant that explains resume-job matches clearly and concisely."
            },
            {
                "role": "user",
                "content": f"""
Compare this resume with this job description and return valid JSON only with the following content in 3 arrays:
match_reasons: array of 2-3 concise bullets, missing_skills: array of 2-5 skills keywords, suggested_keywords: array of 5-8 resume keywords emphasized in job description but missing in resume.
Return ONLY valid JSON.
Do not include markdown.
Do not include ```json.
Do not include explanation outside JSON.
Do not include additional explanation besides match_reasons, missing_skills, and suggested_keywords.
make output less than 100 words. 

Resume:
{resume_text[:3000]}

Job Description:
{job_description[:3000]}
"""
            }
        ],
        max_tokens=400
    )
    content = completion.choices[0].message.content

    content = content.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(content)

        if isinstance(data, list):
            data = data[0]

        return data
        
    except json.JSONDecodeError:
        print("invalid JSON from model:")
        print(content)
        return {
            "match_reasons": [content],
            "missing_skills": [],
            "suggested_keywords": []
        }

if __name__ == "__main__":

    test_resume = "Python React Flask developer"

    test_job = """
    Looking for software engineer with React and backend API experience.
    """

    res = generate_match_explanation(test_resume, test_job)
    print(res)
 