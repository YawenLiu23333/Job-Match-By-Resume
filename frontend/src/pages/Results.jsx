import React, { useState } from 'react'
import JobCard from '../component/JobCard'
import JobDetail from '../component/JobDetail'

function Results({ matchedJobs, onBack }) {
  const [selectedJobIndex, setSelectedJobIndex] = useState(null)

  const handleJobClick = (index) => {
    selectedJobIndex === index
      ? setSelectedJobIndex(null)
      : setSelectedJobIndex(index)
  }
  const jobsPerPage = 5
  const [currentPage, setCurrentPage] = useState(1)

  const totalPages = Math.ceil(matchedJobs.length / jobsPerPage)

  const startIndex = (currentPage - 1) * jobsPerPage
  const endIndex = startIndex + jobsPerPage
  const currentJobs = matchedJobs.slice(startIndex, endIndex)

  return (
    <div className="results-page">
      <div className="results-container">
        <div className="results-header">
          <h1>Your Matched Jobs</h1>
          <p className="score-note">
            Jobs are ranked by <strong>TF-IDF relevance</strong> because it performed better
            in evaluation. Semantic similarity is shown as a secondary signal to capture
            broader meaning between your resume and each job description.
          </p>
        </div>

        {currentJobs.map((job, index) => {
          const actualIndex = startIndex + index

          return (
            <div key={actualIndex}>
              <JobCard job={job} onClick={() => handleJobClick(actualIndex)} />

              {selectedJobIndex === actualIndex && (
              <JobDetail job={job} />
              )}
            </div>
            )
          })}

        <div className="pagination">
          {Array.from({ length: totalPages }, (_, index) => (
          <button
            key={index}
            className={
              currentPage === index + 1
                ? "page-button active-page"
                : "page-button"
                }
            onClick={() => {
              setCurrentPage(index + 1)
              setSelectedJobIndex(null)
            }}
          >
          {index + 1}
            </button>
          ))}
        </div>

        <button className="back-button" onClick={onBack}>
          Go Back
        </button>
      </div>
    </div>
  )
}

export default Results