import sys 
from pathlib import Path
from colorama import Fore,init

init(autoreset=True)

def show_directory(path,indent=""):
    p = Path(path)
    if not p.is_dir():
        print(f"{Fore.RED} Це не папка : {path}")
        return
    print(f"{Fore.YELLOW} {p.name}")
    for file in p.iterdir():
        if file.is_dir():
            show_directory(file,indent + " ")
        else:
            print(f"{Fore.GREEN}   {file.name}")
    
   
if len(sys.argv) < 2:
    print(f"{Fore.RED}Введіть корректний шлях")
    sys.exit(1)
directory = sys.argv[1]
show_directory(directory)
 
        
     