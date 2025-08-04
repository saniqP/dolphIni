import os
import sys
import json


commands_dir = os.path.expanduser('~/.config/DolphIni/Commands')

def search_project(name):
   for file in os.listdir(commands_dir):
        file_name = file.split('.')
        if file_name[1] == 'json' and file_name[0] == name:
            with open(f'{commands_dir}/{file}', 'r') as f:
                json_file = json.load(f)
                if not json_file["only_command"]:
                    return json_file["main"], json_file["venv"], os.path.expanduser(json_file["path"])
                if json_file["only_command"] == True:
                    return json_file["command"], None, None
                break
   else:
        return "echo 'command not found'", None, None
                
def hex_to_ansi(hex_color: str) -> str:
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"\033[38;2;{r};{g};{b}m"


def main():

    run = True

    while run:
        user_command = input(f"{hex_to_ansi("#6394DC")}byDolphin$~>{hex_to_ansi("#55C33F")}")

        if user_command == 'exit':
            run = False
        elif user_command == 'ls':
            for file in os.listdir(commands_dir):
                print(f'{hex_to_ansi('#7555AB')}{file.split('.')[0]}{hex_to_ansi('#D739B2')}.json')

        else:
            main_file, venv_path, path = search_project(user_command)
            if main_file != None and venv_path != None and path != None:
                os.chdir(path)
                os.system(f'source {venv_path} && python3 {main_file}')
            else:
                os.system(main_file)

if __name__ == '__main__':
    main()
        





