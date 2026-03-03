import tkinter as tk
from tkinter import messagebox, ttk

from sleeper_gui.views.base_view import BaseView, _BG


class PlayersView(BaseView):

    def _build(self):
        self._make_header(
            'Players',
            "Players on a user's roster in the selected league."
        )

        ctrl = tk.Frame(self, bg=_BG, padx=32, pady=14)
        ctrl.pack(fill='x')

        tk.Label(ctrl, text='League:', bg=_BG,
                 font=('Helvetica', 10)).grid(row=0, column=0, sticky='w')
        self._league_var = tk.StringVar()
        self._league_combo = ttk.Combobox(ctrl, textvariable=self._league_var,
                                          width=26, state='readonly')
        self._league_combo.grid(row=0, column=1, padx=(6, 18))
        self._league_combo.bind('<<ComboboxSelected>>', self._on_league_selected)

        tk.Label(ctrl, text='User:', bg=_BG,
                 font=('Helvetica', 10)).grid(row=0, column=2, sticky='w')
        self._user_var = tk.StringVar()
        self._user_combo = ttk.Combobox(ctrl, textvariable=self._user_var,
                                        width=18, state='readonly')
        self._user_combo.grid(row=0, column=3, padx=(6, 18))

        self._load_btn = ttk.Button(ctrl, text='Load', command=self._load)
        self._load_btn.grid(row=0, column=4)

        table_frame = tk.Frame(self, bg=_BG, padx=32)
        table_frame.pack(fill='both', expand=True, pady=(4, 0))

        cols = ('name', 'position', 'age')
        self._tree = ttk.Treeview(table_frame, columns=cols, show='headings',
                                  selectmode='browse')
        vsb = ttk.Scrollbar(table_frame, orient='vertical',
                             command=self._tree.yview)
        self._tree.configure(yscrollcommand=vsb.set)

        for col, heading, width, anchor in [
            ('name',     'Name',      220, 'w'),
            ('position', 'Position',   90, 'center'),
            ('age',      'Age',        60, 'center'),
        ]:
            self._tree.heading(col, text=heading)
            self._tree.column(col, width=width, minwidth=40, anchor=anchor)

        self._tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        self._status_var, lbl = self._make_status_label()
        lbl.pack(fill='x', padx=32, pady=6)

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
        except Exception:
            pass

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
        except Exception:
            pass

    def _load(self):
        user = self._user_var.get().strip()
        league_name = self._league_var.get().strip()
        if not user or not league_name:
            messagebox.showwarning('Input required',
                                   'Please select both a user and a league.',
                                   parent=self)
            return
        league_id = self._league_map.get(league_name, league_name)
        try:
            team = self.sleeper.get_team(user, league_id)
            players = team.players
            self._tree.delete(*self._tree.get_children())
            for player in players:
                self._tree.insert('', 'end', values=(
                    player.name,
                    ','.join(player.fantasy_positions),
                    player.age,
                ))
            self._status_var.set(f'{len(players)} player(s).')
        except Exception as exc:
            msg = str(exc)
            self._status_var.set(f'Error: {msg}')
            messagebox.showerror('Error', msg, parent=self)
