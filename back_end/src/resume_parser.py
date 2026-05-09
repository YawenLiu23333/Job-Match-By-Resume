from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text()

    return text
# test for terminal src module not found issue
# file_patch = "../../data/test_sample_resume.pdf"
# res = extract_text_from_pdf(file_patch)
# print(res[:500])



