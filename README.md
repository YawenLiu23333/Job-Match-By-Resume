# Job Match By Resume

A resume-to-job matching web application that ranks job postings using TF-IDF relevance and semantic embedding similarity.

This project was developed to make job searching more efficient and less stressful for job seekers. Users can either paste resume text directly or upload a resume PDF file. The system processes the resume, compares it against job postings, and returns ranked job matches based primarily on TF-IDF similarity scores, since resume-job matching relies heavily on exact skills, technologies, and experience keywords. Semantic similarity scores are also provided as an additional reference to capture broader meaning-based relationships between resumes and job descriptions.

## Features

* Resume text input
* Resume PDF upload
* TF-IDF-based job ranking
* Semantic embedding similarity scoring
* Expandable job detail view
* Paginated search results
* React frontend with Flask backend API
* Responsive and modern UI design

## Tech Stack

### Frontend

* React
* Vite
* CSS

### Backend

* Flask
* pandas
* scikit-learn
* sentence-transformers
* PyPDF

## Demo

https://github.com/user-attachments/assets/b6d023d2-07c4-4433-b27b-05bfd39205ad

## Installation

Follow these steps to run the project locally.

### 1. Clone Repository

```bash
git clone https://github.com/YawenLiu23333/Job-Match-By-Resume.git
cd Job-Match-By-Resume
```

### 2. Install Backend Dependencies

```bash
cd back_end
pip install -r requirements.txt
```

### 3. Run Backend Server

```bash
python app.py
```

The Flask backend will run on:

```text
http://127.0.0.1:5000
```

### 4. Install Frontend Dependencies

Open a new terminal:

```bash
cd frontend
npm install
```

### 5. Run Frontend

```bash
npm run dev
```

The React frontend will run on:

```text
http://localhost:5173
```

## Future Improvements

* Live web scraping of real-time job postings
* Hybrid ranking models combining TF-IDF and semantic embeddings
* Domain-specific job matching models
* Improved explainability for matched and missing skills
* Enhanced frontend UI and analytics dashboard
