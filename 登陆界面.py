#coding=utf-8
from Tkinter import *
from socket import *
import tkMessageBox
from QQ import *

root=Tk()
root.title('登录')

#IP,端口号
#ADDR = ('202.114.196.97',11560)
global udpCliSock
udpCliSock = socket(AF_INET, SOCK_DGRAM)

cin_account=StringVar()
cin_password=StringVar()
#主窗口和子窗口
#子窗的两个数据
top_account=StringVar()
top_password=StringVar()

def Register():
    def onsure():
            data='01#'+top_account.get()+'#'+top_password.get()+'#'+pass_word_sure.get()+'#'
            #ADDR=("localhost",11567)
            ADDR = ('202.114.196.97',11560)
            udpCliSock.sendto(data, ADDR)
            data, ADDR = udpCliSock.recvfrom(1024)
            #udpCliSock.close()
            if data=='01:01':
                tkMessageBox.showinfo('提示','注册成功！')
            elif data=='01:02':
                tkMessageBox.showinfo('注册失败','确认密码不同！')
            elif data=='01:03':
                tkMessageBox.showinfo('注册失败','用户已存在！')
            else:
                tkMessageBox.showinfo('注册失败','格式不正确！')
            top.destroy()
    #子窗口
    top=Toplevel()
    top.title('注册界面')
    Label(top,text='账号：',width=8).grid(row=0,column=0)
    Entry(top,textvariable=top_account).grid(row=0,column=1)
    Label(top,text='密码：',width=8).grid(row=1,column=0)
    Entry(top,textvariable=top_password,show='*').grid(row=1,column=1)
    Label(top,text='确认密码：',width=8).grid(row=2,column=0)
    pass_word_sure=StringVar()
    Entry(top,textvariable=pass_word_sure,show='*').grid(row=2,column=1)
    Button(top,text='确认注册',width=8,command=onsure).grid(row=3)


#登录
def Login():
    if cin_account.get()=='' or cin_password.get()=='':
        tkMessageBox.showinfo('提示','请输入账号和密码！')
        return
    data='02#'+cin_account.get()+'#'+cin_password.get()+'#'
    #udpCliSock = socket(AF_INET, SOCK_DGRAM)
    ADDR = ('202.114.196.97',11560)
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(1024)
    if data=='02:01':
        tkMessageBox.showinfo('提示','登录成功！')
        #udpCliSock.close()
        main(udpCliSock)
        root.destroy()
        
    elif data=='02:02':
        tkMessageBox.showinfo('登录失败','密码错误！')
    elif data=='02:03':
        tkMessageBox.showinfo('登录失败','用户不存在！')
    elif data=='02:04':
        tkMessageBox.showinfo('提示','用户已登录！')
        #若用户已登录，让其离线
        temp='06#'
        udpCliSock.sendto(temp, ADDR)
        data2, ADDR = udpCliSock.recvfrom(1024)
        if data2=='06:01':
            tkMessageBox.showinfo('提示','离线成功！')
           
    else:
        tkMessageBox.showinfo('错误','输入格式有误！')
    #udpCliSock.close()
    

#控件的创建和布局
#grid:类似网格一样的布局
label1=Label(root,fg='white',bg='blue',width=10,height=10)
label1.grid(row=0,column=0)
label2=Label(root,fg='white',bg='blue',text="QQ登录界面",width=25,height=10)
label2.grid(row=0,column=1)
label3=Label(root,fg='white',bg='blue',width=10,height=10)
label3.grid(row=0,column=2)

#输入框与按钮
label4=Label(root,text='帐号：')
label4.grid(row=1,column=0)
#账户
CinAccount=Entry(root,textvariable=cin_account)
CinAccount.grid(row=1,column=1)
button1=Button(root,text='注册',width=8,command=Register)
button1.grid(row=1,column=2)
label5=Label(root,text='密码：')
label5.grid(row=2,column=0)
#密码
CinKey=Entry(root,textvariable=cin_password,show='*')
CinKey.grid(row=2,column=1)
button2=Button(root,text='登录',width=22,command=Login)
button2.grid(row=3,column=1)


root.mainloop()
















