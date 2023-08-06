# Pypertext

Pypertext is a framework to rapidly build data apps with Python. It's built on top of FastAPI and HTMX. With Pypertext, you can create interactive web apps using only Python. Your data, state, and UI are tightly coupled.

- [Documentation](https://pypertext.com)
- [Github repo](https://github.com/asifr/pypertext)

## Install

**Prerequisite**: Pypertext requires Python 3.8 or higher.

```
pip install pypertext
```

## Getting started

Create a new file called `app.py` and add the following code:

```python
from pypertext import ht, create_app

app = create_app()
app.ui(ht.H1("Hello world!"))
```

Run your script from the command line using the `pypertext` command:

```
pypertext app.py
```

You should see the following output:

```
 __       __   ___  __  ___  ___     ___ 
|__) \ / |__) |__  |__)  |  |__  \_/  |  
|     |  |    |___ |  \  |  |___ / \  |  


           Server settings           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Name      ┃ Setting               ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Host      │ http://127.0.0.1:8700 │
│ Workers   │ 1                     │
│ Log Level │ warning               │
│ App       │ app:app               │
└───────────┴───────────────────────┘
```

Open your browser and navigate to [http://127.0.0.1:8700](http://127.0.0.1:8700) to see your app.

Pypertext detected the `app` variable (a FastAPI application), started a web server in development mode, and rendered the app's UI. You can now make changes to your app and see them reflected in your browser.

Make a change to your `app.py` script and save it. You should see the following output:

```
WARNING:  WatchFiles detected changes in 'app.py'. Reloading...
```

What just happened? Pypertext detected that you made a change to your `app.py` script and automatically reloaded the app. Refresh your browser to see the change.

## `pypertext` command

`pypertext --help` shows all the available options:

```
 Usage: pypertext [OPTIONS] FILE

 Start a Pypertext web server

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    file      PATH  [default: None] [required]                              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --app                                  TEXT     [default: app]               │
│ --open-browser    --no-open-browser             [default: no-open-browser]   │
│ --reload          --no-reload                   [default: reload]            │
│ --host                                 TEXT     [default: 127.0.0.1]         │
│ --port                                 INTEGER  [default: 8700]              │
│ --workers                              INTEGER  [default: 1]                 │
│ --log-level                            TEXT     [default: warning]           │
│ --help                                          Show this message and exit.  │
╰──────────────────────────────────────────────────────────────────────────────╯
```

- `--app` - The name of the app variable in your script. Defaults to `app`. This is an instance of a FastAPI application created using `create_app()`.
- `--open-browser` - Open the app in your browser.
- `--reload` - Automatically reload the app when you make changes to your script. This is useful for development. By default, the app is reloaded when you make changes to your script. You can disable this behavior by passing `--no-reload`.
- `--host` - The host web address to use. Defaults to `127.0.0.1`
- `--port` - The port to use. Defaults to `8700`
- `--workers` - The number of workers to use. Defaults to `1` worker. You can increase this number to improve performance in production. Keep it at `1` for development.
- `--log-level` - The log level to use for Uvicorn. Defaults to `warning`. You can set this to `debug` to see more detailed logs.
