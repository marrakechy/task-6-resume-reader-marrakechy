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




