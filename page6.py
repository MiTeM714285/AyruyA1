import tkinter as tk
import main
import page5
import page7
import random
from switchFrame import switch_frame


class PageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def randomStyle():
            styleButton["state"] = tk.DISABLED
            styleIndex = random.randrange(1, 6)
            if styleIndex == 1:
                styleResult = "FREE"
            elif styleIndex == 2:
                styleResult = "NONE"
            elif styleIndex == 3:
                styleResult = "RANDOM"
            elif styleIndex == 4:
                styleResult = "MIRROR"
            else:
                styleResult = "HARF(FLIP) RANDOM"

            main.entry['playstyle'] = styleResult
            styleResultText.config(text="결과:"+styleResult)

        fileUrl = "image/" + main.entry['gameAndKeymode'] + ".png"
        img_gameAndKeymode = tk.PhotoImage(file=fileUrl).subsample(2)
        tk.Label(self, image=img_gameAndKeymode).pack(side="top", pady=(30, 15))
        tk.Label.image = img_gameAndKeymode

        tk.Label(self, text="노트 배치 옵션 랜덤 추첨 결정", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(30, 5)
        )
        tk.Label(self,
                 text="추첨된 곡을 다음 노트 배치 옵션 중 추첨될 하나의 옵션으로 연주하셔야 합니다.",
                 font=("Helvetica", 16, "bold")).pack(
            side="top", fill="x", pady=(10, 10)
        )

        style1 = tk.Label(self, text="FREE (어떤 옵션으로 사용하던지 간에 자유)", fg="blue", font=("Helvetica", 15, "bold"))
        style2 = tk.Label(self, text="NONE (정규 배치. 노트 배치 옵션을 사용하지 않음)", fg="blue", font=("Helvetica", 15, "bold"))
        style3 = tk.Label(self, text="RANDOM (레인의 순서를 무작위로 뒤섞음)", fg="blue", font=("Helvetica", 15, "bold"))
        style4 = tk.Label(self, text="MIRROR (레인의 순서를 반대로 뒤집음)", fg="blue", font=("Helvetica", 15, "bold"))
        style5 = tk.Label(self, text="HARF(FLIP) RANDOM (레인을 2세트로 분리 후 각각 레인 순서를 뒤섞음)", fg="blue", font=("Helvetica", 15, "bold"))
        style1.pack(side="top", fill="x")
        style2.pack(side="top", fill="x")
        style3.pack(side="top", fill="x")
        style4.pack(side="top", fill="x")
        style5.pack(side="top", fill="x", pady=(0, 20))

        tk.Label(self,
                 text="주의:추첨 시작 버튼은 한 번만 유효하며, 다시는 되돌이킬 수 없습니다.",
                 font=("Helvetica", 18, "bold"), fg="red").pack(
            side="top", fill="x", pady=20
        )

        styleResultText = tk.Label(self, text="결과:", font=("Helvetica", 30, "bold"))
        styleResultText.pack(side="top", fill="x", pady=20)

        styleButton = tk.Button(self, text="추첨 시작", font=("Helvetica", 24, "bold"), command=lambda: randomStyle())
        styleButton.pack(pady=(0, 20))

        btn_back = tk.Button(self, text="뒤로", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page5.PageFive))
        btn_next = tk.Button(self, text="다음", font=("Helvetica", 20, "bold"),
                             command=lambda: switch_frame(master, page7.PageSeven))
        btn_back.pack(side="left", padx=(280, 0))
        btn_next.pack(side="right", padx=(0, 280))

        # 초기 셋팅
        if main.entry['playstyle'] != '':
            styleButton['state'] = tk.DISABLED

        styleResultText.config(text="결과:" + main.entry['playstyle'])
