# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Install (development mode):**
```bash
pip install -e .
```

**Run all tests:**
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**Run a single test:**
```bash
# Single module
python -m unittest tests.test_sleeper_db -v

# Single class
python -m unittest tests.test_sleeper_db.TestSleeperDatabase -v

# Single method
python -m unittest tests.test_sleeper_db.TestSleeperDatabase.test_nfl_state -v
```

**Linting:**
```bash
flake8 --max-line-length=120
```

**Run the CLI (after install):**
```bash
sleeper init <username>   # First-time setup
sleeper update            # Fetch latest data from Sleeper API
sleeper team              # Show team stats
sleeper lineup            # Show best projected lineup
```

**Run the GUI (after install):**
```bash
sleeper-gui
```

## Architecture

The project is a Python CLI/GUI tool that fetches and analyzes Sleeper fantasy football data. It has two top-level packages:

- **`sleeper_analyzer/`** — Core business logic, data access, models
- **`sleeper_cli/`** — Argparse-based CLI commands that call into `sleeper_analyzer`
- **`sleeper_gui/`** — tkinter GUI that wraps the same `Sleeper` facade

### Layer Diagram

```
sleeper_cli (CLI commands via argparse)
    └── sleeper_analyzer/sleeper.py  (Facade — main entry point for CLI)
            ├── SleeperDatabase      (Loads/queries local JSON files)
            ├── Config               (JSON-backed config at ~/Sleeper/config.json)
            ├── downloader.py        (Fetches from Sleeper API, writes to disk)
            └── models/              (league.py, team.py, player.py, user.py)
```

### Data Flow

All external data is fetched via `sleeper_analyzer/sleeper_api.py` (pure urllib HTTP client calling `https://api.sleeper.app/v1/`) and cached to the local filesystem at `~/Sleeper/` as JSON. `SleeperDatabase` reads from that cache. No SQL database is involved.

Key path constants live in `sleeper_analyzer/files.py`. The `SLEEPER_HOME` root is `Path.home() / 'Sleeper'`.

### Models

`Player`, `User`, and `League` all extend `dict` and are populated from the cached JSON. `Player` lazy-loads statistics/projections from the database on first access. `Team` contains scoring and best-lineup logic.

### Entry Points

`sleeper_cli/__main__.py:console_entry` is the `sleeper` console script. It checks whether the database is initialized and either runs `initialize()` (first run) or `main()` (normal operation).

`sleeper_gui/__main__.py:console_entry` is the `sleeper-gui` console script. `App(tk.Tk)` in `app.py` owns a shared `Sleeper` instance; each view is a `tk.Frame` subclass of `BaseView` stacked in the content area and raised via `tkraise()`. Long-running operations (download) run in daemon threads; all UI updates go through `self.after(0, callback)`. `app.reload_sleeper()` recreates the `Sleeper` instance and propagates it to all views after a successful init/update. To add a new view: create `sleeper_gui/views/<name>_view.py`, extend `BaseView`, then register it in `_NAV` and `_VIEW_CLASSES` in `app.py`.

### Testing

Tests use Python's `unittest` with no external test runner. `tests/mock_requests.py` patches `urllib.request.urlopen` and routes calls to fixture files in `tests/data/` to avoid real API calls. `tests/mock_files.py` contains path constants for those fixtures.
