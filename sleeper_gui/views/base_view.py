import tkinter as tk
from tkinter import ttk

_BG = '#f4f6f9'
_HEADER_FG = '#1e2a3a'
_SUB_FG = '#7f8c8d'


class BaseView(tk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, bg=_BG)
        self.app = app
        self.sleeper = app.sleeper
        self._build()

    def _build(self):
        """Build UI widgets. Override in subclasses."""

    def on_show(self):
        """Called each time this view is raised. Override to refresh data."""

    # ── layout helpers ────────────────────────────────────────────────────

    def _make_header(self, title, subtitle=None):
        header = tk.Frame(self, bg=_BG, padx=32, pady=22)
        header.pack(fill='x')
        tk.Label(
            header, text=title, bg=_BG, fg=_HEADER_FG,
            font=('Helvetica', 18, 'bold')
        ).pack(anchor='w')
        if subtitle:
            tk.Label(
                header, text=subtitle, bg=_BG, fg=_SUB_FG,
                font=('Helvetica', 10)
            ).pack(anchor='w', pady=(2, 0))
        ttk.Separator(self).pack(fill='x', padx=32)
        return header

    def _make_status_label(self, parent=None, **grid_or_pack_kwargs):
        parent = parent or self
        var = tk.StringVar()
        lbl = tk.Label(
            parent, textvariable=var, bg=_BG,
            fg='#7f8c8d', font=('Helvetica', 9)
        )
        return var, lbl
