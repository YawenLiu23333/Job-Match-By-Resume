from sentence_transformers import CrossEncoder
model = CrossEncoder("cross-encoder/stsb-distilroberta-base")

def job_resume_semantic_matching(processed_resume, jobs):
    ranks = model.rank(processed_resume, jobs)
    return ranks
    
    
    

