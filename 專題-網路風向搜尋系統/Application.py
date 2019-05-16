import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image# pip install pillow
import pickle
import threading
from tkinter import scrolledtext
from button1 import *
from button3 import *

#建立視窗容器物件
root = tk.Tk()     
root.title("網路風向搜尋系統")
root.configure(background = 'black')
listvalues=''#save 下拉式選單的值

Hot()#預先載入熱門看板

#視窗大小
root.geometry("800x550")

#ttk外觀
style = ttk.Style()
style.configure("TLabel",font=('Microsoft Yahei', 13),background = 'black',foreground = 'white')
style.configure("TButton",font=('Arial', 13),background = 'blue',foreground = "black",relief = "solid") #,relief = 'ridge'

#=======================================建立標籤物件==========================================
#元件變數=元件名稱(容器物件變數, [元件選項])

label1 = tk.Label(root, text = "網路風向搜尋系統",font=('Microsoft Yahei', 24),bg = 'black',fg = 'white')   
label1.place(x = 235, y = 23)

label2 = ttk.Label(root, text = "關鍵字搜尋 : ",style = "TLabel")   
label2.place(x = 40, y = 93)

label3 = ttk.Label(root, text = "熱門看板 : ",style = "TLabel")   
label3.place(x = 355, y = 93)

#========================================文字方塊=============================================
var_search_word = tk.StringVar()
searchWord = tk.Entry(root, text = "searchWord",bd = 3,font=('Microsoft Yahei', 10),textvariable = var_search_word)
searchWord.place(x = 145, y = 93)
#儲存搜尋過的關鍵字
def storeSearchWord():
    global listvalues
    store_word = var_search_word.get() #獲取輸入的關鍵字
    # 這邊就...看大神怎麼發揮了
    # pickle a variable to a file
    file = open('search_word.pickle','wb') 
    pickle.dump(store_word,file)
    file.close()
    Search(store_word,listvalues)
#========================================下拉選單=============================================
window0 = tkinter.IntVar(root, value=0)
def go(*args):   #处理事件，*args表示可变参数
    '''
    #if comboxlist.get() == "1":
        def SearchKeyWord():
            #點選搜尋之後的畫面
            tkinter.messagebox.showinfo( "123", "456")
            #tkinter.messagebox.showwarning("警告","警告")#提出警告对话窗
            #tkinter.messagebox.showerror("錯誤","錯誤")#提出错误对话窗
            #tkinter.messagebox.askquestion("?","要退出搜尋嗎?")#询问选择对话窗
    '''
 
comvalue = tk.StringVar() #窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(root,font=('Microsoft Yahei', 13),textvariable = comvalue) #初始化
comboxlist.config(value=TitlePageNames)#hot boards
#裡面的值可能要用呼叫函式的方式之類的


comboxlist.current(0)  #选择第一个
comboxlist.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist.place(x = 445, y = 93)

#=========================================顯示================================================

display1 = tk.Text(root,bd = 5,width = 30,height = 25)
display1.place(x = 40,y = 143)

scrolW = 60
scrolH = 25
scr = scrolledtext.ScrolledText(root,width = scrolW,height = scrolH,wrap = tk.WORD)
scr.place(x = 305,y = 143)


def Button1click():
    #推噓文分析
    global Content
    
    Search(var_search_word.get(),comboxlist.get())
    FetchCon(var_search_word.get(),comboxlist.get())
    display1.delete("1.0",tk.END)
    #temp = display1.get("1.0",tk.END) #取得整個text當中的內容(get)
    #print(temp)
    #display1.insert(tk.END,"文字內容")  #將文字插入最後
    #display1.insert(1.0,"文字內容") #將文字插入最前面(insert)
    #或是
    Good=GTotalGood()
    Bad=GTotalBad()
    quote = '推文數:'+str(Good)+'\n'+'噓文數:'+str(Bad)
    if Good>Bad:
        quote+='\n\n\n\n\n正面評價'
    elif Good<=Bad and Bad:
        quote+='\n\n\n\n\n負面評價'
    else:
        quote+='\n\n\n\n\n無評價'
    display1.insert("insert",quote)
    scr.delete("1.0", tk.END)
    print(len(Content))
    for x in Content:
        if x[0]=='R' or x[0]=='[':
            continue
        else:
            scr.insert('insert',x+'\n')
    Content.clear()
def Button2click():
    #單字分析
    display1.delete("1.0",tk.END)
    #temp = display1.get("1.0",tk.END) #取得整個text當中的內容(get)
    #print(temp)
    #display1.insert(tk.END,"文字內容")  #將文字插入最後
    #display1.insert(1.0,"文字內容") #將文字插入最前面(insert)
    #或是
    quote = """值or文字內容"""
    display1.insert("insert",quote)
def Button3click():
    #句子分析
    global PN
    global Content
    Search(var_search_word.get(),comboxlist.get())
    FetchCon(var_search_word.get(),comboxlist.get())
    display1.delete("1.0",tk.END)
    Good=GTotalGood()
    Bad=GTotalBad()
    quote = '文章內推文:'+str(Good)+'\n'+'文章內噓文:'+str(Bad)
    
    #temp = display1.get("1.0",tk.END) #取得整個text當中的內容(get)
    #print(temp)
    #display1.insert(tk.END,"文字內容")  #將文字插入最後
    #display1.insert(1.0,"文字內容") #將文字插入最前面(insert)
    #或是
    pre()
    x=0
    scr.delete(1.0, tk.END)
    B=0
    G=0
    for i in range(len(Content)):
        if Content[i][0]=='R' or Content[i][0]=='[':
            scr.insert("insert",Content[i]+'\n','title')
        else:
            if PN[x]=='正面':
                tag='pos'
                G+=1
            else:
                tag='neg'
                B+=1
            scr.insert("insert",PN[x]+'\t'+Content[i]+'\n',tag)
            x+=1
    quote+='\n\n\n\n\n系統預測推文:'+str(G)+'\n系統預測噓文:'+str(B)
    if G>B:
        quote+='\n正面評價'
    elif G<=B and B:
        quote+='\n負面評價'
    else:
        quote+='\n無評價'
    display1.insert("end",quote)
    scr.tag_config('neg',foreground='red')
    scr.tag_config('pos',foreground='green')
    Content.clear()
#=========================================按鈕================================================

button1 = ttk.Button(root, text = "推噓文分析",style = "TButton",command = Button1click) 
button1.place(x = 75, y = 500)

#button2 = ttk.Button(root, text = "單字分析",style = "TButton",command = Button2click)
#button2.place(x = 275, y = 500)

button3 = ttk.Button(root, text = "句子分析",style = "TButton",command = Button3click)
button3.place(x = 475, y = 500)

#======================================關閉視窗==============================================
def func1():
    if tkinter.messagebox.askyesno("關閉窗口","確認關閉窗口嗎?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW",func1)

#主視窗迴圈顯示
root.mainloop()
#有例子提供參考(主要是覺得應該會比我更看得懂function的部分)
'''
import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle

window = tk.Tk()
window.title('Welcome to Mofan Python')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                               'You have not signed up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()
'''
