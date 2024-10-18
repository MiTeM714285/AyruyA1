import tkinter as tk
import tkinter.messagebox as msgbox

import main
import page0
import page2
import re
from switchFrame import switch_frame

email_pattern = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._]+[@][a-zA-Z][A-Za-z.]+[.]\w{2,}')
phone_pattern = re.compile(r"^\d{3}-\d{4}-\d{4}")
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def agree_rad():
            if agree.get() == 0:
                main.entry['agree'] = True
                btn_next["state"] = tk.NORMAL
                entry_name["state"] = tk.NORMAL
                entry_phone["state"] = tk.NORMAL
                entry_email["state"] = tk.NORMAL
            elif agree.get() == 1:
                main.entry['agree'] = False
                btn_next["state"] = tk.DISABLED
                entry_name["state"] = tk.DISABLED
                entry_phone["state"] = tk.DISABLED
                entry_email["state"] = tk.DISABLED

        def valueToEntry(name, phone, email):
            if name == '' or name is None:
                msgbox.showerror("오류", "성명을 입력해주세요.")
            elif re.fullmatch(phone_pattern, phone) == None:
                msgbox.showerror("오류", "전화번호 형식을 올바르게 입력해주세요.\n(XXX-XXXX-XXXX)")
            elif re.fullmatch(email_pattern, email) == None:
                msgbox.showerror("오류", "이메일 형식을 올바르게 입력해주세요.\n(abcd@email.com)")
            else:
                main.entry['name'] = name
                main.entry['phone'] = phone
                main.entry['email'] = email
                switch_frame(master, page2.PageTwo)

        def initializeEntry():
            str = msgbox.askokcancel("알림","입력하신 정보들이 초기화됩니다. 계속하시겠습니까?")
            if str:
                switch_frame(master, page0.StartPage)


        # tk.Frame.configure(self, bg="blue")
        tk.Label(self, text="개인정보 이용 동의", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(30,5)
        )
        tk.Label(self, text="이와 관련하여 아래와 같이 귀하의 개인정보를 수집 및 이용 내용을 개인정보보호법 제15조(개인정보의 수집 및 이용) \n및 통계법 33조 (비밀의 보호 등)에 의거하여 안내 드리니 확인하여 주시기 바랍니다.", font=("Helvetica", 12, "bold")).pack(
            side="top", fill="x", pady=5
        )
        tk.Label(self,
                 text="1. 개인정보의 수집 이용 목적: 이벤트 진행에 따른 개인정보 파악\n2. 수집하는 개인정보의 항목 : 성명, 전화번호, 이메일\n3. 수집하는 개인정보의 항목 : 제출일로부터 1개월",
                 font=("Helvetica", 12, "normal")).pack(
            side="top", fill="x", pady=5
        )
        tk.Label(self,
                 text="귀하는 개인정보 수집, 활용에 대하여 동의를 거부할 권리가 있으며 동의하지 않을 시 본 이벤트를 진행하실 수 없습니다.",
                 font=("Helvetica", 12, "bold")).pack(
            side="top", fill="x", pady=(5,0)
        )
        tk.Label(self, text="이 사항들에 동의하십니까?", font=("Helvetica", 12, "bold")).pack(side="top", fill="x", pady=(0,5))
        agree = tk.IntVar()

        rad1 = tk.Radiobutton(self, text="동의합니다.", font=("Helvetica", 12, "bold"), variable=agree, value=0, command=agree_rad)
        rad2 = tk.Radiobutton(self, text="동의하지 않습니다.", font=("Helvetica", 12, "bold"), variable=agree, value=1, command=agree_rad)
        rad1.pack(pady=(30,0))
        rad2.pack(pady=(0,30))

        lbl_name = tk.Label(self, text="성명", font=("Helvetica", 14, "bold"))
        lbl_phone = tk.Label(self, text="전화번호 (XXX-XXXX-XXXX)", font=("Helvetica", 14, "bold"))
        lbl_email = tk.Label(self, text="이메일 (asdf@email.com)", font=("Helvetica", 14, "bold"))
        entry_name = tk.Entry(self, width=30, font=("Helvetica", 14, "bold"))
        entry_phone = tk.Entry(self, width=30, font=("Helvetica", 14, "bold"))
        entry_email = tk.Entry(self, width=30, font=("Helvetica", 14, "bold"))

        lbl_name.pack()
        entry_name.pack(pady=(0,20))
        lbl_phone.pack()
        entry_phone.pack(pady=(0,20))
        lbl_email.pack()
        entry_email.pack(pady=(0,20))

        btn_back = tk.Button(self, text="뒤로", font=("Helvetica", 20, "bold"), command=lambda: initializeEntry())
        btn_next = tk.Button(self, text="다음", font=("Helvetica", 20, "bold"), command=lambda: valueToEntry(entry_name.get(), entry_phone.get(), entry_email.get()))
        btn_back.pack(side="left", padx=(280,0))
        btn_next.pack(side="right", padx=(0,280))

        # 초기 상태
        if main.entry['agree']:
            rad1.select()
            btn_next["state"] = tk.NORMAL
            entry_name["state"] = tk.NORMAL
            entry_phone["state"] = tk.NORMAL
            entry_email["state"] = tk.NORMAL
        else:
            rad2.select()
            btn_next["state"] = tk.DISABLED
            entry_name["state"] = tk.DISABLED
            entry_phone["state"] = tk.DISABLED
            entry_email["state"] = tk.DISABLED
        entry_name.insert(tk.END, main.entry['name'])
        entry_phone.insert(tk.END, main.entry['phone'])
        entry_email.insert(tk.END, main.entry['email'])
