import os
import re

try:
    with open("mbox-short.txt","rb") as infile:

        data = infile.read()
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(pattern, data) #find email addresses

        for e in set(emails):
            print(e)

except Exception as e:
    # Print any exception that occurs during file reading
    print(f'Could not read due to: {str(e)}')







