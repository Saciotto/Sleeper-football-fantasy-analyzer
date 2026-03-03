import tkinter as tk
from tkinter import messagebox, ttk

from sleeper_gui.views.base_view import BaseView, _BG


class SettingsView(BaseView):

    def _build(self):
        self._make_header(
            'Settings',
            'Configure the default user and league used by analysis commands.'
        )

        body = tk.Frame(self, bg=_BG, padx=32, pady=24)
        body.pack(fill='x')

        # ── Default user ──────────────────────────────────────────────────
        tk.Label(body, text='Default user:', bg=_BG,
                 font=('Helvetica', 11)).grid(row=0, column=0, sticky='w', pady=8)

        self._user_var = tk.StringVar()
        self._user_combo = ttk.Combobox(body, textvariable=self._user_var,
                                        width=24, state='readonly')
        self._user_combo.grid(row=0, column=1, padx=12, pady=8)

        ttk.Button(body, text='Set User', command=self._set_user).grid(
            row=0, column=2, padx=4)

        # ── Default league ────────────────────────────────────────────────
        tk.Label(body, text='Default league:', bg=_BG,
                 font=('Helvetica', 11)).grid(row=1, column=0, sticky='w', pady=8)

        self._league_var = tk.StringVar()
        self._league_combo = ttk.Combobox(body, textvariable=self._league_var,
                                          width=24, state='readonly')
        self._league_combo.grid(row=1, column=1, padx=12, pady=8)
        self._league_combo.bind('<<ComboboxSelected>>', self._on_league_selected)

        ttk.Button(body, text='Set League', command=self._set_league).grid(
            row=1, column=2, padx=4)

        # ── Status ────────────────────────────────────────────────────────
        self._status_var, lbl = self._make_status_label(body)
        lbl.grid(row=2, column=0, columnspan=3, sticky='w', pady=(8, 0))

        # Internal: league display name → league_id
        self._league_map = {}

    def on_show(self):
        if not self.sleeper.db.initialized:
            return
        try:
            leagues = self.sleeper.db.user_leagues
            self._league_map = {
                l.get('name', l['league_id']): l['league_id']
                for l in leagues
            }
            self._league_combo['values'] = list(self._league_map.keys())
            current_id = self.sleeper.default_league
            for name, lid in self._league_map.items():
                if lid == current_id:
                    self._league_var.set(name)
                    break
            self._user_var.set(self.sleeper.default_user or '')
            self._on_league_selected()
        except Exception as exc:
            self._status_var.set(f'Error loading settings: {exc}')

    def _on_league_selected(self, _event=None):
        league_name = self._league_var.get()
        league_id = self._league_map.get(league_name)
        if not league_id:
            return
        try:
            users = self.sleeper.db.get_league_users(league_id)
            names = [u.get('display_name', u['user_id']) for u in users]
            self._user_combo['values'] = names
            names_ci = {n.lower(): n for n in names}
            current = self._user_var.get()
            if current.lower() in names_ci:
                self._user_var.set(names_ci[current.lower()])
                return
            default = self.sleeper.default_user or ''
            if default.lower() in names_ci:
                self._user_var.set(names_ci[default.lower()])
            elif names:
                self._user_var.set(names[0])
        except Exception as exc:
            self._status_var.set(f'Error loading users: {exc}')

    # ── actions ───────────────────────────────────────────────────────────

    def _set_user(self):
        user = self._user_var.get().strip()
        if not user:
            messagebox.showwarning('Input required',
                                   'Enter a username.', parent=self)
            return
        try:
            self.sleeper.default_user = user
            self._status_var.set(f'Default user set to "{user}".')
        except Exception as exc:
            messagebox.showerror('Error', str(exc), parent=self)

    def _set_league(self):
        name = self._league_var.get().strip()
        if not name:
            messagebox.showwarning('Input required',
                                   'Select a league.', parent=self)
            return
        league_id = self._league_map.get(name, name)
        try:
            self.sleeper.default_league = league_id
            self._status_var.set(f'Default league set to "{name}".')
        except Exception as exc:
            messagebox.showerror('Error', str(exc), parent=self)
