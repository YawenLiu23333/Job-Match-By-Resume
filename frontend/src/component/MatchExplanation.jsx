import React from 'react'

function MatchExplanation({ explanation }) {
  if (!explanation) return null

  return (
    <div className="match-explanation">
      <h4>AI Match Explanation</h4>

      <h5>Why this job matches</h5>
      <ul>
        {explanation.match_reasons?.map((reason, index) => (
          <li key={index}>{reason}</li>
        ))}
      </ul>

      <h5>Missing skills</h5>
      <ul>
        {explanation.missing_skills?.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>

      <h5>Suggested resume keywords</h5>
      <ul>
        {explanation.suggested_keywords?.map((keyword, index) => (
          <li key={index}>{keyword}</li>
        ))}
      </ul>
    </div>
  )
}

export default MatchExplanation;