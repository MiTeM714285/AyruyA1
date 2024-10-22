import tkinter as tk

import main
import page4
import page6
import random

from dbConnect import findMusicAndDifficulty
from switchFrame import switch_frame


class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def randomMusicAndDifficulty():
            musicButton["state"] = tk.DISABLED
            btn_next['state'] = tk.NORMAL
            musicAndDifficultyIndex = random.randrange(0, 3)
            main.entry['musicname'] = musicAndDifficulty[musicAndDifficultyIndex][0]
            main.entry['difficulty'] = musicAndDifficulty[musicAndDifficultyIndex][1]
            musicResultText.config(text="결과:"+musicAndDifficulty[musicAndDifficultyIndex][0] + " [" + musicAndDifficulty[musicAndDifficultyIndex][1] + "]")

        # tk.Frame.configure(self, bg="red")
        fileUrl = "image/" + main.entry['gameAndKeymode'] + ".png"
        img_gameAndKeymode = tk.PhotoImage(file=fileUrl).subsample(2)
        tk.Label(self, image=img_gameAndKeymode).pack(side="top", pady=(30,15))
        tk.Label.image = img_gameAndKeymode

        tk.Label(self, text="곡 랜덤 추첨 결정", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(30, 5)
        )
        tk.Label(self,
                 text="추첨된 레벨 범위 내로 다음 중 과제곡을 랜덤으로 추첨합니다.",
                 font=("Helvetica", 16, "bold")).pack(
            side="top", fill="x", pady=(10,10)
        )

        music1 = tk.Label(self, text="곡명1 [난이도]", font=("Helvetica", 25, "bold"))
        music2 = tk.Label(self, text="곡명2 [난이도]", font=("Helvetica", 25, "bold"))
        music3 = tk.Label(self, text="곡명3 [난이도]", font=("Helvetica", 25, "bold"))
        music1.pack(side="top", fill="x")
        music2.pack(side="top", fill="x")
        music3.pack(side="top", fill="x", pady=(0, 20))

        tk.Label(self,
                 text="주의:추첨 시작 버튼은 한 번만 유효하며, 다시는 되돌이킬 수 없습니다.",
                 font=("Helvetica", 18, "bold"), fg="red").pack(
            side="top", fill="x", pady=20
        )

        musicResultText = tk.Label(self, text="결과:", font=("Helvetica", 30, "bold"))
        musicResultText.pack(side="top", fill="x", pady=20)

        musicButton = tk.Button(self, text="추첨 시작", font=("Helvetica", 24, "bold"), command=lambda: randomMusicAndDifficulty())
        musicButton.pack(pady=(0, 20))

        btn_back = tk.Button(self, text="뒤로", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page4.PageFour))
        btn_next = tk.Button(self, text="다음", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page6.PageSix))
        btn_back.pack(side="left", padx=(280, 0))
        btn_next.pack(side="right", padx=(0, 280))

        # 초기 셋팅
        musicAndDifficulty = findMusicAndDifficulty(main.entry['gameAndKeymode'], main.entry['level'])
        music1.config(text=musicAndDifficulty[0][0] + " [" + musicAndDifficulty[0][1] + "]")
        music2.config(text=musicAndDifficulty[1][0] + " [" + musicAndDifficulty[1][1] + "]")
        music3.config(text=musicAndDifficulty[2][0] + " [" + musicAndDifficulty[2][1] + "]")

        if main.entry['musicname'] != '':
            musicButton['state'] = tk.DISABLED
            btn_next['state'] = tk.NORMAL
            musicResultText.config(text="결과:" + main.entry['musicname'] + " [" + main.entry['difficulty'] + "]")
        else:
            musicButton['state'] = tk.NORMAL
            btn_next['state'] = tk.DISABLED
            musicResultText.config(text="결과:")


