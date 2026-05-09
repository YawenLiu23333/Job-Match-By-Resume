import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "back_end" / "src"))

from pipeline import run_pipeline

df = run_pipeline()
print(df["embedding_score"].min())
print(df["embedding_score"].max())
print(df["embedding_score"].head())