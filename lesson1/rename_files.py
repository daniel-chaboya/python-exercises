import os

print "Type the path of the directory containing your files"

files_dir = raw_input()
files_dir.replace("\\", "//")

def rename_files():
    files = os.listdir(files_dir)
    root_dir = os.getcwd()
    os.chdir(files_dir)
    for file in files:
        print "Renaming " + file + " to " + file.translate(None, "0123456789")
        os.rename(file, file.translate(None, "0123456789"))
    os.chdir(root_dir)
    print "Done renaming files"

rename_files()
