from tkinter import * #함수를 다 갖다 씀

#화씨 -> 섭씨
def process1():
    temp=float(e1.get())        #get()은 가져오는거(e1내용)
    myt=(temp-32)*5/9
    e2.insert(0, str(myt))         #insert()은 넣는것(e2에 삽입)

#섭씨 -> 화씨
def process2():
    temp=float(e2.get())        
    myt=(temp*(9/5))+32
    e1.insert(0, str(myt))       
    
window =Tk()

l1=Label(window, text="화씨")
l1.pack()
e1=Entry(window)    #입력받을수 있는 클래스
e1.pack()

l2=Label(window, text="섭씨")
l2.pack()
e2=Entry(window)    #입력받을수 있는 클래스
e2.pack()

b1=Button(window, text="화씨 -> 섭씨",command=process1)
b2=Button(window, text="섭씨 -> 화씨",command=process2)
b1.pack()
b2.pack()


window.mainloop()
