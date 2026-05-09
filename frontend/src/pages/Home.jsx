import React, { useState } from 'react'

function Home({ onResumeTextSubmit, onResumeFileSubmit }) {
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

            <button className="primary-button" onClick={handleFileSubmit}>
              Upload & Match Jobs
            </button>
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

              <button className="primary-button" type="submit">
                Find Matches
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home