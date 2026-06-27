import shutil
import os

# copy file
shutil.copy("shutil.py","shutil2.py")

# Copy Folder
shutil.copytree(".Day11","myDay11") 

# Move File/Folder
shutil.move("") 

# Delete file
os.remove("shutil2.py") 

# Delete an empty folder
os.rmdir("empty_folder")

# Delete a folder with all its contents
shutil.rmtree("myDay11")