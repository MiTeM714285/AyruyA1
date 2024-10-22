import tkinter as tk

import main


class PageSeven(tk.Frame):
    def __init__(self, master):
        global gameAndKeymode
        tk.Frame.__init__(self, master)

        tk.Label(self, text="이벤트 진행을 위한 준비가 모두 끝났습니다.\n다음을 진행해 주세요.", font=("Helvetica", 20, "bold")).pack(
            side="top", fill="x", pady=(20, 5)
        )

        tk.Label(self, text="1. alt+tab을 눌러 자신에 해당하는 게임으로 화면 전환 후 아래와 같은 조건으로 플레이", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(15)
        )

        tk.Label(self, text="아래와 같은 조건으로 플레이하지 않을 시, 실격 처리될 수 있습니다.",
                 font=("Helvetica", 20, "bold"), fg="red").pack(
            side="top", fill="x", pady=(15)
        )

        if main.entry['gameAndKeymode'] == 'djmax-4':
            gameAndKeymode = 'DJMAX RESPECT V - 4B MODE'
        elif main.entry['gameAndKeymode'] == 'djmax-5':
            gameAndKeymode = 'DJMAX RESPECT V - 5B MODE'
        elif main.entry['gameAndKeymode'] == 'djmax-6':
            gameAndKeymode = 'DJMAX RESPECT V - 6B MODE'
        elif main.entry['gameAndKeymode'] == 'djmax-8':
            gameAndKeymode = 'DJMAX RESPECT V - 8B MODE'
        elif main.entry['gameAndKeymode'] == 'ez2on-4':
            gameAndKeymode = 'EZ2ON REBOOT:R - 4K BASIC'
        elif main.entry['gameAndKeymode'] == 'ez2on-5':
            gameAndKeymode = 'EZ2ON REBOOT:R - 4K BASIC'
        elif main.entry['gameAndKeymode'] == 'ez2on-6':
            gameAndKeymode = 'EZ2ON REBOOT:R - 4K BASIC'
        elif main.entry['gameAndKeymode'] == 'ez2on-8':
            gameAndKeymode = 'EZ2ON REBOOT:R - 4K BASIC'

        musicname = main.entry['musicname']
        difficulty = main.entry['difficulty']
        playstyle = main.entry['playstyle']

        tk.Label(self, text="게임 및 모드 : " + gameAndKeymode + "\n"
                "과제곡 및 난이도 : " + musicname + " [" + difficulty + "]\n"
                "노트 배치 옵션 : " + playstyle, font=("Helvetica", 12, "normal")).pack(
            side="top", fill="x", pady=(5, 5))

        tk.Label(self, text="이외 노트 스타일 및 키설정 등 기타 옵션은 자유로 설정할 수 있습니다.",
                 font=("Helvetica", 14, "bold")).pack(
            side="top", fill="x", pady=(5,25)
        )

        tk.Label(self, text="2. 리절트 화면이 뜨면 키보드 0번을 눌러 자신의 성과 제출하기",
                 font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(15)
        )

        tk.Label(self, text="리절트 화면에서 무심코 진행 버튼을 눌러 성과를 제출하지 못하는 불상사가 없도록 합니다.\n"
                            "성과 제출을 하지 않으면 실격 처리 됩니다.",
                 font=("Helvetica", 20, "bold"), fg="red").pack(
            side="top", fill="x", pady=(15)
        )