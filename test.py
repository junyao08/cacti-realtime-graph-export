import os

# Specify the original and new filenames
original_filename = 'user_fd1c6a9e31fcf122c68cfe602b2052bff8bec2e060576fe041f36f2cc463ca4d_lgi_515.png'
new_filename = original_filename[-7:]

print(new_filename)
# Use the rename function to rename the file
os.rename(original_filename, new_filename)
