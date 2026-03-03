import tkinter as tk
from tkinter import ttk

from sleeper_gui.views.init_view import InitView
from sleeper_gui.views.lineup_view import LineupView
from sleeper_gui.views.settings_view import SettingsView
from sleeper_gui.views.team_view import TeamView
from sleeper_gui.views.update_view import UpdateView

# ── Sidebar colour palette ────────────────────────────────────────────────────
_SB_BG = '#1e2a3a'        # sidebar background
_SB_ACTIVE = '#2ecc71'    # highlighted nav button
_SB_FG = '#ecf0f1'        # normal nav text
_SB_FG_DIM = '#4a6177'    # disabled nav text
_CONTENT_BG = '#f4f6f9'   # main content area

# ── Navigation definition ─────────────────────────────────────────────────────
# Each entry: (label, view_key, implemented)  |  None = separator
_NAV = [
    ('Initialize',     'init',           True),
    ('Update Data',    'update',         True),
    ('Settings',       'settings',       True),
    None,
    ('Team',           'team',           True),
    ('Lineup',         'lineup',         True),
    None,
    ('Leagues',        'leagues',        False),
    ('Players',        'players',        False),
    ('Users',          'users',          False),
    ('League Players', 'league_players', False),
]

_VIEW_CLASSES = {
    'init':     InitView,
    'update':   UpdateView,
    'settings': SettingsView,
    'team':     TeamView,
    'lineup':   LineupView,
}


class App(tk.Tk):

    def __init__(self, sleeper):
        super().__init__()
        self.sleeper = sleeper
        self.title('Sleeper Fantasy Analyzer')
        self.geometry('1100x680')
        self.minsize(860, 520)

        self._nav_buttons: dict[str, tk.Button] = {}
        self.views: dict[str, tk.Frame] = {}

        self._build_layout()
        self._create_views()
        self._build_nav()
        self._open_initial_view()

    # ── layout ────────────────────────────────────────────────────────────────

    def _build_layout(self):
        # Sidebar
        self.sidebar = tk.Frame(self, bg=_SB_BG, width=200)
        self.sidebar.pack(side='left', fill='y')
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar, text='Sleeper\nAnalyzer',
            bg=_SB_BG, fg='white',
            font=('Helvetica', 15, 'bold'), pady=24
        ).pack(fill='x')

        ttk.Separator(self.sidebar).pack(fill='x', padx=16, pady=4)

        self._nav_frame = tk.Frame(self.sidebar, bg=_SB_BG)
        self._nav_frame.pack(fill='both', expand=True, pady=8)

        # Content area
        content_outer = tk.Frame(self, bg=_CONTENT_BG)
        content_outer.pack(side='right', fill='both', expand=True)

        # Status bar (bottom strip)
        self.status_var = tk.StringVar(value='Ready')
        status_bar = tk.Frame(content_outer, bg='#dde1e7', height=24)
        status_bar.pack(side='bottom', fill='x')
        status_bar.pack_propagate(False)
        tk.Label(
            status_bar, textvariable=self.status_var,
            bg='#dde1e7', fg='#444', anchor='w', padx=12,
            font=('Helvetica', 9)
        ).pack(side='left', fill='y')

        # View container (all view frames stack here)
        self.view_container = tk.Frame(content_outer, bg=_CONTENT_BG)
        self.view_container.pack(fill='both', expand=True)

    # ── views ─────────────────────────────────────────────────────────────────

    def _create_views(self):
        for key, cls in _VIEW_CLASSES.items():
            view = cls(self.view_container, self)
            view.place(relwidth=1, relheight=1)
            self.views[key] = view

    # ── navigation ────────────────────────────────────────────────────────────

    def _build_nav(self):
        btn_cfg = dict(bg=_SB_BG, bd=0, padx=20, pady=9,
                       anchor='w', font=('Helvetica', 10))

        for item in _NAV:
            if item is None:
                ttk.Separator(self._nav_frame).pack(
                    fill='x', padx=16, pady=6)
                continue

            label, key, implemented = item
            if implemented:
                btn = tk.Button(
                    self._nav_frame, text=label,
                    fg=_SB_FG,
                    activebackground='#2c3e50', activeforeground='white',
                    cursor='hand2',
                    command=lambda k=key: self.show_view(k),
                    **btn_cfg
                )
                self._nav_buttons[key] = btn
            else:
                btn = tk.Button(
                    self._nav_frame, text=label,
                    fg=_SB_FG_DIM,
                    disabledforeground=_SB_FG_DIM,
                    activebackground=_SB_BG,
                    state='disabled',
                    font=('Helvetica', 10, 'italic'),
                    bg=_SB_BG, bd=0, padx=20, pady=9, anchor='w'
                )
            btn.pack(fill='x')

    def show_view(self, key: str):
        if key not in self.views:
            return
        self.views[key].tkraise()
        for k, btn in self._nav_buttons.items():
            btn.config(
                bg=_SB_ACTIVE if k == key else _SB_BG,
                fg='white'
            )
        self.views[key].on_show()

    # ── helpers ───────────────────────────────────────────────────────────────

    def set_status(self, msg: str):
        self.status_var.set(msg)
        self.update_idletasks()

    def reload_sleeper(self):
        """Recreate the Sleeper instance so all views see the refreshed data."""
        from sleeper_analyzer.sleeper import Sleeper
        self.sleeper = Sleeper()
        for view in self.views.values():
            view.sleeper = self.sleeper

    def _open_initial_view(self):
        if self.sleeper.db.initialized:
            self.show_view('team')
        else:
            self.show_view('init')
