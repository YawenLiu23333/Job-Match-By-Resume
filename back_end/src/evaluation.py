import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score

def evaluation_scores(true, predict):
    evaluation_output = []

    precision = precision_score(true, predict)
    recall = recall_score(true, predict)
    f1 = f1_score(true, predict)
    # use continuous scores not binary scores for MAP
    # map_score = average_precision_score(true, predict)

    evaluation_output += [precision, recall, f1]
    return evaluation_output

