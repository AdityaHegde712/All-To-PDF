# Project currently on hold due to other projects going on, will be continued in future

# All-To-PDF - A Lab Report creator for college computer science students
**Features**:
* Read through folders and subfolders for files, add them to a pdf document.
* Top folder will be the name of the PDF
* Subfolders will be section headings
* Each file name will be considered a page heading, and the contents of the file become the page contents. The contents will be followed by 2 or 3 blank lines, a title called "output", and the output text. For this, there will be another file that runs the target file and retrieves output and sends the output string back to where it was called. Of course, this wouldn't work if the output is an image. It would have to be text output. 
* This effectively reproduces all content as a report that's immediately submit-able for college students, rather than having to manually copy, reformat, etc. 
* Standard used fonts for headings etc will be updated in future. 
* The program will also read from an existing PDF if you want it to append new pages instead (useful when adding more content), but this feature will be added after the prior ones are implemented. 

**Future Features**:
* Image addition to word docs
* Image output retrieval also added to the output section
* Read and append an existing pdf report of your lab with the correct formatting. 
