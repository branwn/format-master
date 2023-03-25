import os
from PyPDF2 import PdfReader

# set directory containing PDF files
directory = './'

# create output directory for text files
output_dir = os.path.join(directory, './')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# loop through all PDF files in directory
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        # open PDF file
        pdf_file = open(os.path.join(directory, filename), 'rb')

        # create PDF reader object
        pdf_reader = PdfReader(pdf_file)

        # create output text file
        text_file = open(os.path.join(output_dir, filename.replace('.pdf', '.txt')), 'w')

        # loop through all pages in PDF file
        for page in pdf_reader.pages:
            # extract text from page and write to output file
            text = page.extract_text()
            text_file.write(text)

        # close files
        pdf_file.close()
        text_file.close()
