
# PeterPy

Peter's Personal Python Shell

## A Personal Python Library
- What to call such?
- `pytools`? (taken)
- `peterpy`? (`peter-py`, `pypeter`, `py-peter`)
- github: `peter-py`
- local: `peter_py`
- https://github.com/peter201943/peter-py
- where to place locally? projects?
  - I'd like to be able to launch it easily from within python interpreter
  - so where to put it?
- perhaps I need to spend some time learning how to make a python cli app for windows...
- if publishing on pypi, do any similar libraries already exist?
- what to even call these things, "better repl"?
  - [this one is an app and not a library](https://github.com/prompt-toolkit/ptpython)
- example: "python repl clear screen", there are no results for any libraries that make this better/integral feature
- should probably clarify intent as well
- similar projects? ([pytools](https://github.com/inducer/pytools) has a similar layout that I like)
- huh, now I remember
  - Didn't I want to switch to Emacs for this exact reason?
  - Alas, ~~my memory really is bad~~ my *persistence* is bad, that was like 3 years ago when I got that plan in mind
- was almost tempted to call this `py-cheats` or `personal-py`
  - might talk about motivations inside the README for why it is the way it is
- misc
  - [Ptpython: A Better Python REPL](https://towardsdatascience.com/ptpython-a-better-python-repl-6e21df1eb648)
  - [3 Tools to Track and Visualize the Execution of your Python Code](https://towardsdatascience.com/3-tools-to-track-and-visualize-the-execution-of-your-python-code-666a153e435e)
- usage
  - would this be best as a CLI?
    - just call from batch/bash as `$ cd music && peterpy bcrename *`
      - need some way of registering `peterpy` as some command with the cli
        - alias?
          - so could modify `profile.bat` with a new `doskey peterpy=python -m peterpy`
            - does this support arguments?
              - suppose one writes `$ peterpy bcrename`
                - does `bcrename` get evaluated before `peterpy`?
        - as shortcut/batch script?
          - (have it just launch `python -m peterpy $ARGS`)
          - way to do this?
            - add shortcut to path?
              - does this appear as a `.lnk` file when calling?
            - add batch script?
              - does this appear as a `.bat` file when calling?
        - as system modification
          - win10: can use `ftype` and `assoc`
            - `ftype PythonScript=c:\pathtofolder\python.exe %*`
            - `assoc .py=PythonScript`
            - this allows invocation of a file via `project_dir> my_script.py arg1 arg2 arg3`
          - can then add the script to the Environment Variables
            - such as `c/utils/`
  - would this be best as a library?
    - after launching python repl, do `cd("music/"); cleanup.bcrename("*")`
- chosen solution
  - think I will just create an alias `doskey pp=python -m C:\Users\peter\projects\peter-py\peterpy\peterpy.py` (`pp` is "peter py")
    - where `peterpy.py` simply imports (`from _ import *`) from my other utilities

## Python CLI Publishing
- [x] [Deploy Python Command-Line Application](https://stackoverflow.com/questions/41453530/deploy-python-command-line-application)
- [x] [Distributing a Python command line application](https://gehrcke.de/2014/02/distributing-a-python-command-line-application/)
- [x] [Create Your First CLI Application With Python Click](https://betterprogramming.pub/python-click-building-your-first-command-line-interface-application-6947d5319ef7)
- [x] **[How to publish Python apps for human beings](https://gist.github.com/ForgottenUmbrella/ce6ecd8983e76f6d8ef47e07240eb4ac)**
- [x] **[Building Command-Line Applications with Python](https://dev.to/wangonya/building-command-line-applications-with-python-5l4)**
- [x] (WIN) **[Running python scripts on windows 10 cmd just by typing python nameofthescript.py](https://stackoverflow.com/questions/59832392/running-python-scripts-on-windows-10-cmd-just-by-typing-python-nameofthescript-p)**
- [x] [Build a Command-Line To-Do App With Python and Typer](https://realpython.com/python-typer-cli/)
- [x] (PSX) [how to run python script without typing 'python ...'](https://stackoverflow.com/questions/4993621/how-to-run-python-script-without-typing-python)
- [x] (PSX) [Run Python scripts without explicitly invoking `python`](https://superuser.com/questions/828737/run-python-scripts-without-explicitly-invoking-python)
- [ ] [How to create permanent PowerShell Aliases](https://stackoverflow.com/questions/24914589/how-to-create-permanent-powershell-aliases)

## Misc
- [x] [How to view profile on Linux](https://askubuntu.com/questions/886483/how-to-view-profile-on-linux)

## Call it "Personal Py"
- And let individual users set their name in `config.py`
- Therefore allow for a lot more personalization

## Disabling Metadata and Extensive Logging
- Not sure how to do this just yet
- Will need to consider later

