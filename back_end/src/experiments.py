from sklearn.metrics import precision_recall_curve
import numpy as np
import pandas as pd
from pipeline import run_pipeline
from dataset_pipeline import run_dataset_pipeline

#find threshold with max f1, f2 score
def find_best_threshold(y_true, y_scores):
    precision, recall, thresholds = precision_recall_curve(
        y_true, y_scores)
    #find best F1
    f1_scores = (2 * precision * recall) / (precision + recall + 1e-10) # 1e-10 avoids div by zero
    best_f1_index = np.argmax(f1_scores)
    best_f1 = f1_scores[best_f1_index]
    best_f1_thresh = thresholds[best_f1_index]

    #find best F2 (emphasizes recall)
    beta = 2
    f2_scores = ((1 + beta**2) * precision * recall) / (beta**2 * precision + recall + 1e-10)
    best_f2_index = np.argmax(f2_scores)
    best_f2 = f2_scores[best_f2_index]
    best_f2_thresh = thresholds[best_f2_index]

    result = [best_f1,best_f1_thresh,best_f2,best_f2_thresh]
    return result

#Top-K evaluation
def top_k_evaluation(k, df, test_score):
    sorted_df = df.sort_values(by=test_score, ascending=False)
    sliced_df = sorted_df[:k]

    retrieved = (sliced_df["labeled_score"] == 1).sum()
    precision_at_k = retrieved/k

    total_relevant = (df["labeled_score"] == 1).sum()
    recall_at_k = retrieved/total_relevant

    return([precision_at_k, recall_at_k])

if __name__ == "__main__":
# test initial data
# tfidf_evaluation_at_5 = top_k_evluation(5, df, "tfidf_score")
# embedding_evaluation_at_5 = top_k_evluation(5, df, "embedding_score")
# print(tfidf_evaluation_at_5, embedding_evaluation_at_5)
# 
# test intial data
# # df = run_pipeline() 
# tfidf_best_thresholds = find_best_threshold(df["labeled_score"], df["tfidf_score"])
# embedding_best_thresholds = find_best_threshold(df["labeled_score"], df["embedding_score"])
# print('key-word-based model best f1: ', tfidf_best_thresholds[0], 
    #   ', at threshold: ', tfidf_best_thresholds[1],', best f2: ', 
    #   tfidf_best_thresholds[2], ', at threshold: ', tfidf_best_thresholds[3],
    #   'semantic-embedding-based model best f1: ', embedding_best_thresholds[0], 
    # ', at threshold: ', embedding_best_thresholds[1],', best f2: ', 
    # embedding_best_thresholds[2], ', at threshold: ', embedding_best_thresholds[3])
    
    # test dataset1 for f1/f2 & top k
    dataset_df = run_dataset_pipeline(2000) #parameter: size of sample 
    tfidf_best_f1f2_threshold = find_best_threshold(dataset_df["labeled_score"], dataset_df["tfidf_score"])
    embedding_best_f1f2_threshold = find_best_threshold(dataset_df["labeled_score"], dataset_df["embedding_score"])
    print(tfidf_best_f1f2_threshold, embedding_best_f1f2_threshold)  
    for k in [10, 20, 50, 100]:
        print(k, top_k_evaluation(k, dataset_df, "tfidf_score"))
        print(k, top_k_evaluation(k, dataset_df, "embedding_score"))

