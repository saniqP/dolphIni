# dolphIni

## install
```
git clone https://github.com/saniqP/dolphIni.git
cd dolphIni
chmod +x makepkg
./makepkg
```
 restart terminal and enter command dolphIni

 ## commands

 all commands are on the ~/.config/DolpIni/Commands

## Parameters

Configuration is done via JSON in `~/.config/DolpIni/Commands/config.json`:

```json
{
  "only_command": boolean,    // If true, only runs the specified command
  "venv": "string",          // Path to Python virtual environment
  "path": "string",          // Path to project folder (containing main file)
  "main": "string",          // Path to main executable file
  "command": "string"        // Command to execute (only when only_command=true)
}
