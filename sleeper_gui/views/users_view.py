import tkinter as tk
from tkinter import ttk

from sleeper_gui.views.base_view import BaseView, _BG


class UsersView(BaseView):

    def _build(self):
        self._make_header(
            'Users',
            'All users in the selected league.'
        )

        ctrl = tk.Frame(self, bg=_BG, padx=32, pady=14)
        ctrl.pack(fill='x')

        tk.Label(ctrl, text='League:', bg=_BG,
                 font=('Helvetica', 10)).grid(row=0, column=0, sticky='w')
        self._league_var = tk.StringVar()
        self._league_combo = ttk.Combobox(ctrl, textvariable=self._league_var,
                                          width=26, state='readonly')
        self._league_combo.grid(row=0, column=1, padx=(6, 0))
        self._league_combo.bind('<<ComboboxSelected>>', self._load)

        table_frame = tk.Frame(self, bg=_BG, padx=32)
        table_frame.pack(fill='both', expand=True, pady=(4, 0))

        cols = ('display_name', 'user_id')
        self._tree = ttk.Treeview(table_frame, columns=cols, show='headings',
                                  selectmode='browse')
        vsb = ttk.Scrollbar(table_frame, orient='vertical',
                             command=self._tree.yview)
        self._tree.configure(yscrollcommand=vsb.set)

        for col, heading, width, anchor in [
            ('display_name', 'Display Name', 200, 'w'),
            ('user_id',      'User ID',      160, 'w'),
        ]:
            self._tree.heading(col, text=heading)
            self._tree.column(col, width=width, minwidth=60, anchor=anchor)

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
            self._load()
        except Exception as exc:
            self._status_var.set(f'Error: {exc}')

    def _load(self, _event=None):
        league_name = self._league_var.get()
        league_id = self._league_map.get(league_name)
        if not league_id:
            return
        try:
            users = self.sleeper.db.get_league_users(league_id)
            self._tree.delete(*self._tree.get_children())
            for user in users:
                self._tree.insert('', 'end', values=(
                    user.get('display_name', ''),
                    user.get('user_id', ''),
                ))
            self._status_var.set(f'{len(users)} user(s).')
        except Exception as exc:
            self._status_var.set(f'Error: {exc}')
