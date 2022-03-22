import tkinter as tk

import widgets_data as wdt


class GenericButtons:
    font = wdt.WidgetsData.font_reg
    bg = 'white'

    def __init__(self, root, text):
        self.text = text
        self.root = root

    def build_show(self, comm):
        btn = tk.Button(self.root,
                        bg=self.bg,
                        relief='flat',
                        text=self.text,
                        font=self.font,
                        command=comm
                        )

        btn.pack()
        return btn


class OkButton(GenericButtons):
    bg = '#99ee99'


class CancelButton(GenericButtons):
    bg = '#ee9999'
