import pyshorteners
from tkinter import *
import pyperclip
top=Tk()
top.geometry("400x200")
top.title("URL SHORTNER")
top.configure(bg='#49A')
#top.iconbitmap('url_short.ico')
url=StringVar()
address=StringVar()

def urlshortner():
    urladdress = url.get()
    url_add=pyshorteners.Shortener().tinyurl.short(urladdress)
    address.set(url_add)

def copyurl():
    url_add=url_address.get()
    pyperclip.copy(url_add)
Label(top, text="URL Shorter App",font="algerian 20 bold").pack()
Entry(top,textvariable=url).pack(pady=5)
Button(top,text="Short Your URL",command=urlshortner).pack(pady=7)
Entry(top,textvariable=address).pack(pady=5)
Button(top,text="copy",command=copyurl).pack()
top.mainloop()
