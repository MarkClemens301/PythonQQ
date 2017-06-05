#coding=utf-8
from Tkinter import *
import datetime
import time
import thread
from socket import *




#udpCliSock = socket(AF_INET, SOCK_DGRAM)


#此函数用于一个线程
def send():
    while True:
        ADDR = ('202.114.196.97', 11560)
        udpCliSock.sendto('04#', ADDR)
        data, ADDR = udpCliSock.recvfrom(1024)
        #text_msglist.insert(END,'服务器：'+data)
        print data
        #udpCliSock.close()
        time.sleep(300)
        


#发送按钮事件
def add_friend():
    def send_message():
        msgcontent = '我:'+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
        text_msglist.insert(END, msgcontent, 'green')
        text_msglist.insert(END, text_msg.get('0.0', END))
        data=text_msg.get('0.0', END)
        text_msg.delete('0.0', END)
        data2='03#'+temp+'#'+data+'#'
        #ADDR = ('202.114.196.97', 11560)
        #udpCliSock = socket(AF_INET, SOCK_DGRAM)
        udpCliSock.sendto(data2.encode('utf-8'), ADDR)
        data3, ADDR = udpCliSock.recvfrom(1024)
        #udpCliSock.close()
        text_msglist.insert(END,'服务器：'+data3+'\n')
        
        
    child=Toplevel()
    temp=friend_account.get()
    child.title(temp)
    frame_left_top   = Frame(child,width=380, height=270, bg='white')
    frame_left_center  = Frame(child,width=380, height=50, bg='white')
    frame_left_top.grid(row=0, column=0, padx=2, pady=5)
    frame_left_center.grid(row=1, column=0, padx=2, pady=5)
    frame_left_top.grid_propagate(0)
    frame_left_center.grid_propagate(0)
    text_msglist    = Text(frame_left_top)
    text_msg      = Text(frame_left_center)
    text_msglist.grid()
    text_msg.grid()
    Button(child, text='发送',command=send_message).grid(row=2,column=0,sticky=W)
    

def main(udpCliSock1):
    global udpCliSock
    udpCliSock=udpCliSock1
    udpCliSock = socket(AF_INET, SOCK_DGRAM)
    root = Tk()
    root.title('QQ客户端')
    frame_left_top   = Frame(width=300, height=200, bg='white')
    frame_left_top.grid(row=0, column=0, padx=2, pady=5)
    frame_left_top.grid_propagate(0)
    global text_msglist
    text_msglist    = Text(frame_left_top)
    text_msglist.grid()
    Label(root,text='账号：',width=8).grid(row=1,column=0)
    global friend_account
    friend_account=StringVar()
    Entry(root,textvariable=friend_account).grid(row=2,column=0)
    Button(root, text='添加好友',command=add_friend).grid(row=3,column=0)
    
    #开始线程
    thread.start_new_thread(send,())
    #主事件循环
    root.mainloop()
    
if(__name__ == '__main__'):
    main(udpCliSock)











