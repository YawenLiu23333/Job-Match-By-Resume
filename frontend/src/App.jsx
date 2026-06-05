import React, { useState } from "react";
import Home from "./pages/Home";
import Results from "./pages/Results";
import "./App.css";

function App() {
  const [matchedJobs, setMatchedJobs] = useState(null);
  const API_URL = import.meta.env.VITE_API_URL;

  const handleResumeTextSubmit = async (resumeInput) => {
    console.log("API URL:", import.meta.env.VITE_API_URL)
    const response = await fetch(`${API_URL}/api/match`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ resume: resumeInput }),
    });

    const data = await response.json();
    setMatchedJobs(data);
  };

  const handleResumeFileSubmit = async (file) => {
    console.log("API URL:", import.meta.env.VITE_API_URL)
    const formData = new FormData();
    formData.append("resume_file", file);

    const response = await fetch(`${API_URL}/api/match-pdf`, {
      method: "POST",
      body: formData,
    })

    const data = await response.json();
    setMatchedJobs(data);
  };

  const handleBack = () => {
    setMatchedJobs(null);
  };

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
  );
}

export default App;
