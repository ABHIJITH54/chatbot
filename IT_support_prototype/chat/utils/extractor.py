from docx import Document

def extract_paragraphs_from_docx(file_path):
    doc=Document(file_path)
    return [p.text.strip() for p in doc.paragraphs if p.text.strip()]

file_path=r"C:\Users\ACER USER\Downloads\COMPREHENSIVE IT SUPPORT KNOWLEDGE BASE FOR RAG IMPLEMENTATION.docx"

paragraphs = extract_paragraphs_from_docx(file_path)

