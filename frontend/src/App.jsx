import React, { useState } from "react";
import Home from "./pages/Home";
import Results from "./pages/Results";
import "./App.css";

function App() {
  const [matchedJobs, setMatchedJobs] = useState(null);
  const [explanations, setExplanations] = useState('');
  const [resume, setResume] = useState('');
  const [textLoading, setTextLoading] = useState(false);
  const [fileLoading, setFileLoading] = useState(false);
  const [exLoading, setExLoading] = useState(false);
  const API_URL = import.meta.env.VITE_API_URL;

  const handleResumeTextSubmit = async (resumeInput) => {
    setTextLoading(true);
    const response = await fetch(`${API_URL}/api/match`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ resume: resumeInput }),
    });

    const data = await response.json();
    setMatchedJobs(data);
    setResume(resumeInput);
    setTextLoading(false);
  };

  const handleResumeFileSubmit = async (file) => {
    setFileLoading(true);
    const formData = new FormData();
    formData.append("resume_file", file);

    const response = await fetch(`${API_URL}/api/match-pdf`, {
      method: "POST",
      body: formData,
    })

    const data = await response.json();
    setMatchedJobs(data.results);
    setResume(data.resume_text);
    setFileLoading(false);
  };

  const handleExplanationRequest = async (jobDescription) => {
    setExLoading(true);
    const formData = new FormData();
    formData.append("resume_file", resume);

    const response = await fetch(`${API_URL}/api/match/explanation`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        resume: resume, job_description: jobDescription
      })
    })

    const data = await response.json();
    setExplanations(data);
    console.log(explanations);
    setExLoading(false);
  };

  const handleBack = () => {
    setMatchedJobs(null);
  };

  return (
    <>
      {matchedJobs ? (
        <Results 
        matchedJobs={matchedJobs} 
        onBack={handleBack} 
        onExplanation={handleExplanationRequest} 
        explanation={explanations}
        setExplanations={setExplanations}
        exLoading={exLoading}
        />
      ) : (
        <Home
          onResumeTextSubmit={handleResumeTextSubmit}
          onResumeFileSubmit={handleResumeFileSubmit}
          textLoading={textLoading}
          fileLoading={fileLoading}
        />
      )}
    </>
  );
}

export default App;
