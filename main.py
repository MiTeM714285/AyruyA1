import tkinter as tk

import page0
from switchFrame import switch_frame

entry = {
    'agree': False,
    'name': '',
    'phone': '',
    'email': '',
    'gameAndKeymode': 'djmax-6',
    'level': 0,
    'musicname': '',
    'difficulty': '',
    'playstyle': '',
    'condition1': 0,
    'condition2': 0,
    'condition3': 0
}


class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("AyruyA의 리듬공방")
        self.geometry("1280x720")
        self.resizable(False, False)
        self._frame = None
        switch_frame(self, page0.StartPage)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
