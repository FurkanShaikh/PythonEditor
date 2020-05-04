from tkinter import Tk,scrolledtext,filedialog,Menu,END,messagebox
import os

#win for main window
win=Tk(className = " Text Editor")
textArea =scrolledtext.ScrolledText(win,width=100 , height=80)

#function

def open_file():
    file = filedialog.askopenfile(parent=win,mode='rb',title='SELECT A TEXT FILE',filetypes=(('Text file','*.txt'),('All files','*.*')))

    if file != None:
        content = file.read()
        textArea.insert('1.0',content)
        file.close()

def savefile():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exito():
    ans = messagebox.askyesno("QUIT","Are you sure you want to quit?")
    if(ans):
        win.destroy()
    
def about():
    label=messagebox.showinfo("ABOUT","Text Editor by Team FPS.\nCredits: \nShubham Mishra(Roll no:18) \nPallav Chaudhari(Roll no: 7) \nFurkan Shaikh(Roll no: 29)")

def help():
    label=messagebox.showinfo("HELP","This is a simple text editor programmed in python. Python was created in the early 1990s by Guido van Rossum at Stichting. Know more at https://www.python.org/ ")    

def __cut():
       textArea.event_generate("<<Cut>>")

def __copy():
      textArea.event_generate("<<Copy>>")

def __paste():
      textArea.event_generate("<<Paste>>")

def newfile():
    win.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0,END)
    
#menu option
menu = Menu(win)
win.config(menu=menu)
filename = Menu(menu, tearoff=0)
menu.add_cascade(label="File",menu=filename)
filename.add_command(label="New", command = newfile)
filename.add_command(label="Open", command = open_file) 
filename.add_command(label="Save",command= savefile)
filename.add_separator()
filename.add_command(label="Exit", command = exito)

EditMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit",menu=EditMenu)
EditMenu.add_command(label="Cut",command=__cut) 
EditMenu.add_command(label="Copy",command=__copy)         
EditMenu.add_command(label="Paste",command=__paste)             

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label = "Help",command = help)
menu.add_cascade(label="About",command = about)



textArea.pack()
# keep window open
win.mainloop()



