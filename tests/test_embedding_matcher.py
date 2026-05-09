import sys
import os

sys.path.append(os.path.abspath("back_end/src"))

from embedding_matcher import job_resume_semantic_matching

query = [
    "Find me a photo of a vehicle parked near a building",
]
docs = [
    "A green car parked in front of a yellow building",
    "A red car driving on a highway",
    "A bee on a pink flower",
    "A wasp on a wooden table",
]

res = job_resume_semantic_matching(query, docs)
print(res)