#test data_preprocessing: 
# from data_preprocessing import preprocess_text
# 
# sample_text = "I have experience in Python, SQL, and Machine Learning."
# 
# processed = preprocess_text(sample_text)
# 
# print(processed)
import pandas as pd
from data_preprocessing import preprocess_text
from resume_parser import extract_text_from_pdf

#process sample jobs 
df = pd.read_csv('data/sample_jobs.csv')

df["processed_description"] = df["description"].apply(preprocess_text)

print(df[["title", "processed_description"]].head())

#process resume
resume_text = extract_text_from_pdf("data/test_sample_resume.pdf")
processed_resume = preprocess_text(resume_text)
print(processed_resume[:500])

#calculate TF-IDF and cosine similarity 

#return ranked results