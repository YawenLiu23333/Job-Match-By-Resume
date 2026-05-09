# from sentence_transformers import CrossEncoder
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
# model = CrossEncoder("cross-encoder/stsb-distilroberta-base")


def job_resume_semantic_matching(processed_resume, job):
    # for job in jobs:
    query_embeddings = model.encode(processed_resume)
    doc_embeddings = model.encode(job)
    similarities = model.similarity(query_embeddings, doc_embeddings)
    return similarities

def pairwise_job_resume_semantic_matching(resumes, jobs):
    query_embeddings = model.encode(resumes)
    doc_embeddings = model.encode(jobs)
    scores = []
    for i in range(len(resumes)):
        similarity = model.similarity(query_embeddings[i], doc_embeddings[i]).item()
        scores.append(similarity)
    return scores


    
    

