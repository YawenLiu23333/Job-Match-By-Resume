import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report

# Example DataFrame
df = pd.DataFrame({
    'y_true': [0, 1, 1, 0, 1, 0],
    'y_pred': [0, 1, 0, 0, 1, 1]
})

# Calculate individual metrics
precision = precision_score(df['y_true'], df['y_pred'])
recall = recall_score(df['y_true'], df['y_pred'])
f1 = f1_score(df['y_true'], df['y_pred'])

res = []
res += [precision, recall, f1]
print(res)




