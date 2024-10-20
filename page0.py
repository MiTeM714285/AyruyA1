import tkinter as tk

import page1
from main import entry
from switchFrame import switch_frame


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        img_title = tk.PhotoImage(file="image/title.png").subsample(2)
        img_logo = tk.PhotoImage(file="image/logo.png").subsample(2)
        tk.Label(self, text="AyruyA의 리듬공방", font=("Helvetica", 32, "bold")).pack(
            side="top", fill="x", pady=30
        )
        tk.Label(self, image=img_title).pack()

        tk.Label.image = img_title, img_logo
        tk.Label(self, text="이벤트 진행에 오신 것을 환영합니다.", font=("Helvetica", 24, "bold")).pack(
            side="top", fill="x", pady=30
        )
        tk.Button(
            self, text="시작하기", font=("Helvetica", 24, "bold"), command=lambda: switch_frame(master, page1.PageOne)
        ).pack()
        tk.Label(self, image=img_logo).pack(pady=25)

        # 초기 셋팅
        entry['agree'] = False
        entry['name'] = ''
        entry['phone'] = ''
        entry['email'] = ''
