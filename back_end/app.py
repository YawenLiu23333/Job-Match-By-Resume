from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
from pathlib import Path
from src.pipeline import run_pipeline
from src.resume_parser import extract_text_from_pdf
from src.match_explanation import generate_match_explanation

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask backend is running!"

@app.route("/api/match", methods=["POST"])
def resume_match():
    data = request.get_json()
    resume_text = data["resume"]

    results_df = run_pipeline(resume_text, include_embedding=False)
    results = results_df.to_dict(orient="records")

    return jsonify(results)

@app.route("/api/match-pdf", methods=["POST"])
def resume_match_pdf():
    uploaded_file = request.files["resume_file"]
    temp_dir = tempfile.gettempdir()
    temp_path = Path(temp_dir)/ "uploaded_resume.pdf"

    uploaded_file.save(temp_path)

    resume_text = extract_text_from_pdf(temp_path)

    results_df = run_pipeline(resume_text, include_embedding=False)
    results = results_df.to_dict(orient="records")

    return jsonify(results)

@app.route("/api/match/explanation", methods=["POST"])
def resume_match_explanation():

    data = request.get_json()

    resume_text = data["resume"]
    job_description = data["job_description"]

    explanation = generate_match_explanation(
        resume_text, job_description
        )

    return jsonify(explanation)
    
if __name__ == "__main__":
    app.run(debug=True)