import threading
import tkinter as tk
from tkinter import messagebox, ttk

from sleeper_gui.views.base_view import BaseView, _BG


class FollowView(BaseView):

    def _build(self):
        self._make_header(
            'Follow',
            'Follow users to keep their league data updated alongside yours.'
        )

        # ── Add user row ───────────────────────────────────────────────────
        add_frame = tk.Frame(self, bg=_BG, padx=32, pady=16)
        add_frame.pack(fill='x')

        tk.Label(add_frame, text='Username:', bg=_BG,
                 font=('Helvetica', 10)).pack(side='left')

        self._entry_var = tk.StringVar()
        ttk.Entry(add_frame, textvariable=self._entry_var, width=22).pack(
            side='left', padx=(8, 10))

        self._follow_btn = ttk.Button(add_frame, text='Follow',
                                      command=self._follow)
        self._follow_btn.pack(side='left')

        # ── Followed list + Unfollow button ───────────────────────────────
        list_frame = tk.Frame(self, bg=_BG, padx=32)
        list_frame.pack(fill='both', expand=True)

        self._listbox = tk.Listbox(list_frame, font=('Helvetica', 10),
                                   selectmode='single', activestyle='none',
                                   relief='flat', bd=1, highlightthickness=1,
                                   highlightcolor='#bdc3c7',
                                   highlightbackground='#bdc3c7')
        vsb = ttk.Scrollbar(list_frame, orient='vertical',
                             command=self._listbox.yview)
        self._listbox.configure(yscrollcommand=vsb.set)
        self._listbox.pack(side='left', fill='both', expand=True)
        vsb.pack(side='left', fill='y')

        btn_col = tk.Frame(list_frame, bg=_BG, padx=12)
        btn_col.pack(side='left', anchor='n', pady=4)
        self._unfollow_btn = ttk.Button(btn_col, text='Unfollow',
                                        state='disabled',
                                        command=self._unfollow)
        self._unfollow_btn.pack()

        self._listbox.bind('<<ListboxSelect>>', self._on_select)

        # ── Status ────────────────────────────────────────────────────────
        self._status_var, lbl = self._make_status_label()
        lbl.pack(fill='x', padx=32, pady=6)

    def on_show(self):
        self._refresh_list()

    # ── helpers ───────────────────────────────────────────────────────────

    def _refresh_list(self):
        self._listbox.delete(0, 'end')
        for username in self.sleeper.followed_users:
            self._listbox.insert('end', username)
        self._unfollow_btn.config(state='disabled')

    def _on_select(self, _event=None):
        has_selection = bool(self._listbox.curselection())
        self._unfollow_btn.config(state='normal' if has_selection else 'disabled')

    # ── actions ───────────────────────────────────────────────────────────

    def _follow(self):
        if not self.sleeper.db.initialized:
            messagebox.showwarning('Not initialized',
                                   'Run Initialize first.', parent=self)
            return
        username = self._entry_var.get().strip()
        if not username:
            messagebox.showwarning('Input required',
                                   'Enter a username.', parent=self)
            return
        if username in self.sleeper.followed_users:
            self._status_var.set(f'Already following "{username}".')
            return

        self._follow_btn.config(state='disabled')
        self._status_var.set(f'Downloading data for "{username}"\u2026')

        def run():
            try:
                self.sleeper.follow(username)
                self.after(0, lambda: self._on_follow_done(username))
            except Exception as exc:
                self.after(0, lambda: self._on_error(exc))

        threading.Thread(target=run, daemon=True).start()

    def _on_follow_done(self, username):
        self._follow_btn.config(state='normal')
        self._entry_var.set('')
        self._refresh_list()
        self._status_var.set(f'Now following "{username}".')

    def _unfollow(self):
        sel = self._listbox.curselection()
        if not sel:
            return
        username = self._listbox.get(sel[0])
        if not messagebox.askyesno('Unfollow',
                                   f'Unfollow "{username}"?\n\n'
                                   'Their downloaded data will be kept.',
                                   parent=self):
            return
        try:
            self.sleeper.unfollow(username)
            self._refresh_list()
            self._status_var.set(f'Unfollowed "{username}".')
        except Exception as exc:
            self._on_error(exc)

    def _on_error(self, exc):
        self._follow_btn.config(state='normal')
        msg = str(exc)
        self._status_var.set(f'Error: {msg}')
        messagebox.showerror('Error', msg, parent=self)
