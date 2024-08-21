import os
from dotenv import load_dotenv
from tools import parseBoolean, isEmpty
from rich import print
 
load_dotenv()
use_main_file = parseBoolean(os.getenv('USE_MAIN_FILE'))
main_file_name = os.getenv('MAIN_FILE_NAME')
main_extension = os.getenv('MAIN_EXTENSION')
file_name_wp = os.getenv('FILE_NAME_WP')
extension_wp = os.getenv('EXTENSION_WP')
file_name_vc = os.getenv('FILE_NAME_VC')
extension_vc = os.getenv('EXTENSION_VC')

def validateFileNameVariables(file_name, extension):
    """ try:
        return True
    except ValueError as e:
        print(f"a variable is empty: file_name: {'EMPTY' if isEmpty(file_name) else file_name}, extension: {'EMPTY' if isEmpty(extension) else extension}") """
    if isEmpty(file_name) or isEmpty(extension):
        print(f"file_name {file_name}")
        print(f"extension {extension}")
        raise ValueError(f"a variable is empty: file_name: {'EMPTY' if isEmpty(file_name) else file_name}, extension: {'EMPTY' if isEmpty(extension) else extension}")

    return True


def getFileName(fileNameExpected = 'wp'):
            
    try:
        if (use_main_file and validateFileNameVariables(main_file_name, main_extension)):
            return main_file_name+'.'+main_extension
        
        else:
            fileNameExpected = fileNameExpected.lower()
            if(validateFileNameVariables(file_name_wp, extension_wp) and fileNameExpected == 'wp'):
                return file_name_wp+'.'+extension_wp
            else:
                return file_name_vc+'.'+extension_vc
    except ValueError as e:
        print(f'[bold red]{e}[/bold red]')
