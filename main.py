from page0 import StartPage
import tkinter as tk



class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("AyruyA의 리듬공방")
        self.geometry("1280x720")
        self.resizable(False,False)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()