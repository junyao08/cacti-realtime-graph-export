import os, shutil
import logging


# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
f_handler = logging.FileHandler('deleted-files.log')
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)

# Function to delete realtime graph that has been sent.
def deleteAllFiles(folderPath):
    for file in os.listdir(folderPath):
        # Grab only png files
        if file.endswith(".rrd") or file.endswith(".png"):
            file_path = os.path.join(folderPath, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                logger.error('File removed: ', file)
            except Exception as e:
                logger.error('Failed to delete %s. Reason: %s' % (file_path, e))