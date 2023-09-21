
import os
import PyPDF2

with open("Resumes/app-0009.pdf","rb") as infile:
    pdfReader = PyPDF2.PdfReader(infile)
    for p in pdfReader.pages:
        print(p.extract_text())





