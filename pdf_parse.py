import pdfplumber
import PyPDF2
import os
from PyPDF2 import PdfReader


def GetFolderContents(path):
    dirListing = os.listdir(path)
    editFiles = []
    for item in dirListing:
        if ".pdf" in item:
            editFiles.append(path+'\\'+item)
    print(editFiles)

GetFolderContents("C:\Users\Kaushal\Desktop\RAG\PDF_collection")

"""
reader = PdfReader("")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
"""
