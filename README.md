
# Peter Py

Various Small Utilities for Python for *ME*!

TODO README

See the [docs](docs/readme.md) for help

## Motivation
- Personal extensions to the Python REPL to allow it to be treated more like a shell
- Also various small scripts to go along with it
- Install by cloning this folder to some location on your local machine
- Write down the path of installation
- Then open and edit your terminal profile with an alias ([Linux](#linux)) ([Mac](#mac)) ([Windows Batch](#windows-batch)) ([Git for Windows](#git-for-windows)) ([PowerShell](#powershell))
- and then wherever you are working from the shell, just type `pp` to get an extended Python Shell
- I started this nonsense because I was tired of not having an easy way of clearing the screen
- So I added `c()` to do just that
- This is a lot of simple/small scripts
- it follows the `personal-py` framework (TODO: LINK)

## Opinions
- This is also meant to comprehensively replace a lot of my logging/journaling and metadata management systems
- I have a lot of opinions about metadata, but I am considerate enough to let you *configure* these options
- Be sure to set `config.py` with your choices or run `profile` from within the script
- If you have better ideas about how to manage configurations, I would love to hear about them! Create an issue for it.

## Terminal Profiles

### Linux
- Linux has a lot of different "prompts" or "shells", if you are using anything other than Bash than I expect you know what you are doing
- You can edit your profile at `~/.profile` by using any regular text editor
- you will want to add the following line to your profile:
```bash
alias pp="python3 -i $INSTALLPATH/peter-py/peterpy/__main__.py"
```
- where `$INSTALLPATH` is wherever you put peterpy
- You can rename the alias to whatever you want, I'd suggest the first letter of your name

### Mac
- TODO

### Windows Batch
- Windows Batch has no formal system for remembering user profiles
- Since `cmd` launches from `C:\Users\%USER%` by default, I simply put a "`profile.cmd`" there and remember to run it as the first thing I do when I open `cmd`
- You will want to add this line to it:
```batch
doskey pp=py -i %INSTALLPATH%\peter-py\peter_py\__main__.py
```
- Where `%INSTALLPATH%` is wherever you installed peterpy to
- You can rename the alias to whatever you want, I'd suggest the first letter of your name

### Git for Windows
- Git for Windows (TODO link) adds a thin Bash wrapper to Windows and includes a `profile` file at `C:\Users\%USER%\.bashrc`
- You will want to add this line to it:
```bash
alias pp="python3 -i $INSTALLPATH/peter-py/peterpy/__main__.py"
```
- where `$INSTALLPATH` is wherever you put peterpy
- You can rename the alias to whatever you want, I'd suggest the first letter of your name

### PowerShell
- PowerShell is a little bit weird
- TODO

