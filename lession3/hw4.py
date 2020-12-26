import os
import sys

# input a valid adress of the target folder to path after running the file hw4.py
path = sys.argv[1]
print(f"Start in {path}")

# create a list of file-names of the target folder
files = os.listdir(path)

# create a set for file extensions
extensions_names = set()
# create lists for each file-group
music_files = []
image_files = []
document_files = []
video_files = []
unknown_files_and_folders = []
music_files_ext = ('.mp3', '.ogg', '.waw', '.amr')
image_file_ext = ('.jpeg', '.png', '.jpg', '.pdf')
document_files_ext = ('.doc', '.docx', '.txt')
video_files_ext = ('.avi', '.mp4', '.mov')
# variables to manage loop
name_len, index_of_dot = 0, 0

# sort all files according to extension
for file in files:
    name_len = len(file)
    for char in file:
        index_of_dot = file.rfind('.')
    extensions_names.add(file[index_of_dot:name_len:1])
    if file.endswith(music_files_ext):
        music_files.append(file)
    elif file.endswith(image_file_ext):
        image_files.append(file)
    elif file.endswith(document_files_ext):
        document_files.append(file)
    elif file.endswith(video_files_ext):
        video_files.append(file)
    else:
        unknown_files_and_folders.append(file)


print(f"Music files: {music_files} \n"
      f"Image files: {image_files} \n"
      f"Document files: {document_files} \n"
      f"Video files: {video_files} \n"
      f"Unknown files or folders: {unknown_files_and_folders} \n"
      )
print(
    f"We have files with the following extensions in this folder: {extensions_names}")
