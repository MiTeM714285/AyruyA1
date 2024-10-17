import tkinter as tk

import page2
import page4


class PageThree(tk.Frame):
    def __init__(self, master):

        def gameAndKeymode_rad():
            if gameAndKeymode.get() == 0:
                print("0")
            elif gameAndKeymode.get() == 1:
                print("1")
            elif gameAndKeymode.get() == 2:
                print("2")
            elif gameAndKeymode.get() == 3:
                print("3")
            elif gameAndKeymode.get() == 4:
                print("4")
            elif gameAndKeymode.get() == 5:
                print("5")
            elif gameAndKeymode.get() == 6:
                print("6")
            elif gameAndKeymode.get() == 7:
                print("7")

        tk.Frame.__init__(self, master)
        tk.Label(self, text="게임 및 키모드 선택", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(30, 5)
        )

        img_djmax_4b = tk.PhotoImage(file="image/djmax_4b.png").subsample(2)
        img_djmax_5b = tk.PhotoImage(file="image/djmax_5b.png").subsample(2)
        img_djmax_6b = tk.PhotoImage(file="image/djmax_6b.png").subsample(2)
        img_djmax_8b = tk.PhotoImage(file="image/djmax_8b.png").subsample(2)
        img_ez2on_4b = tk.PhotoImage(file="image/ez2on_4b.png").subsample(2)
        img_ez2on_5b = tk.PhotoImage(file="image/ez2on_5b.png").subsample(2)
        img_ez2on_6b = tk.PhotoImage(file="image/ez2on_6b.png").subsample(2)
        img_ez2on_8b = tk.PhotoImage(file="image/ez2on_8b.png").subsample(2)

        gameAndKeymode = tk.IntVar()

        rad1 = tk.Radiobutton(self, image=img_djmax_4b, variable=gameAndKeymode, value=0,
                              command=gameAndKeymode_rad)
        rad2 = tk.Radiobutton(self, image=img_djmax_5b, variable=gameAndKeymode, value=1,
                              command=gameAndKeymode_rad)
        rad3 = tk.Radiobutton(self, image=img_djmax_6b, variable=gameAndKeymode, value=2,
                              command=gameAndKeymode_rad)
        rad4 = tk.Radiobutton(self, image=img_djmax_8b, variable=gameAndKeymode, value=3,
                              command=gameAndKeymode_rad)
        rad5 = tk.Radiobutton(self, image=img_ez2on_4b, variable=gameAndKeymode, value=4,
                              command=gameAndKeymode_rad)
        rad6 = tk.Radiobutton(self, image=img_ez2on_5b, variable=gameAndKeymode, value=5,
                              command=gameAndKeymode_rad)
        rad7 = tk.Radiobutton(self, image=img_ez2on_6b, variable=gameAndKeymode, value=6,
                              command=gameAndKeymode_rad)
        rad8 = tk.Radiobutton(self, image=img_ez2on_8b, variable=gameAndKeymode, value=7,
                              command=gameAndKeymode_rad)

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
                             command=lambda: master.switch_frame(page2.PageTwo))
        btn_next = tk.Button(self, text="다음", font=("Helvetica", 20, "bold"),
                             command=lambda: master.switch_frame(page4.PageFour))
        btn_back.pack(side="left", padx=(280, 0))
        btn_next.pack(side="right", padx=(0, 280))