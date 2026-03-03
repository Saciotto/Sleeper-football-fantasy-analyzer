import threading
import tkinter as tk
from tkinter import messagebox, ttk

from sleeper_gui.views.base_view import BaseView, _BG


class InitView(BaseView):

    def _build(self):
        self._make_header(
            'Initialize',
            'Connect Sleeper Fantasy Analyzer to your Sleeper account.'
        )

        body = tk.Frame(self, bg=_BG, padx=32, pady=28)
        body.pack(fill='x')

        tk.Label(body, text='Sleeper username:', bg=_BG,
                 font=('Helvetica', 11)).grid(row=0, column=0, sticky='w')

        self._username_var = tk.StringVar()
        self._entry = ttk.Entry(body, textvariable=self._username_var,
                                width=28, font=('Helvetica', 11))
        self._entry.grid(row=0, column=1, padx=12, pady=4)
        self._entry.bind('<Return>', lambda _e: self._start())
        self._entry.focus_set()

        self._btn = ttk.Button(body, text='Initialize', command=self._start)
        self._btn.grid(row=1, column=1, sticky='w', padx=12, pady=10)

        self._progress = ttk.Progressbar(self, mode='indeterminate', length=340)
        self._status_var, lbl = self._make_status_label(padx=32, anchor='w')
        lbl.pack(fill='x', padx=32, pady=4)

    # ── actions ───────────────────────────────────────────────────────────

    def _start(self):
        username = self._username_var.get().strip()
        if not username:
            messagebox.showwarning('Username required',
                                   'Please enter your Sleeper username.',
                                   parent=self)
            return

        self._btn.config(state='disabled')
        self._progress.pack(padx=32, pady=6, anchor='w')
        self._progress.start(12)
        self._status_var.set(
            f'Downloading data for "{username}" \u2014 this may take a minute\u2026'
        )

        def run():
            try:
                self.sleeper.download(username)
                self.after(0, self._on_success)
            except Exception as exc:
                self.after(0, lambda: self._on_error(exc))

        threading.Thread(target=run, daemon=True).start()

    def _on_success(self):
        self._progress.stop()
        self._progress.pack_forget()
        self._btn.config(state='normal')
        self._status_var.set('Initialization complete!')
        self.app.set_status('Ready')
        self.app.reload_sleeper()
        self.app.show_view('team')

    def _on_error(self, exc):
        self._progress.stop()
        self._progress.pack_forget()
        self._btn.config(state='normal')
        msg = str(exc)
        self._status_var.set(f'Error: {msg}')
        messagebox.showerror('Initialization failed', msg, parent=self)
