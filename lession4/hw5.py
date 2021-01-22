from pathlib import Path

# input a valid adress of the target folder to path after running the file hw5.py
content = Path("F:\My_personal_info")

# create a list of file-names of the target folder
#content = os.listdir(path)
music_files = []
image_files = []
document_files = []
video_files = []
archieve_files = []
unknown_files = []
# create empty sets to add the extentions of found files
known_extensions = set()
unknown_extensions = set()

# define a sorting function
def sort_folder(p):

    
    global known_extensions
    global unknown_extensions

    global music_files
    global image_files
    global document_files
    global video_files
    global archieve_files
    global unknown_files
    
    # define sets of known file extentions
    music_files_ext = ('mp3', 'ogg', 'waw', 'amr')
    image_file_ext = ('jpeg', 'png', 'jpg', 'pdf')
    document_files_ext = ('doc', 'docx', 'txt', 'pdf', 'xls', 'pptx', 'xlsx'),
    archieve_files_ext = ('zip', 'gz', 'tar')
    video_files_ext = ('avi', 'mp4', 'mov')
    for item in p.iterdir():
        # sort all files according to extension
        if item.is_file():
            file = str(item)
            file_extension = file.rsplit('.', 1)[-1]
            if file_extension in music_files_ext:
                music_files.append(file)
                known_extensions.add(file_extension)
            elif file_extension in image_file_ext:
                image_files.append(file)
                known_extensions.add(file_extension)
            elif file_extension in document_files_ext:
                document_files.append(file)
                known_extensions.add(file_extension)
            elif file_extension in video_files_ext:
                video_files.append(file)
                known_extensions.add(file_extension)
            elif file_extension in archieve_files_ext:
                archieve_files.add(file)
                known_extensions.add(file_extension)
            else:
                unknown_files.append(file)
                unknown_extensions.add(file_extension)
        else:
            return sort_folder(item)
    return music_files, image_files, document_files, video_files, archieve_files, unknown_files, known_extensions, unknown_extensions


sort_folder(content)

print(f"Music files: {music_files} \n"
      f"Image files: {image_files} \n"
      f"Document files: {document_files} \n"
      f"Video files: {video_files} \n"
      f"Archieve files: {archieve_files} \n"
      f"Unknown files or folders: {unknown_files} \n"
      )
print(
    f"We have files with the following extensions in this folder we know: {known_extensions}")
print(
    f"We have files with the following extensions in this folder we don't know: {unknown_extensions}")

