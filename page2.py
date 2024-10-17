import tkinter as tk

import page1
import page3


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # tk.Frame.configure(self, bg="red")
        tk.Label(self, text="이벤트 진행 룰(Rule)", font=("Helvetica", 18, "bold")).pack(
            side="top", fill="x", pady=(30, 5)
        )
        tk.Label(self, text="공통 사항",font=("Helvetica", 16, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self,
                 text="1. 이벤트는 개인정보를 입력한 대로 한 번만 수행 가능합니다.\n\n"
                      "2. 반드시 지정된 컨트롤러만으로 연주가 가능합니다. 컨트롤러 내 키설정은 자유입니다.\n\n"
                      "3. 연주 시작 직후 배속 조정 및 키 테스트에 있어 10초 정도의 유예시간이 주어지고, 단 1번의 재시작 기회가 주어집니다. \n하지만 그 이후 연주 중 중도 포기 및 폭사(게이지가 모두 소진되어 게임 오버)시 실격 됩니다. \n(단, 할인 쿠폰은 수령가능합니다)\n\n"
                      "4. 각종 사고(PC 오작동 및 컨트롤러 오작동)로 인해 정상적인 연주가 불가능할때, 해당 연주를 무효화하고 같은 조건으로 재연주가 가능합니다.",
                 font=("Helvetica", 12, "normal")).pack(
            side="top", fill="x", pady=5
        )
        tk.Label(self, text="DJMAX RESPECT V",font=("Helvetica", 16, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self,
                 text="1. 피버를 사용하지 않습니다.",
                 font=("Helvetica", 12, "normal")).pack(
            side="top", fill="x", pady=5
        )
        tk.Label(self, text="EZ2ON REBOOT:R", font=("Helvetica", 16, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self,
                 text="1. BASIC 판정모드로 진행합니다.\n\n"
                      "2. 판정 계기판은 텍스트 모드는 사용 가능하나, 인디케이터 모드 및 둘 다는 사용할 수 없습니다.",
                 font=("Helvetica", 12, "normal")).pack(
            side="top", fill="x", pady=5
        )
        img_indicator = tk.PhotoImage(file="image/indicator.png")
        tk.Label(self, image=img_indicator).pack(pady=(0,30))
        tk.Label.image = img_indicator

        btn_back = tk.Button(self, text="뒤로", font=("Helvetica", 20, "bold"),
                             command=lambda: master.switch_frame(page1.PageOne))
        btn_next = tk.Button(self, text="다음", font=("Helvetica", 20, "bold"),
                             command=lambda: master.switch_frame(page3.PageThree))
        btn_back.pack(side="left", padx=(360, 0))
        btn_next.pack(side="right", padx=(0, 360))
