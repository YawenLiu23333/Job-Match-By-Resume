import React, { useState } from 'react'

function Home({ onResumeTextSubmit, onResumeFileSubmit, textLoading, fileLoading }) {
  const [resume, setResume] = useState("")
  const [file, setFile] = useState(null)

  const handleTextSubmit = (event) => {
    event.preventDefault()
    onResumeTextSubmit(resume)
  }

  const handleFileSubmit = (event) => {
    event.preventDefault()
    if (!file) {
      alert("Please choose a PDF file first.")
      return
    }
    onResumeFileSubmit(file)
  }

  return (
    <div className="home-page">
      <div className="home-container">
        <div className="badge">Resume-to-job matching powered by IR scoring</div>

        <h1 className="hero-title">Find the jobs that match your resume best.</h1>

        <p className="hero-subtitle">
          Upload a resume PDF or paste your resume text to rank real job postings using
          TF-IDF relevance and semantic similarity.
        </p>

        <div className="input-grid">
          <div className="input-card">
            <h2>Upload Resume PDF</h2>
            <p>Best if you already have a saved resume file.</p>

            <input
              type="file"
              accept="application/pdf"
              onChange={(event) => setFile(event.target.files[0])}
            />

            <button className="primary-button" onClick={handleFileSubmit} disabled={fileLoading}>
              {fileLoading? "Finding Matches...":"Upload & Match Jobs"}
            </button>
            {fileLoading && (
              <p className="loading-message">
                Analyzing your resume and ranking jobs. This may take a few seconds on the first request.
              </p>
            )}
          </div>

          <div className="input-card">
            <h2>Paste Resume Text</h2>
            <p>Fastest way to test the matching pipeline.</p>

            <form onSubmit={handleTextSubmit}>
              <textarea
                value={resume}
                placeholder="Paste your resume here..."
                onChange={(event) => setResume(event.target.value)}
              />
              
              <button className="primary-button" type="submit" disabled={textLoading}>
                {textLoading? "Finding Matches...": "Find Matches"}
              </button>
            
              {textLoading && (
                <p className="loading-message">
                  Analyzing your resume and ranking jobs. This may take a few seconds on the first request.
                </p>)}

            </form>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home