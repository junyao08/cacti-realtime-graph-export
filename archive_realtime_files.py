import os
from zipfile import ZipFile

abspath = os.path.abspath(os.path.dirname(__file__))
dname = os.path.dirname(abspath)
os.chdir(dname)

    

def zip_rename_file(imageDir):
    # path to folder which needs to be zipped
    directory = imageDir
  
    # calling function to get all file paths in the directory
    

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
  
    # writing files to a zipfile
    with ZipFile('my_python_files.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')        


