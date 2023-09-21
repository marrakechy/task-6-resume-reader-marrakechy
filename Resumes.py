import os
import re

try:
    with open("mboc-short.txt","rb") as infile:

        data = infile.read()
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        for p in pdfReader.pages:
            print(p.extract_text())

except Exception as e:
    # Print any exception that occurs during file reading
    print(f"Could not read due to: {str(e)}")







