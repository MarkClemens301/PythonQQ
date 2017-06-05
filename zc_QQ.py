#coding=utf-8
from Tkinter import *
from socket import *
import tkMessageBox
import datetime
import time
import thread

#全局的套接字
global udpCliSock
udpCliSock = socket(AF_INET, SOCK_DGRAM)

#此函数用于一个线程，每30秒向服务器发送消息
def send():
    while True:
        ADDR = ('202.114.196.97', 11560)
        udpCliSock.sendto('04#', ADDR)
        data, ADDR = udpCliSock.recvfrom(1024)
        temp_data=data[3:]
        if temp_data!='0':
            udpCliSock.sendto('05#', ADDR)
            data2, ADDR = udpCliSock.recvfrom(1024)
            data3=data2[3:]
            #字符串的切割，返回一个列表
            l=data3.split(':')
            text_msglist.insert(END,l[0]+' '+l[1]+':'+l[2]+':'+l[3]+'\n')
            text_msglist.insert(END,l[4]+'\n')
        else :
            text_msglist.insert(END,'无未读消息...\n')
        time.sleep(30000)

#添加朋友，发送消息
def add_friend():
    def send_message():
        msgcontent = '我:'+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
        text_msglist_child.insert(END, msgcontent, 'green')
        text_msglist_child.insert(END, text_msg_child.get('0.0', END))
        data=text_msg_child.get('0.0', END)
        text_msg_child.delete('0.0', END)
        data2='03#'+temp+'#'+data+'#'
        ADDR = ('202.114.196.97', 11560)
        udpCliSock.sendto(data2.encode('utf-8'), ADDR)
        data3, ADDR = udpCliSock.recvfrom(1024)
        text_msglist_child.insert(END,'服务器：'+data3+'\n')
       
    temp=friend_account.get()
    if temp=='':
        tkMessageBox.showinfo('提示','请输入账号后再添加！')
        return
    friend_account.set('')
    #子窗口 
    child=Toplevel()
    child.title(temp)
    frame_left_top   = Frame(child,width=380, height=270, bg='white')
    frame_left_center  = Frame(child,width=380, height=50, bg='white')
    frame_left_top.grid(row=0, column=0, padx=2, pady=5)
    frame_left_center.grid(row=1, column=0, padx=2, pady=5)
    frame_left_top.grid_propagate(0)
    frame_left_center.grid_propagate(0)
    text_msglist_child= Text(frame_left_top)
    text_msg_child= Text(frame_left_center)
    text_msglist_child.grid()
    text_msg_child.grid()
    Button(child, text='发送',command=send_message).grid(row=2,column=0,sticky=W)
    
def Register():
    def onsure():
            data='01#'+top_account.get()+'#'+top_password.get()+'#'+pass_word_sure.get()+'#'
            ADDR = ('202.114.196.97',11560)
            udpCliSock.sendto(data, ADDR)
            data, ADDR = udpCliSock.recvfrom(1024)
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
    #子窗口的数据
    top_account=StringVar()
    top_password=StringVar()
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
    ADDR = ('202.114.196.97',11560)
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(1024)
    if data=='02:01':
        tkMessageBox.showinfo('提示','登录成功！')
        root.destroy()
        root2=Tk()
        root2.title('QQ客户端')
        frame_left_top   = Frame(root2,width=300, height=200, bg='white')
        frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        frame_left_top.grid_propagate(0)
        global text_msglist
        text_msglist    = Text(frame_left_top)
        text_msglist.grid()
        Label(root2,text='账号：',width=8).grid(row=1,column=0)
        global friend_account
        friend_account=StringVar()
        Entry(root2,textvariable=friend_account).grid(row=2,column=0)
        Button(root2, text='添加好友',command=add_friend).grid(row=3,column=0)
        #开始线程
        thread.start_new_thread(send,())
        
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
   
root=Tk()
root.title('登录')
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
#主窗口的数据
cin_account=StringVar()
cin_password=StringVar()
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




















