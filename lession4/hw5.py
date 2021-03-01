import os
import sys
from pathlib import Path
import re


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


def sort_folder(p):

    # define sets of known file extentions
    music_files_ext = ('.mp3', '.ogg', '.waw', '.amr')
    image_file_ext = ('.jpeg', '.png', '.jpg', '.pdf')
    document_files_ext = ('.doc', '.docx', '.txt',
                          '.pdf', '.xls', '.pptx', '.xlsx')
    archieve_files_ext = ('.zip', '.gz', '.tar')
    video_files_ext = ('.avi', '.mp4', '.mov')
    if p.is_dir():
        for item in p.iterdir():
            sort_folder(item)
    else:
        file = p.name
        file_extension = os.path.splitext(p)[1]
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
            archieve_files.append(file)
            known_extensions.add(file_extension)
        else:
            unknown_files.append(file)
            unknown_extensions.add(file_extension)
    return music_files, image_files, document_files, video_files, archieve_files, unknown_files, known_extensions, unknown_extensions


def main():
    # e.g. "F:/My_personal_info/My_test/"
    path = Path(sys.argv[1])
    sort_folder(path)


if __name__ == '__main__':
    main()


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
    f"We have files with the following files extensions we don't know: {unknown_extensions}")
