import tkinter as tk

import main
import page1
import page3
from switchFrame import switch_frame


class PageFour(tk.Frame):
    def __init__(self, master):
        global levelBoundary
        tk.Frame.__init__(self, master)

        if main.entry['gameAndKeymode'] == 'djmax-4':
            levelBoundary = "레벨 추첨 범위는 5.X ~ 14.X (V-ARCHIVE 기준) 입니다."
        elif main.entry['gameAndKeymode'] == 'djmax-5':
            levelBoundary = "레벨 추첨 범위는 3.X ~ 12.X (V-ARCHIVE 기준) 입니다."
        elif main.entry['gameAndKeymode'] == 'djmax-6':
            levelBoundary = "레벨 추첨 범위는 3.X ~ 12.X (V-ARCHIVE 기준) 입니다."
        elif main.entry['gameAndKeymode'] == 'djmax-8':
            levelBoundary = "레벨 추첨 범위는 1.X ~ 9.X (V-ARCHIVE 기준) 입니다."
        elif main.entry['gameAndKeymode'] == 'ez2on-4':
            levelBoundary = "레벨 추첨 범위는 12 ~ 19 입니다."
        elif main.entry['gameAndKeymode'] == 'ez2on-5':
            levelBoundary = "레벨 추첨 범위는 11 ~ 18 입니다."
        elif main.entry['gameAndKeymode'] == 'ez2on-6':
            levelBoundary = "레벨 추첨 범위는 11 ~ 18 입니다."
        elif main.entry['gameAndKeymode'] == 'ez2on-8':
            levelBoundary = "레벨 추첨 범위는 9 ~ 16 입니다."

        # tk.Frame.configure(self, bg="red")
        fileUrl = "image/" + main.entry['gameAndKeymode'] + ".png"
        img_gameAndKeymode = tk.PhotoImage(file=fileUrl).subsample(2)
        tk.Label(self, image=img_gameAndKeymode).pack(side="top", pady=30)
        tk.Label.image = img_gameAndKeymode

        tk.Label(self, text="레벨 랜덤 추첨 결정", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(30, 5)
        )
        tk.Label(self,
                 text=levelBoundary,
                 font=("Helvetica", 16, "bold")).pack(
            side="top", fill="x", pady=20
        )

        tk.Label(self,
                 text="주의:추첨 시작 버튼은 한 번만 유효하며, 다시는 되돌이킬 수 없습니다.",
                 font=("Helvetica", 18, "bold"), fg="red").pack(
            side="top", fill="x", pady=30
        )

        tk.Label(self, text="결과:", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=20
        )

        tk.Button(
            self, text="추첨 시작", font=("Helvetica", 24, "bold"), command=lambda: switch_frame(master, page1.PageOne)
        ).pack()

        btn_back = tk.Button(self, text="뒤로", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page3.PageThree))
        btn_back.pack(side="left", padx=(280, 0))
