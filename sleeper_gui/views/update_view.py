import threading
import tkinter as tk
from tkinter import messagebox, ttk

from sleeper_gui.views.base_view import BaseView, _BG


class UpdateView(BaseView):

    def _build(self):
        self._make_header(
            'Update Data',
            'Download the latest statistics and projections from Sleeper.'
        )

        body = tk.Frame(self, bg=_BG, padx=32, pady=24)
        body.pack(fill='x')

        tk.Label(body, text='Last updated:', bg=_BG,
                 font=('Helvetica', 11)).grid(row=0, column=0, sticky='w')

        self._last_var = tk.StringVar(value='\u2014')
        tk.Label(body, textvariable=self._last_var, bg=_BG,
                 font=('Helvetica', 11, 'bold'), fg='#1e2a3a').grid(
            row=0, column=1, padx=12, sticky='w')

        self._btn = ttk.Button(body, text='Update Now', command=self._start)
        self._btn.grid(row=1, column=0, columnspan=2, sticky='w', pady=16)

        self._progress = ttk.Progressbar(self, mode='indeterminate', length=340)
        self._status_var, lbl = self._make_status_label()
        lbl.pack(fill='x', padx=32, pady=4)

    def on_show(self):
        self._refresh_timestamp()

    # ── actions ───────────────────────────────────────────────────────────

    def _refresh_timestamp(self):
        try:
            dt = self.sleeper.last_download
            self._last_var.set(dt.strftime('%Y-%m-%d  %H:%M'))
        except Exception:
            self._last_var.set('Unknown')

    def _start(self):
        if not self.sleeper.db.initialized:
            messagebox.showwarning('Not initialized',
                                   'Run Initialize first.', parent=self)
            self.app.show_view('init')
            return

        username = self.sleeper.db.username
        self._btn.config(state='disabled')
        self._progress.pack(padx=32, pady=6, anchor='w')
        self._progress.start(12)
        self._status_var.set(
            f'Updating data for "{username}" \u2014 this may take a minute\u2026'
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
        self._status_var.set('Update complete!')
        self._refresh_timestamp()

    def _on_error(self, exc):
        self._progress.stop()
        self._progress.pack_forget()
        self._btn.config(state='normal')
        msg = str(exc)
        self._status_var.set(f'Error: {msg}')
        messagebox.showerror('Update failed', msg, parent=self)
