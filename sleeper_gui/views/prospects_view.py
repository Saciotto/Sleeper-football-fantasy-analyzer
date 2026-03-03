import threading
import tkinter as tk
from tkinter import messagebox, ttk

from sleeper_gui.views.base_view import BaseView, _BG

_ROLE_BG = '#d6eaf8'


class ProspectsView(BaseView):

    def _build(self):
        self._make_header(
            'Prospects',
            'Top 5 unowned players per roster slot, ranked by projected score.'
        )

        # ── Controls ──────────────────────────────────────────────────────
        ctrl = tk.Frame(self, bg=_BG, padx=32, pady=14)
        ctrl.pack(fill='x')

        tk.Label(ctrl, text='League:', bg=_BG,
                 font=('Helvetica', 10)).grid(row=0, column=0, sticky='w')
        self._league_var = tk.StringVar()
        self._league_combo = ttk.Combobox(ctrl, textvariable=self._league_var,
                                          width=26, state='readonly')
        self._league_combo.grid(row=0, column=1, padx=(6, 18))

        tk.Label(ctrl, text='Week:', bg=_BG,
                 font=('Helvetica', 10)).grid(row=0, column=2, sticky='w')
        self._week_var = tk.IntVar(value=1)
        ttk.Spinbox(ctrl, textvariable=self._week_var,
                    from_=1, to=18, width=5).grid(row=0, column=3, padx=(6, 18))

        self._load_btn = ttk.Button(ctrl, text='Load', command=self._load)
        self._load_btn.grid(row=0, column=4)

        # ── Tree ──────────────────────────────────────────────────────────
        table_frame = tk.Frame(self, bg=_BG, padx=32)
        table_frame.pack(fill='both', expand=True, pady=(4, 0))

        cols = ('position', 'projection')
        self._tree = ttk.Treeview(table_frame, columns=cols,
                                  show='tree headings', selectmode='browse')

        self._tree.heading('#0',         text='Role / Player')
        self._tree.heading('position',   text='Position')
        self._tree.heading('projection', text='Projected')

        self._tree.column('#0',         width=220, minwidth=120, stretch=True)
        self._tree.column('position',   width=90,  minwidth=60,  anchor='center', stretch=False)
        self._tree.column('projection', width=100, minwidth=60,  anchor='center', stretch=False)

        vsb = ttk.Scrollbar(table_frame, orient='vertical',
                             command=self._tree.yview)
        self._tree.configure(yscrollcommand=vsb.set)

        self._tree.tag_configure('role',   background=_ROLE_BG,
                                           font=('Helvetica', 10, 'bold'))
        self._tree.tag_configure('player', background='white')

        self._tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        # ── Status ────────────────────────────────────────────────────────
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
            self._week_var.set(self.sleeper.db.current_week)
        except Exception:
            pass

    # ── actions ───────────────────────────────────────────────────────────

    def _load(self):
        league_name = self._league_var.get().strip()
        if not league_name:
            messagebox.showwarning('Input required',
                                   'Please select a league.', parent=self)
            return
        league_id = self._league_map.get(league_name, league_name)
        week = self._week_var.get()
        self._load_btn.config(state='disabled')
        self._status_var.set('Searching prospects\u2026')
        self._tree.delete(*self._tree.get_children())

        def run():
            try:
                results = self.sleeper.get_prospects(league_id, week)
                self.after(0, lambda: self._populate(results))
            except Exception as exc:
                self.after(0, lambda: self._on_error(exc))

        threading.Thread(target=run, daemon=True).start()

    def _populate(self, results):
        self._load_btn.config(state='normal')
        self._tree.delete(*self._tree.get_children())

        if not results:
            self._status_var.set(
                'No prospects found — make sure other leagues are downloaded.')
            return

        total_players = 0
        for role, players in results.items():
            role_iid = self._tree.insert(
                '', 'end', text=role, open=True, tags=('role',))
            for rank, (player, score) in enumerate(players, start=1):
                pos = '/'.join(player.fantasy_positions) if player.fantasy_positions \
                      else player.position
                self._tree.insert(
                    role_iid, 'end',
                    text=f'  {rank}. {player.name}',
                    values=(pos, round(score, 2)),
                    tags=('player',),
                )
                total_players += 1

        self._status_var.set(
            f'{len(results)} role(s) — {total_players} prospect(s) found.')

    def _on_error(self, exc):
        self._load_btn.config(state='normal')
        msg = str(exc)
        self._status_var.set(f'Error: {msg}')
        messagebox.showerror('Error', msg, parent=self)
