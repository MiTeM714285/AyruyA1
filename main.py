import threading
import tkinter as tk

import keyboard
import tkinter.messagebox as msgbox
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

def exit_window():
    str = msgbox.askokcancel("알림", "프로그램을 종료하시겠습니까?")
    if str:
        app.destroy()
def start_keyboard_listener():
    keyboard.add_hotkey("alt+tab",on_key_event)
    keyboard.wait()  #

def on_key_event():
    app.iconify()

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
    app.attributes('-topmost', True)
    app.protocol('WM_DELETE_WINDOW', exit_window)
    app.iconbitmap('image/icon.ico')
    listener_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
    listener_thread.start()
    app.mainloop()
