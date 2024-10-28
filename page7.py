import sqlite3
import threading
import tkinter as tk
import keyboard

from dbConnect import insertInfo
import main
import time
import tkinter.messagebox as msgbox
from PIL import ImageGrab
import random

class PageSeven(tk.Frame):
    def __init__(self, master):
        global gameAndKeymode
        tk.Frame.__init__(self, master)

        conditions = random.sample(range(1,12),3)
        condition1 = conditions[0]
        condition2 = conditions[1]
        condition3 = conditions[2]
        str_condition1 = str(condition1)
        str_condition2 = str(condition2)
        str_condition3 = str(condition3)
        main.entry['condition1'] = condition1
        main.entry['condition2'] = condition2
        main.entry['condition3'] = condition3

        def start_keyboard_listener():
            keyboard.on_press(on_key_event)
            keyboard.wait()  #

        def on_key_event(event):
            if event.name == '0':
                curr_time = time.strftime("%Y%m%d-%H%M%S")
                img = ImageGrab.grab()
                img.save("screenshot/" + main.entry['name'] + "_" + main.entry['phone'] + "_" + main.entry['email'] + "_" + "{}.png".format(curr_time))
                main.entry['condition1'] = condition1
                main.entry['condition2'] = condition2
                main.entry['condition3'] = condition3
                try:
                    insertInfo(main.entry['name'], main.entry['phone'], main.entry['email'], main.entry['gameAndKeymode'], main.entry['musicname'], main.entry['difficulty'], main.entry['playstyle'], main.entry['condition1'], main.entry['condition2'], main.entry['condition3'])
                except sqlite3.Error:
                    msgbox.showerror("오류", "데이터베이스 오류가 발생하였습니다")
                message = "성과 제출이 완료되었습니다.\n적용 조건번호는 다음과 같습니다.\n" + str_condition1 + ", " + str_condition2 + ", " + str_condition3 + "\n자세한 사항은 이벤트 공지를 참조해 주세요.\n이벤트가 종료되었습니다. 감사합니다."
                str = msgbox.showinfo("알림", message)
                if str:
                    master.destroy()

        tk.Label(self, text="이벤트 진행을 위한 준비가 모두 끝났습니다.\n다음을 진행해 주세요.", font=("Helvetica", 20, "bold")).pack(
            side="top", fill="x", pady=(20, 5)
        )

        tk.Label(self, text="1. 자신이 선택한 게임을 아래와 같은 조건으로 플레이",
                 font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(15, 5)
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
                                                                                                             "노트 배치 옵션 : " + playstyle,
                 font=("Helvetica", 14, "normal")).pack(
            side="top", fill="x", pady=(5, 5))

        tk.Label(self, text="이외 노트 스타일 및 키설정 등 기타 옵션은 자유로 설정할 수 있습니다.",
                 font=("Helvetica", 14, "bold")).pack(
            side="top", fill="x", pady=(5, 25)
        )

        tk.Label(self, text="2. 리절트 화면이 뜨면 키보드 0번을 눌러 자신의 성과 제출하기",
                 font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(15, 5)
        )

        tk.Label(self, text="리절트 화면에서 무심코 넘어가기 버튼을 눌러 성과를 제출하지 못하는 불상사가 없도록 합니다.\n"
                            "성과 제출을 하지 않으면 실격 처리 됩니다.",
                 font=("Helvetica", 20, "bold"), fg="red").pack(
            side="top", fill="x", pady=(15)
        )

        tk.Label(self, text="모두 읽었다면, alt+tab을 눌러 자신이 선택한 게임으로 이동 후 게임을 진행합니다.",
                 font=("Helvetica", 25, "bold"), fg="blue").pack(
            side="top", fill="x", pady=(30)
        )

        listener_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
        listener_thread.start()