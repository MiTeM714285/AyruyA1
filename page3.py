import tkinter as tk

import main
import page2
import page4
from switchFrame import switch_frame


class PageThree(tk.Frame):
    def __init__(self, master):

        def gameAndKeymode_rad():
            print(gameAndKeymode.get())
            main.entry['gameAndKeymode'] = gameAndKeymode.get()

        tk.Frame.__init__(self, master)
        tk.Label(self, text="게임 및 키모드 선택", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(30, 5)
        )

        img_djmax_4b = tk.PhotoImage(file="image/djmax-4.png").subsample(2)
        img_djmax_5b = tk.PhotoImage(file="image/djmax-5.png").subsample(2)
        img_djmax_6b = tk.PhotoImage(file="image/djmax-6.png").subsample(2)
        img_djmax_8b = tk.PhotoImage(file="image/djmax-8.png").subsample(2)
        img_ez2on_4b = tk.PhotoImage(file="image/ez2on-4.png").subsample(2)
        img_ez2on_5b = tk.PhotoImage(file="image/ez2on-5.png").subsample(2)
        img_ez2on_6b = tk.PhotoImage(file="image/ez2on-6.png").subsample(2)
        img_ez2on_8b = tk.PhotoImage(file="image/ez2on-8.png").subsample(2)

        gameAndKeymode = tk.StringVar()

        rad1 = tk.Radiobutton(self, image=img_djmax_4b, variable=gameAndKeymode, value="djmax-4", command=gameAndKeymode_rad)
        rad2 = tk.Radiobutton(self, image=img_djmax_5b, variable=gameAndKeymode, value="djmax-5", command=gameAndKeymode_rad)
        rad3 = tk.Radiobutton(self, image=img_djmax_6b, variable=gameAndKeymode, value="djmax-6", command=gameAndKeymode_rad)
        rad4 = tk.Radiobutton(self, image=img_djmax_8b, variable=gameAndKeymode, value="djmax-8", command=gameAndKeymode_rad)
        rad5 = tk.Radiobutton(self, image=img_ez2on_4b, variable=gameAndKeymode, value="ez2on-4", command=gameAndKeymode_rad)
        rad6 = tk.Radiobutton(self, image=img_ez2on_5b, variable=gameAndKeymode, value="ez2on-5", command=gameAndKeymode_rad)
        rad7 = tk.Radiobutton(self, image=img_ez2on_6b, variable=gameAndKeymode, value="ez2on-6", command=gameAndKeymode_rad)
        rad8 = tk.Radiobutton(self, image=img_ez2on_8b, variable=gameAndKeymode, value="ez2on-8", command=gameAndKeymode_rad)

        tk.Label.image = img_djmax_4b, img_djmax_5b, img_djmax_6b, img_djmax_8b, img_ez2on_4b, img_ez2on_5b, img_ez2on_6b, img_ez2on_8b



        rad1.pack()
        rad2.pack()
        rad3.pack()
        rad4.pack()
        rad5.pack()
        rad6.pack()
        rad7.pack()
        rad8.pack()

        tk.Label(self,
                 text="각 키모드별 아래와 같은 범위 내에서 레벨이 랜덤 배정됩니다.",
                 font=("Helvetica", 12, "bold")).pack(
            side="top", fill="x", pady=3
        )
        tk.Label(self,
                 text="DJMAX RESPECT V [4B MODE] : 5.1~14.3 (V-ARCHIVE 기준) / EZ2ON REBOOT:R [4B BASIC] : 12~19\n"
                      "DJMAX RESPECT V [5B MODE] : 3.1~12.3 (V-ARCHIVE 기준) / EZ2ON REBOOT:R [5B BASIC] : 11~18\n"
                      "DJMAX RESPECT V [6B MODE] : 3.1~12.3 (V-ARCHIVE 기준) / EZ2ON REBOOT:R [6B BASIC] : 11~18\n"
                      "DJMAX RESPECT V [8B MODE] : 1.1~9.3 (V-ARCHIVE 기준) / EZ2ON REBOOT:R [8B BASIC] : 9~16\n",
                 font=("Helvetica", 12, "normal")).pack(
            side="top", fill="x", pady=3
        )

        btn_back = tk.Button(self, text="뒤로", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page2.PageTwo))
        btn_next = tk.Button(self, text="다음", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page4.PageFour))
        btn_back.pack(side="left", padx=(280, 0))
        btn_next.pack(side="right", padx=(0, 280))

        # 초기 설정
        if main.entry['level'] != 0:
            rad1['state'] = tk.DISABLED
            rad2['state'] = tk.DISABLED
            rad3['state'] = tk.DISABLED
            rad4['state'] = tk.DISABLED
            rad5['state'] = tk.DISABLED
            rad6['state'] = tk.DISABLED
            rad7['state'] = tk.DISABLED
            rad8['state'] = tk.DISABLED

        if main.entry['gameAndKeymode'] == "djmax-4":
            rad1.select()
        elif main.entry['gameAndKeymode'] == "djmax-5":
            rad2.select()
        elif main.entry['gameAndKeymode'] == "djmax-6":
            rad3.select()
        elif main.entry['gameAndKeymode'] == "djmax-8":
            rad4.select()
        elif main.entry['gameAndKeymode'] == "ez2on-4":
            rad5.select()
        elif main.entry['gameAndKeymode'] == "ez2on-5":
            rad6.select()
        elif main.entry['gameAndKeymode'] == "ez2on-6":
            rad7.select()
        elif main.entry['gameAndKeymode'] == "ez2on-8":
            rad8.select()
