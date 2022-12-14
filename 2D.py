from tkinter import *
import hydraulicheadsimulate as hs

def main_():
    s=float(entry1.get())
    x=int(entry2.get())
    y=int(entry3.get())
    ht=int(entry4.get())
    hb=int(entry5.get())
    hl=int(entry6.get())
    hr=int(entry7.get())
    if va.get()=='1':
        L_R_NOFLOW=True
    else:
        L_R_NOFLOW=False 
    H_all=hs.hydraulic_head_finite_difference_calaculate(step_length=s,X_length=x,Y_length=y,H_top=ht,H_bottom=hb,H_left=hl,H_right=hr,L_R_NOFLOW=L_R_NOFLOW)
    hs.draw_3D_hydraulic_head(step_length=s,X_length=x,Y_length=y,H_ALL=H_all)

main = Tk()
main.title('承压含水层稳定二维流有限差分模拟')
#设置窗口大小
main.geometry('400x350')
main.maxsize(1920,1080)
main.minsize(280,200)
label1 = Label(main,text='输入差分步长:',font=('黑体',12))
label1.place(x = 10,y = 20,width=250,height=20)
entry1 = Entry(main,background='light sky blue')
entry1.place(x=250,y=20,width=80,height=20)

label2=Label(main,text='输入限定X轴长度:',font=('黑体',12))
label2.place(x=10,y=45,width=250,height=20)
entry2 = Entry(main,background='light sky blue')
entry2.place(x=250,y=45,width=80,height=20)

label3=Label(main,text='输入限定Y轴长度:',font=('黑体',12))
label3.place(x=10,y=70,width=250,height=20)
entry3=Entry(main,background='light sky blue')
entry3.place(x=250,y=70,width=80,height=20)

label4=Label(main,text='输入上部水头:',font=('黑体',12))
label4.place(x=10,y=95,width=250,height=20)
entry4=Entry(main,background='light sky blue')
entry4.place(x=250,y=95,width=80,height=20)

label5=Label(main,text='输入下部水头:',font=('黑体',12))
label5.place(x=10,y=120,width=250,height=20)
entry5=Entry(main,background='light sky blue')
entry5.place(x=250,y=120,width=80,height=20)

label6=Label(main,text='输入左侧水头:',font=('黑体',12))
label6.place(x=10,y=145,width=250,height=20)
entry6=Entry(main,background='light sky blue')
entry6.place(x=250,y=145,width=80,height=20)

label7=Label(main,text='输入右侧水头:',font=('黑体',12))
label7.place(x=10,y=170,width=250,height=20)
entry7=Entry(main,background='light sky blue')
entry7.place(x=250,y=170,width=80,height=20)

label8=Label(main,text='是否左右无流',font=('黑体',12))
label8.place(x=10,y=195,width=250,height=20)

va=StringVar()
radiobutton1 = Radiobutton(main,text='是',variable=va,value='1',font=('黑体',12))
radiobutton1.place(x=50,y=220,width=75,height=20)
radiobutton2 = Radiobutton(main,text='否',variable=va,value='0',font=('黑体',12))
radiobutton2.place(x=150,y=220,width=75,height=20)

button1=Button(main,text='计算',background='SeaGreen2',command=main_,font=('黑体',12))
button1.place(x=135,y=250,width=40,height=20)

main.mainloop()