import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from embedding_matcher import pairwise_job_resume_semantic_matching

splits = {'train': 'train.csv', 'test': 'test.csv'}
df = pd.read_csv("hf://datasets/cnamuangtoun/resume-job-description-fit/" + splits["train"])
#rdataset format: resume_text + job_description_text + fit_label, data size: 8k rows

def load_dataset_sample(k):  
    #Load k rows 
    small_df = df.sample(n=k, random_state=42).copy()
    print("loaded sample")
    return small_df
    
    # map labels and drop potential fit 
def map_labels(small_df):
    small_df = small_df[small_df["label"] != "Potential Fit"]
    label_map = {
    "Good Fit": 1,
    "No Fit": 0
    }
    small_df["labeled_score"] = small_df["label"].map(label_map)
    small_df = small_df.dropna(subset=["labeled_score"])
    small_df["labeled_score"] = small_df["labeled_score"].astype(int)
    print("labels mapped")
    return small_df

# compute pairwise TF-IDF score 
def tfidf_compute_pair(corpus,resume_len):
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        token_pattern=r"(?u)\b[a-zA-Z]{2,}\b"
    )

    tfidf_matrix = vectorizer.fit_transform(corpus)
    resumes_tfidf = tfidf_matrix[:resume_len]
    jobs_tfidf = tfidf_matrix[resume_len:]
    scores = []
    for i in range(resume_len):
        sim = cosine_similarity(
        resumes_tfidf[i],
        jobs_tfidf[i])[0][0]
        scores.append(sim)
    print("tfidf computed")
    return scores

def run_dataset_pipeline(k):
    #takes k as sample saize 
    sample_dataset = load_dataset_sample(k)
    mapped_dataset = map_labels(sample_dataset)
    
    resumes = mapped_dataset['resume_text'].tolist()
    jobs = mapped_dataset['job_description_text'].tolist()
    all_text = resumes + jobs
    resume_len = mapped_dataset.shape[0]

    #calculate tfidf/semantic scores and attach back to df
    scores = tfidf_compute_pair(all_text,resume_len)
    mapped_dataset["tfidf_score"] = scores
    semantic_scores = pairwise_job_resume_semantic_matching(resumes, jobs)
    mapped_dataset["embedding_score"] = semantic_scores
    print("pipeline finished")
    return mapped_dataset

    # evaluate
# if __name__ == "__main__":
    # df = run_dataset_pipeline(500)
    # print(df.shape)
    # print(df["label"].value_counts())