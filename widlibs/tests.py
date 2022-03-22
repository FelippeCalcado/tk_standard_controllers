import tkinter as tk

import widgets as wid


def fn_tst():
    app = tk.Tk()
    frm = tk.Frame(app)
    frm.pack()

    def tst():
        print('This is a test')

    wid.CancelButton(frm, 'Botao de teste').build_show(tst)
    wid.OkButton(frm, 'Botao de teste').build_show(tst)

    app.mainloop()


if __name__ == '__main__':
    fn_tst()
