from tkinter import * #함수를 다 갖다 씀

def process():
    print("테스트합니다.")


window =Tk()
window.title("연습")

label=Label(window, text="14주 수업이다.",fg="blue")
label.pack()    #pack() -> 화면에 표시
button=Button(window, text="click", command=process)    #버튼 클릭시 process함수 실행
button.pack()    #화면에 표시

window.mainloop()
