import os
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from docx.oxml.ns import qn
from all_functions_needed import *

def main():
    # Get user input for the top-level folder
    folder = input("Enter the top-level folder name: ")

    # Create a new document
    doc = create_document(folder)

    # Process the top-level folder and its contents
    process_folder(doc, folder)

    # Save the document
    doc.save(f"{folder}.docx")
    print(f"Document '{folder}.docx' created.")

if __name__ == "__main__":
    main()