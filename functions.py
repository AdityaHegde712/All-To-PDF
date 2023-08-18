import os
END = '\n\n------------------------------------------------------------\n\n'

def read_and_add_files(file):
    with open(file, 'r') as f:
        content = f.read()

    # Append this text into a pdf file on a new page
    with open(f"{folder}.pdf", 'a') as f:
        f.write(content)
        f.write(END)

def readfolder(path='./'):
    for file in os.listdir(path):
        if file == '.git': # Avoid the github setup files
            pass
        else:
            new_path = path + '/' + file
            if os.path.isdir(new_path):
                readfolder(new_path)
            else:
                read_and_add_files(new_path)



folder = input("Enter the name of the folder containing your files: ")

readfolder(folder)
