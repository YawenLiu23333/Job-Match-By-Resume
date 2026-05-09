from pipeline import run_pipeline
from evaluation import evaluation_scores

# df = run_pipeline()

# show top 5 matching jobs by keywords matching score
# sorted_df = df.sort_values(by="tfidf_score", ascending=False)
# top_jobs = sorted_df[:5]
# top_jobs = top_jobs[["title", "company", "tfidf_score"]]
# top_jobs['tfidf_score'] = top_jobs['tfidf_score'].map('{:.2%}'.format)
# top_jobs = top_jobs.reset_index(drop=True)
# print(top_jobs)


# attach sematic embedding ranks back to datafram and sort by ranks
# semantic_sorted_df = df.sort_values(by="embedding_score", ascending=False)
 
# show top 5 matching jobs by semantic matching score
# semantic_top_jobs = sorted_df[["title", "company", "embedding_score"]].head(5)
# semantic_top_jobs["embedding_score"] = semantic_top_jobs["embedding_score"].map("{:.2%}".format)
# semantic_top_jobs = semantic_top_jobs.reset_index(drop=True)
# print(semantic_top_jobs)
# 
#evaluate key word matching with binary score converted by data median as threshold
# tfidf_score_binary = (df['tfidf_score']>= 0.04327523030864779).astype(int)
# key_word_evaluation = evaluation_scores(df['labeled_score'], tfidf_score_binary)
# print('for key word based job match performance (with best f2 threshold), precision is: ', key_word_evaluation[0], ', recall score is: ', key_word_evaluation[1], ', F1 score is: ', key_word_evaluation[2], '.')
# 
#evaluate key word matching with data median as threshold
# semantic_score_binary = (df['embedding_score']>= 0.5179589986801147).astype(int)
# semantic_evaluation = evaluation_scores(df['labeled_score'],semantic_score_binary)
# print('for semantic analysis job match performance (with best f2 threshold), precision is: ', semantic_evaluation[0], ', recall score is: ', semantic_evaluation[1], ', F1 score is: ', semantic_evaluation[2], '.')


