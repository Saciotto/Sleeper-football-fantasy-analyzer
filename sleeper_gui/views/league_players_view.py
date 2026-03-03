import threading
import tkinter as tk
from tkinter import messagebox, ttk

from pandas import DataFrame

from sleeper_gui.views.base_view import BaseView, _BG


class LeaguePlayersView(BaseView):

    def _build(self):
        self._make_header(
            'League Players',
            'Weekly scoring for all players across the selected league.'
        )

        ctrl = tk.Frame(self, bg=_BG, padx=32, pady=14)
        ctrl.pack(fill='x')

        tk.Label(ctrl, text='League:', bg=_BG,
                 font=('Helvetica', 10)).grid(row=0, column=0, sticky='w')
        self._league_var = tk.StringVar()
        self._league_combo = ttk.Combobox(ctrl, textvariable=self._league_var,
                                          width=26, state='readonly')
        self._league_combo.grid(row=0, column=1, padx=(6, 18))

        self._load_btn = ttk.Button(ctrl, text='Load', command=self._load)
        self._load_btn.grid(row=0, column=2)

        table_frame = tk.Frame(self, bg=_BG, padx=32)
        table_frame.pack(fill='both', expand=True, pady=(4, 0))

        self._tree = ttk.Treeview(table_frame, show='headings',
                                  selectmode='browse')
        vsb = ttk.Scrollbar(table_frame, orient='vertical',
                             command=self._tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient='horizontal',
                             command=self._tree.xview)
        self._tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self._tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
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
        except Exception:
            pass

    def _load(self):
        league_name = self._league_var.get().strip()
        if not league_name:
            messagebox.showwarning('Input required',
                                   'Please select a league.',
                                   parent=self)
            return
        league_id = self._league_map.get(league_name, league_name)
        self._load_btn.config(state='disabled')
        self._status_var.set('Loading\u2026')

        def run():
            try:
                league = self.sleeper.get_league(league_id)
                data, columns = league.scoring(league.players)
                df = DataFrame(data, columns=columns)
                self.after(0, lambda: self._populate(df))
            except Exception as exc:
                self.after(0, lambda: self._on_error(exc))

        threading.Thread(target=run, daemon=True).start()

    def _populate(self, df):
        self._load_btn.config(state='normal')
        self._tree.delete(*self._tree.get_children())

        cols = list(df.columns)
        self._tree['columns'] = cols
        for col in cols:
            heading = col.replace('_', ' ').title()
            is_week = col.startswith('week')
            width = 64 if is_week else 120
            anchor = 'center' if is_week else 'w'
            self._tree.heading(col, text=heading,
                               command=lambda c=col: self._sort(c, False))
            self._tree.column(col, width=width, minwidth=40, anchor=anchor)

        for _, row in df.iterrows():
            values = [round(v, 2) if isinstance(v, float) else v for v in row]
            self._tree.insert('', 'end', values=values)

        self._status_var.set(f'{len(df)} player(s) loaded.')

    def _sort(self, col, reverse):
        rows = [(self._tree.set(c, col), c) for c in self._tree.get_children('')]
        try:
            rows.sort(key=lambda t: float(t[0]) if t[0] not in ('', 'nan') else -1,
                      reverse=reverse)
        except ValueError:
            rows.sort(reverse=reverse)
        for idx, (_, child) in enumerate(rows):
            self._tree.move(child, '', idx)
        self._tree.heading(col, command=lambda c=col: self._sort(c, not reverse))

    def _on_error(self, exc):
        self._load_btn.config(state='normal')
        msg = str(exc)
        self._status_var.set(f'Error: {msg}')
        messagebox.showerror('Error', msg, parent=self)
