# dolphIni

## install
```bash
git clone https://github.com/saniqP/gooseTerm.git
cd gooseTerm
chmod +x makepkg
./makepkg
```
 restart terminal and enter command goose

 ## commands

 to create a command you need to create a directory with the name of the command in ~/.config/goose/cmd/ and in your directory create parametrs.json and settings.json

## Parameters

`~/.config/DolpIni/Commands/example/parametrs.json`:

```json
{
    "path": "string или null — путь к файлу или директории (None означает отсутствие пути)",
    "file": "string — имя файла (например, 'g.sh' — скрипт Bash)",
    "venv": "string — путь к виртуальному окружению Python (если используется)",
    "command": "string — команда, которую нужно выполнить"
}
```

`~/.config/DolpIni/Commands/example/settings.json`:

```json
{
    "python": "boolean — включает/отключает поддержку Python в скрипте",
    "bash": "boolean — включает/отключает поддержку Bash в скрипте",
    "venv": "boolean — указывает, нужно ли использовать виртуальное окружение Python (если включено)",
    "one_command": "boolean — определяет, должен ли скрипт выполнять только одну команду (true) или несколько (false)"
}
```
