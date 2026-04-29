import pandas as pd
from data_preprocessing import preprocess_text
from resume_parser import extract_text_from_pdf
from job_matcher import job_resume_similarity
# from embedding_matcher import job_resume_semantic_matching
from evaluation import evaluation_scores

#add comlum 'labeled_score' in df for later evaluation


# process sample jobs
df = pd.read_csv('data/sample_jobs.csv')
df["processed_description"] = df["description"].apply(preprocess_text)
# print(df[["title", "processed_description"]].head())
df['labeled_score'] = [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, ]

# process resume
resume_text = extract_text_from_pdf("data/test_sample_resume.pdf")
processed_resume = preprocess_text(resume_text)
# print(processed_resume[:500])

df = df.reset_index(drop=True)
jobs = df["processed_description"].tolist()
docs = [processed_resume] + jobs
# return ranked results
scores = job_resume_similarity(docs)

# attach score back to jobs
df["tfidf_score"] = scores
sorted_df = df.sort_values(by="tfidf_score", ascending=False)

# show top 5 matching jobs by keywords matching score
top_jobs = sorted_df[:5]
top_jobs = top_jobs[["title", "company", "tfidf_score"]]
top_jobs['tfidf_score'] = top_jobs['tfidf_score'].map('{:.2%}'.format)
top_jobs = top_jobs.reset_index(drop=True)
print(top_jobs)


# attach sematic embedding ranks back to datafram and sort by ranks
# ranks = job_resume_semantic_matching(processed_resume, jobs)
# for rank in ranks:
    # df.loc[rank['corpus_id'], 'embedding_score'] = rank['score']
# sorted_df = df.sort_values(by="embedding_score", ascending=False)

# show top 5 matching jobs by semantic matching score
# semantic_top_jobs = sorted_df[["title", "company", "embedding_score"]].head(5)
# semantic_top_jobs["embedding_score"] = semantic_top_jobs["embedding_score"].map("{:.2%}".format)
# semantic_top_jobs = semantic_top_jobs.reset_index(drop=True)
# print(semantic_top_jobs)

#evaluate key word matching with binary score converted by 0.1 as threshold
tfidf_score_binary = (sorted_df['tfidf_score']>= 0.1).astype(int)
key_word_evaluation = evaluation_scores(df['labeled_score'], tfidf_score_binary)
print('for key word based job match accuracy, precision is: ', key_word_evaluation[0], ', recall score is: ', key_word_evaluation[1], ', F1 score is: ', key_word_evaluation[2], ', MAP score is: ', key_word_evaluation[3], '.')

#evaluate key word matching
# key_word_evaluation = evaluation_scores(df['labeled_score'], sorted_df['embedding_score'])
# print('for semantic analysis job match accuracy, precision is: ', key_word_evaluation[0], ', recall score is: ', key_word_evaluation[1], ', F1 score is: ', key_word_evaluation[2], ', MAP score is: ', key_word_evaluation[3], '.')
