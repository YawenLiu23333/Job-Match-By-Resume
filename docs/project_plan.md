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


# **Progress Update — May 4**

## **Completed**

1. Refactored project structure:
    Separated pipeline.py from app.py for cleaner, reusable workflow
2. Implemented evaluation framework:
    Used precision-recall curve to analyze model performance
3. Computed best F1 and F2 scores with corresponding thresholds
4. Applied optimal thresholds to:
    Calculate precision, recall, and F1 for both TF-IDF and semantic models
5. Implemented Top-K evaluation:
    Precision@K and Recall@K for ranking-based evaluation
6. Analyzed model behavior: 
    Observed TF-IDF outperforming semantic embedding on small dataset
7. Began scaling effort:
    Researched publicly available resume-job datasets
8. Loaded and mapped a larger dataset (~8k rows)
9. Started building a separate dataset pipeline for pairwise evaluation
10. Initiated TF-IDF computation for new dataset (in progress)

## **Design Decisions**

1. Separated pipeline logic from application logic to improve modularity and enable reuse across experiments and datasets.
2. Used F2 score for threshold selection to prioritize recall, aligning with the goal of retrieving more potentially relevant job matches.
3. Maintained both:
keyword-based (TF-IDF) model as a strong baseline
semantic embedding model for capturing contextual similarity
4. Identified that small sample size and general-purpose embedding model may limit semantic performance.

## **Next Steps**

1. Complete dataset pipeline:
    Efficient preprocessing for larger dataset
2. Pairwise TF-IDF similarity computation
3. Evaluate models on larger dataset:
    Compare TF-IDF vs semantic embedding more reliably
4. Improve semantic matching:
    Experiment with domain-specific models (e.g., JobBERT, MPNet)
5. Develop hybrid scoring model:
    Combine skill-based keyword matching with semantic similarity
6. Assign weights to skills, experience, and contextual relevance
7. (Optional) Optimize preprocessing for scalability:   
    Replace NLTK pipeline with vectorizer-based preprocessing for large data

# **Progress Update — May 7**
## **Completed**
1. completed backend data processing and Flask data fetching 
2. connect front end with back end
3. finished pipeline: user paste resume, React fecthes mathced job and display

