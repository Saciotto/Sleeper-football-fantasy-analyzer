import tkinter as tk
from tkinter import ttk

from sleeper_gui.views.base_view import BaseView, _BG


class LeaguesView(BaseView):

    def _build(self):
        self._make_header(
            'Leagues',
            'All leagues for the current user.'
        )

        table_frame = tk.Frame(self, bg=_BG, padx=32)
        table_frame.pack(fill='both', expand=True, pady=(16, 0))

        cols = ('name', 'league_id', 'season', 'total_rosters', 'status')
        self._tree = ttk.Treeview(table_frame, columns=cols, show='headings',
                                  selectmode='browse')
        vsb = ttk.Scrollbar(table_frame, orient='vertical',
                             command=self._tree.yview)
        self._tree.configure(yscrollcommand=vsb.set)

        for col, heading, width, anchor in [
            ('name',          'Name',         220, 'w'),
            ('league_id',     'League ID',    140, 'w'),
            ('season',        'Season',        70, 'center'),
            ('total_rosters', 'Teams',         60, 'center'),
            ('status',        'Status',        90, 'center'),
        ]:
            self._tree.heading(col, text=heading)
            self._tree.column(col, width=width, minwidth=40, anchor=anchor)

        self._tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        self._status_var, lbl = self._make_status_label()
        lbl.pack(fill='x', padx=32, pady=6)

    def on_show(self):
        if not self.sleeper.db.initialized:
            return
        try:
            leagues = self.sleeper.db.user_leagues
            self._tree.delete(*self._tree.get_children())
            for league in leagues:
                self._tree.insert('', 'end', values=(
                    league.get('name', ''),
                    league.get('league_id', ''),
                    league.get('season', ''),
                    league.get('total_rosters', ''),
                    league.get('status', ''),
                ))
            self._status_var.set(f'{len(leagues)} league(s).')
        except Exception as exc:
            self._status_var.set(f'Error: {exc}')
