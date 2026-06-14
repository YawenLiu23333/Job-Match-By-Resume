import React from 'react'

function MatchExplanation({ explanation }) {
  if (!explanation) return null

  return (
    <div className="match-explanation">
      <h4>AI Match Analysis</h4>

      <div className="explanation-grid">
        <div className="explanation-section">
          <h5>Why this job matches</h5>
          <ul>
            {explanation.match_reasons?.map((reason, index) => (
              <li key={index}>{reason}</li>
            ))}
          </ul>
        </div>

        <div className="explanation-section">
          <h5>Missing skills</h5>
          <ul>
            {explanation.missing_skills?.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
        </div>

        <div className="explanation-section">
          <h5>Suggested resume keywords</h5>
          <ul>
            {explanation.suggested_keywords?.map((keyword, index) => (
              <li key={index}>{keyword}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  )
}
export default MatchExplanation;