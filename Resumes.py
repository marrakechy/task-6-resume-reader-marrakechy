
import os
import PyPDF2

try:
    with open("Resumes/app-0009.pdf","rb") as infile:

        pdfReader = PyPDF2.PdfReader(infile)
        for p in pdfReader.pages:
            print(p.extract_text())

except Exception as e:
    # Print any exception that occurs during file reading
    print(f"Could not read due to: {str(e)}")







