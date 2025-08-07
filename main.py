import os
import json
import readline
import getpass

def hex_to_ansi(hex_color: str) -> str:
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"\033[38;2;{r};{g};{b}m"

commands_dir = os.path.expanduser('~/.config/goose/cmd')
rc_dir = os.path.expanduser('~/iuirc')  #maybe
history = []

with open(os.path.expanduser('~/.config/goose/history'), 'r') as file:
    for line in file:
        readline.add_history(line.replace('\n', ''))

try:
    with open(os.path.expanduser('~/.config/goose/colors.json'), 'r') as file:
        colors = json.load(file)

        TERMINAL = hex_to_ansi(colors['terminal'])
        TEXT = hex_to_ansi(colors['text'])
        DIRECTORY = hex_to_ansi(colors['directory'])
        USER = hex_to_ansi(colors["user"])
except Exception as e:
    print(f"colors not loaded \nerror: {e}")
    TERMINAL = hex_to_ansi('#FFFFFF')
    TEXT = hex_to_ansi('#FFFFFF')
    DIRECTORY = hex_to_ansi('#FFFFFF')
    USER = hex_to_ansi('#FFFFFF')

def search_command_files(name):
    for folder in os.listdir(commands_dir):
        if folder == name:
            with open(f'{commands_dir}/{folder}/parametrs.json') as file:
                parametrs = json.load(file)
            with open(f'{commands_dir}/{folder}/settings.json') as file:
                settings = json.load(file)
            return parametrs, settings
    else:
        return 'not', None



def main():
    
    while True:

        current_dir = os.getcwd()
        username = getpass.getuser()


        user_command = input(f'{DIRECTORY}{"home" if current_dir.split('/')[-1] == username else current_dir.split('/')[-1]}{TERMINAL}@{USER}{username}{TERMINAL} ~> {TEXT}')

        with open(os.path.expanduser('~/.config/goose/history'), 'a') as file:
            file.write(f'{user_command}\n')

        history.append(user_command)


        if user_command == 'exit':
            break

        elif user_command.startswith('cd'):
            os.chdir(user_command.split(' ')[-1])

        elif user_command == 'commands':
            for file in os.listdir(commands_dir):
                print(file)
            
        
        elif user_command.startswith('start$'):
            parametrs, settings = search_command_files(user_command.split('$')[-1])
            if parametrs != 'not':
                try:
                    if settings['one_command']:
                        os.system(parametrs['command'])
                    else:
                        if settings['python']:
                            if parametrs['path'] != 'None':
                                os.chdir(os.path.expanduser(parametrs['path']))
                            if settings['venv']:
                                os.system(f'source {os.path.expanduser(parametrs["venv"])} && python3 {parametrs["file"]}')
                            else:
                                os.system(f'python3 {parametrs["file"]}')
                        elif settings['bash']:
                            if parametrs['path'] != 'None':
                                os.chdir(os.path.expanduser(parametrs['path']))
                            os.system(f'./{parametrs["file"]}')
                except Exception as e:
                    print(e)
            else:
                print("user command not found")
        else:
            os.system(user_command)
        
        





if __name__ == '__main__':
    main()
        
