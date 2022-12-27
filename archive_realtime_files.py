import os
import datetime
from zipfile import ZipFile

# abspath = os.path.abspath(os.path.dirname(__file__))
# dname = os.path.dirname(abspath)
# os.chdir(dname)

    
# Function to delete realtime graph that has been sent.
def deleteAllFiles(folderPath):
    for file in os.listdir(folderPath):
        # Grab only png files
        if file.endswith(".rrd") or file.endswith(".png"):
            file_path = os.path.join(folderPath, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)

def get_all_graphs(directory):
    images = []
    for image in os.listdir(directory):
        if image.endswith('.png'):
            imagefilepath = os.path.join(directory, image)
            images.append(imagefilepath)

    return images

def zip_rename_file(imageDir):
    # path to folder which needs to be zipped
    directory = imageDir
  
    # calling function to get all file paths in the directory
    file_paths = get_all_graphs(directory)
  
    date_time = str(datetime.datetime.now())
    # writing files to a zipfile
    with ZipFile(date_time + '.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')        


imagedirectory = '.'

get_all_graphs(imagedirectory)
zip_rename_file(imagedirectory)
deleteAllFiles(imagedirectory)
