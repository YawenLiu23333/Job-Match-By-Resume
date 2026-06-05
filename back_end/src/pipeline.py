import pandas as pd
from .data_preprocessing import preprocess_text
from .resume_parser import extract_text_from_pdf
from .job_matcher import job_resume_similarity
from .embedding_matcher import job_resume_semantic_matching
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"    

def load_data():
    # process sample jobs
    df = pd.read_csv(DATA_DIR / "sample_jobs.csv")
    df = df.dropna(axis=1, how='all')
    df["processed_description"] = df["description"].apply(preprocess_text)
    # print(df[["title", "processed_description"]].head())
    df['labeled_score'] = [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, ]
    return df
    
def load_resume(): 
    # process resume
    resume_text = extract_text_from_pdf(DATA_DIR / "test_sample_resume.pdf")
    return resume_text

def process_resume(resume_text):
    processed_resume = preprocess_text(resume_text)
    # print(processed_resume[:500])
    return processed_resume
    
def add_tfidf_scores(df, processed_resume):    
    # df = df.reset_index(drop=True)
    jobs = df["processed_description"].tolist()
    docs = [processed_resume] + jobs
    # return ranked results
    scores = job_resume_similarity(docs)
    # attach score back to jobs
    df["tfidf_score"] = scores
    sorted_df = df.sort_values(by="tfidf_score", ascending=False)
    return sorted_df

def add_embedding_scores(df, processed_resume):   
    # attach sematic embedding ranks back to datafram and sort by ranks
    jobs = df["processed_description"].tolist()
    semantic_scores = job_resume_semantic_matching(processed_resume, jobs)
    df["embedding_score"] = semantic_scores.squeeze().tolist()
    return df
    # semantic_sorted_df = df.sort_values(by="embedding_score", ascending=False)

def run_pipeline(resume_text):
    # controls the whole flow
    df = load_data()
    processed_resume = process_resume(resume_text)
    df = add_tfidf_scores(df, processed_resume) 
    df = add_embedding_scores(df, processed_resume)
    return df

# if __name__ == "__main__":
    # resume_text = load_resume()
    # results = run_pipeline(resume_text)
    # print(results[["title", "company", "tfidf_score"]].head())
    # print(results.isna().any(), results.isna().sum().sum())