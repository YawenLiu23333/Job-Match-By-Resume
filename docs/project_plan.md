# **Progress Update — Day 1**

## **Completed**

1. Created project structure
2. Prepared 20 real-world job postings dataset from LinkedIn and company career pages
3. Converted postings into CSV format
4. Added sample resume PDF for testing
5. Implemented text preprocessing pipeline:
    tokenization
    stopword removal
    lemmatization
6. Built resume parser

## **Design Decisions**

Chose lemmatization over stemming for higher precision in resume/job matching.
Plan to combine traditional IR methods (TF-IDF / cosine similarity) with semantic embeddings later.

## **Next Steps**

Build TF-IDF ranking system
Add semantic embedding matching
Expand dataset using Kaggle / web scraping
Create input handle later to manage: uploaded PDF, local TXT, URL, HTML pag, LinkedIn profile etc.