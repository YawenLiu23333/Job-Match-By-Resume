import React, { useState } from 'react'
import Home from './pages/Home'
import Results from './pages/Results'
import './App.css'

function App() {
  const [matchedJobs, setMatchedJobs] = useState(null)

  const handleResumeTextSubmit = async (resumeInput) => {
    const response = await fetch('/api/match', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ resume: resumeInput }),
    })

    const data = await response.json()
    setMatchedJobs(data)
  }

  const handleResumeFileSubmit = async (file) => {
    const formData = new FormData()
    formData.append("resume_file", file)

    const response = await fetch('/api/match-pdf', {
      method: "POST",
      body: formData,
    })

    const data = await response.json()
    setMatchedJobs(data)
  }

  const handleBack = () => {
    setMatchedJobs(null)
  }

  return (
    <>
      {matchedJobs ? (
        <Results matchedJobs={matchedJobs} onBack={handleBack} />
      ) : (
        <Home
          onResumeTextSubmit={handleResumeTextSubmit}
          onResumeFileSubmit={handleResumeFileSubmit}
        />
      )}
    </>
  )
}

export default App