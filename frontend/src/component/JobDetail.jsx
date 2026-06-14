import React from 'react'
import MatchExplanation from './MatchExplanation';

function JobDetail({ job, onExplanation, exLoading, explanation}) {
  return (
    <div className="job-detail">
      <h3>Job Details</h3>

      <p><strong>Title:</strong> {job.title}</p>
      <p><strong>Company:</strong> {job.company}</p>
      <p><strong>Location:</strong> {job.location}</p>

      <p>
        <strong>Primary TF-IDF Score:</strong> {(Number(job.tfidf_score) * 100).toFixed(1)}%
      </p>

      {job.embedding_score !== undefined && (
        <p>
          <strong>Semantic Similarity Score:</strong> {(Number(job.embedding_score) * 100).toFixed(1)}%
        </p>
      )}

      <button className="ai-button" onClick={() => onExplanation(job.description)}>
        {exLoading? "Generating AI analysis...":"Show AI-powered explanation"}
      </button>
      {explanation && <MatchExplanation explanation={explanation}/>}

      <div className="score-explanation">
        TF-IDF emphasizes keyword overlap between your resume and the job description.
        Semantic similarity compares broader meaning using embeddings, so it may look higher
        even though TF-IDF is used as the primary ranking method.
      </div>

      <p><strong>Description:</strong></p>
      <p>{job.description}</p>

      {job.link && (
        <a className="apply-link" href={job.link} target="_blank" rel="noreferrer">
          View / Apply for Job
        </a>
      )}
    </div>
  )
}

export default JobDetail