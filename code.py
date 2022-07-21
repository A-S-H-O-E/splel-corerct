from tkinter import *
import tkinter
from textblob import TextBlob
import textblob
def correctword():
    inputword = word1.get()
    obj = TextBlob(inputword)
    cw = obj.correct()
    word2.delete(0,END)
    word2.insert(10,cw)
def clearall():
    word1.delete(0,END)
    word2.delete(0,END)
if __name__ == "__main__":
    root = Tk()
    root.configure(background = "lightblue")
    root.geometry("600x250")
    root.title("splleing coreciton")
    header = Label(root,text = 'Spel checer ap',bg = 'lightblue',fg = 'black')
    header.grid(row = 0, column = 1)
    label1 = Label(root,text = 'Input Word',bg = 'lightgreen',fg = 'black')
    label1.grid(row=1,column = 1)
    label2 = Label(root,text = 'Correct Spelling',bg = 'pink',fg = 'black')
    label2.grid(row=3,column = 1)
    word1 = Entry()
    word2 = Entry()
    word1.grid(row=1,column = 2)
    word2.grid(row=3,column = 2)
    button1 = Button(root,text = 'Correct',bg = 'lightblue',fg = 'black',command = correctword)
    button1.grid(row=1,column = 3,padx = 10)
    clear = Button(root,text = 'clear',bg = '#ffcccb',fg = 'black',command = clearall)
    clear.grid(row=3,column = 3)
    root.mainloop()