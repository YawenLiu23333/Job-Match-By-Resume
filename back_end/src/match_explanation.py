from openai import OpenAI
import os
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
Compare this resume with this job description.

Return:
1. Why this job matches
2. Missing skills
3. Suggested resume keywords

Resume:
{resume_text[:3000]}

Job Description:
{job_description[:3000]}
"""
            }
        ],
        max_tokens=500
    )
    return completion.choices[0].message.content

if __name__ == "__main__":

    test_resume = "Python React Flask developer"

    test_job = """
    Looking for software engineer with React and backend API experience.
    """

    res = generate_match_explanation(test_resume, test_job)
    print(res)
# 