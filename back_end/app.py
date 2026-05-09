from flask import Flask, request, jsonify
from src.pipeline import run_pipeline, DATA_DIR
from src.resume_parser import extract_text_from_pdf

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask backend is running!"

@app.route("/api/match", methods=["POST"])
def resume_match():
    data = request.get_json()
    resume_text = data["resume"]

    results_df = run_pipeline(resume_text)
    results = results_df.to_dict(orient="records")

    return jsonify(results)

@app.route("/api/match-pdf", methods=["POST"])
def resume_match_pdf():
    uploaded_file = request.files["resume_file"]

    temp_path = DATA_DIR / "uploaded_resume.pdf"
    uploaded_file.save(temp_path)

    resume_text = extract_text_from_pdf(temp_path)

    results_df = run_pipeline(resume_text)
    results = results_df.to_dict(orient="records")

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)