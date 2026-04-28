import pandas as pd

df = pd.read_csv("data/sample_jobs.csv")
#df = df.dropna(how="all")

print(df.shape)
print(df.head())
print(df.columns)
