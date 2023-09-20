pip install PyPDF2
import os
import PyPDF2

resume_folder = 'Resumes'

#get all files from the specified folder
files = os.listdir(resume_folder)

#loop through all files
for file in files:
    #check if the file extension is .pdf
    if file.endswith('.pdf'):
        #file path
        file_path = os.path.join(resume_folder, file)

        try:
            # Open the file in read-binary mode
            with open("Data/tale2cities-alt.pdf", "rb") as infile:
                # Create a PDF reader object
                pdfReader = PyPDF2.PdfReader(infile)
                print(len(pdfReader.pages))

                # Loop through all pages and display their content
                for page_num, page in enumerate(pdfReader.pages):
                    print(f'Content of {file}, page {page_num + 1}:')
                    print(page.extract_text())

        except Exception as e:
            # Print any exception that occurs during file reading
            print(f"Could not read {file} due to: {str(e)}")




