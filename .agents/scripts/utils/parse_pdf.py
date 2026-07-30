import os
import PyPDF2
import json

def parse_pdf(file_path):
    out = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            out += page.extract_text() + "\n"
    return out

if __name__ == "__main__":
    text = parse_pdf(r"C:\Users\caida\Downloads\Event tracking _ MyVNPT - Payment (1).pdf")
    with open("temp_pdf_output.txt", "w", encoding='utf-8') as f:
        f.write(text)
