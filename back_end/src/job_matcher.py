from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
vectorizer = TfidfVectorizer()


def job_resume_similarity(docs):
    tfidf_matrix = vectorizer.fit_transform(docs)
    resume_tfidf = tfidf_matrix[0]
    jobs_tfidf = tfidf_matrix[1:]
    score = []
    for job_tfidf in jobs_tfidf:
        similarity = cosine_similarity(resume_tfidf, job_tfidf)[0][0]
        score.append(similarity)

    return score

    
    
    


    
    

