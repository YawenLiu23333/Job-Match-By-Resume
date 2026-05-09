import React from 'react'

function JobCard({ job, onClick }) {
  return (
    <div className="job-card" onClick={onClick}>
      <h2>{job.title}</h2>
      <p><strong>Company:</strong> {job.company}</p>
      <p><strong>Location:</strong> {job.location}</p>

      <div className="score-pill">
        Match Score: {(Number(job.tfidf_score) * 100).toFixed(1)}%
      </div>

      <p className="click-hint">Click to view job details</p>
    </div>
  )
}

export default JobCard