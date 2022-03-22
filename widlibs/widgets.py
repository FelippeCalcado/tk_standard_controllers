import tkinter as tk

import widlibs.widgets_data as wdt


class GenericButtons:
    font = wdt.WidgetsData.font_sml
    wid_data = wdt.WidgetsData()
    bg = wid_data.colors()['generic_buttons_background']
    fg = wid_data.colors()['light_btn_bg']

    def __init__(self, root, text):
        self.text = text
        self.root = root

    def build_show(self, comm):

        btn = tk.Button(self.root,
                        bg=self.bg,
                        relief='flat',
                        text=self.text,
                        font=self.font,
                        fg=self.fg,
                        command=comm
                        )

        btn.pack(fill='x')
        return btn


class OkButton(GenericButtons):
    bg = '#99ee99'
    fg = 'black'


class CancelButton(GenericButtons):
    bg = '#ee9999'
    fg = 'black'
