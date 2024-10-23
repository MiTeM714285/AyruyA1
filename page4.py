import sqlite3
import tkinter as tk

import main
import page3
import page5
import random
import tkinter.messagebox as msgbox
from dbConnect import findLevelResult
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
            levelBoundary = "레벨 추첨 범위는 1.X ~ 10.X (V-ARCHIVE 기준) 입니다."
        elif main.entry['gameAndKeymode'] == 'ez2on-4':
            levelBoundary = "레벨 추첨 범위는 11 ~ 19 입니다."
        elif main.entry['gameAndKeymode'] == 'ez2on-5':
            levelBoundary = "레벨 추첨 범위는 10 ~ 18 입니다."
        elif main.entry['gameAndKeymode'] == 'ez2on-6':
            levelBoundary = "레벨 추첨 범위는 10 ~ 18 입니다."
        elif main.entry['gameAndKeymode'] == 'ez2on-8':
            levelBoundary = "레벨 추첨 범위는 8 ~ 16 입니다."

        def randomLevel():
            levelButton["state"] = tk.DISABLED
            btn_next['state'] = tk.NORMAL
            level = random.randrange(1, 10)
            main.entry['level'] = level
            try:
                levelResult = findLevelResult(main.entry['gameAndKeymode'], main.entry['level'])
            except sqlite3.Error:
                msgbox.showerror("오류", "데이터베이스 오류가 발생하였습니다.")
            levelResultText.config(text="결과:"+levelResult)

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

        levelResultText = tk.Label(self, text="결과:", font=("Helvetica", 30, "bold"))
        levelResultText.pack(side="top", fill="x", pady=20)

        levelButton = tk.Button(self, text="추첨 시작", font=("Helvetica", 24, "bold"), command=lambda: randomLevel())
        levelButton.pack(pady=(0, 50))

        btn_back = tk.Button(self, text="뒤로", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page3.PageThree))
        btn_next = tk.Button(self, text="다음", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page5.PageFive))
        btn_back.pack(side="left", padx=(280, 0))
        btn_next.pack(side="right", padx=(0, 280))

        # 초기 셋팅
        if main.entry['level'] != 0:
            levelButton['state'] = tk.DISABLED
            btn_next['state'] = tk.NORMAL
        else:
            levelButton['state'] = tk.NORMAL
            btn_next['state'] = tk.DISABLED

        levelResult = findLevelResult(main.entry['gameAndKeymode'], main.entry['level'])
        levelResultText.config(text="결과:" + levelResult)
