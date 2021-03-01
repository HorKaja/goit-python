import os
from pathlib import Path
import re
import sys
from shutil import copyfile, move, unpack_archive


def normalize(string):
    '''
    Convert Cyrillic symbols in string into Latin symbols and  special characters into "_"-symbol.
        Parameters:
            string (str): text with symbols in Cyrillic /optional:with digits and/or special characters
        Returns:
            string (str): text with symbols in Latin /optional:with digits and/or "_"-symbols
    '''

    symbol_map = {ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B', ord('в'): 'v', ord('В'): 'V', ord('г'): 'g', ord('Г'): 'G', ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E', ord('ё'): 'jo', ord('Ё'): 'Jo', ord('ж'): 'zh', ord('Ж'): 'Zh', ord('з'): 'z', ord('З'): 'Z', ord('и'): 'i', ord('И'): 'I', ord('й'): 'y', ord('Й'): 'Y', ord('к'): 'k', ord('К'): 'K', ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M', ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O', ord('п'): 'p', ord(
        'П'): 'P', ord('р'): 'r', ord('Р'): 'R', ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T', ord('у'): 'u', ord('У'): 'U', ord('ф'): 'f', ord('Ф'): 'F', ord('х'): 'h', ord('Х'): 'H', ord('ц'): 'ts', ord('Ц'): 'Ts', ord('ч'): 'ch', ord('Ч'): 'Ch', ord('ш'): 'sh', ord('Ш'): 'Sh', ord('щ'): 'shch', ord('Щ'): 'Shch', ord('ы'): 'y', ord('Ы'): 'Y', ord('ь'): '', ord('Ь'): '', ord('ъ'): '', ord('Ъ'): '', ord('э'): 'e', ord('Э'): 'E', ord('ю'): 'ju', ord('Ю'): 'Ju', ord('я'): 'Ja', ord('Я'): 'Ja', }
    lat_str = string.translate(symbol_map)
    fixed_str = re.sub(r'\W', "_", lat_str)
    return fixed_str


def sort_folder(p):
    '''
    Recursively sort the folder content according to files extentions.
    Files with uncommon extentions stay unsorted.
        Parameters:
            p (pathlib.WindowsPath): absolute path to a folder to sort
    '''
    os.chdir(str_pass)
    music_files_ext = ('.mp3', '.ogg', '.waw', '.amr')
    image_files_ext = ('.jpeg', '.png', '.jpg', '.pdf')
    document_files_ext = ('.doc', '.docx', '.txt',
                          '.pdf', '.xls', '.pptx', '.xlsx')
    archieve_files_ext = ('.zip', '.gz', '.tar')
    video_files_ext = ('.avi', '.mp4', '.mov')
    if p.is_dir():
        for item in p.iterdir():
            sort_folder(item)
    else:
        file_name = p.stem
        file_extension = os.path.splitext(p)[1]
        if file_extension in music_files_ext:
            os.makedirs(str_pass + "\\audio", exist_ok=True)
            move(p, str_pass + "\\audio" + normalize(file_name) + file_extension)
        elif file_extension in image_files_ext:
            os.makedirs(str_pass + "\\images", exist_ok=True)
            move(p, str_pass + "\\images\\" +
                 normalize(file_name) + file_extension)
        elif file_extension in document_files_ext:
            os.makedirs(str_pass + "\\documents", exist_ok=True)
            move(p, str_pass + "\\documents\\" +
                 normalize(file_name) + file_extension)
        elif file_extension in video_files_ext:
            os.makedirs(str_pass + "\\video", exist_ok=True)
            move(p, str_pass + "\\video\\" +
                 normalize(file_name) + file_extension)
        elif file_extension in archieve_files_ext:
            os.makedirs(str_pass + "\\archieves", exist_ok=True)
            unpack_archive(p, str_pass + "\\archieves\\")


print("Thank's Lord, this mess has been finally sorted!)")


def main():

    global str_pass
    str_pass = sys.argv[1]
    path = Path(sys.argv[1])  # e.g. "F:/My_personal_info/My_test/"
    sort_folder(path)


if __name__ == '__main__':
    main()
