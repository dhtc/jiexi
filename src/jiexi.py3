#-*- coding:utf-8 -*-
import sys,webbrowser



import tkinter
main=tkinter.Tk()
main.geometry("600x400+500+300")
main.title('解析')
l1=tkinter.Label(main,text='url')
l1.pack()
url=tkinter.Entry(main)
url.pack()
l2=tkinter.Label(main,text='number(目前仅有8条线路)')
l2.pack()
apinum=tkinter.Entry(main)
apinum.pack()
def jiexi():
    u = url.get()
    n= apinum.get()
    api = ('http://api.baiyug.cn/vip/index.php?url=', 'http://www.662820.com/xnflv/index.php?url=',
           'http://api.pucms.com/index.php?url=', 'http://api.wlzhan.com/sudu/?url=',
           'http://api.1008net.com/v.php?url=', 'http://vip.jisprh.com/index.php?url=',
           'http://jiexi.92fz.cn/player/vip.php?url=', 'http://jx.vgoodapi.com/jx.php?url=')
    n = int(n) - 1
    if n < 8:
        webbrowser.open_new(url=api[n] + u)
    else:
        print('<8')
button=tkinter.Button(main,command=jiexi,text='open',width=15,height=2)
button.pack()
main.mainloop()
