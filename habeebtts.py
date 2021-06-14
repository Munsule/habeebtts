# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:25:43 2021

@author: Munsule
"""

import tkinter as tk
from tkinter import ttk, filedialog

from tkinter import *
import pyttsx3 

main=Tk()


main.title('Untitled')

#Combobox
def month_changed(event):
    msg = f'You selected {month_cb.get()}!'
    showinfo(title='Result', message=msg)


# month of year
months = (50, 60, 70, 80, 90, 100,110,120,130,140,150,160,170,180,190,200)

label = ttk.Label(text="Please select a month:")
label.pack()

# create a combobox
selected_month = tk.StringVar()

month_cb = ttk.Combobox(main, textvariable=selected_month)
month_cb['values'] = months
month_cb['state'] = 'readonly'  # normal
month_cb.pack()

month_cb.bind('<<ComboboxSelected>>', month_changed)



#   Scrollbar functionality for the main window
scrollbar=Scrollbar(main);
scrollbar.pack(side=RIGHT,fill=Y)

textbody=Text(main,yscrollcommand=scrollbar.set)
textbody.pack(fill=BOTH)

speech=pyttsx3.init()

scrollbar.config(command=textbody.yview)
""" Menu Operational functions are declared here

"""


def read_all():    
    speech.setProperty("language","en-UK")
    speech.setProperty("rate",150)
    speech.setProperty("pitch",1)
    speech.say(textbody.get("1.0",END))    
    speech.save_to_file(textbody.get("1.0",END),'C:/converted.mp3')
    speech.runAndWait()
    
# Save Audio File Menu
def saveAudioFile():
    if(main.title() == "Untitled"):
        tf=filedialog.asksaveasfilename(
                initialdir="C:/Users/",
                title="Save File Dialog",
                filetypes=(("Text Files","*.*"),)
                )    
        main.title(tf)
        tf=open(tf,"w+")
        tf.write(textbody.get(1.0,END))
        tf.close()
        speech.save_to_file(textbody.get(1.0,END),'C:/Users/test.mp3')
    else:     
        tf=main.title()
        tf=open(tf,"w+")
        tf.write(textbody.get(1.0,END))
        speech.save_to_file(textbody.get(1.0,END),'C:/Users/test.mp3')
        
#   Menubar declaration
menubar=Menu(main)

#   Filemenu Functions

# OpenFile Menu Item
def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.*"),)
        )
    #  pathh.insert(END, tf)
    tf = open(tf,'r')  # or tf = open(tf, 'r')
    data = tf.read()
    textbody.delete(1.0,END)
    textbody.insert(END, data)
    main.title(tf.name)
    tf.close()
    
#   Create New File
def newFile():
    textbody.delete(1.0,END)    
    main.title("Untitle")
    
# Save File Menu
def saveFile():
    if(main.title() == "Untitled"):
        tf=filedialog.asksaveasfilename(
                initialdir="C:/Users/",
                title="Save File Dialog",
                filetypes=(("Text Files","*.*"),)
                )    
        main.title(tf)
        tf=open(tf,"w+")
        tf.write(textbody.get(1.0,END))
        tf.close()
    else:     
        tf=main.title()
        tf=open(tf,"w+")
        tf.write(textbody.get(1.0,END))
    
#   Filemenu declaration with cascade/items
file=Menu(menubar, tearoff=0)
file.add_command(label="New", command=newFile)
file.add_separator()

file.add_command(label="Open", command=openFile)
file.add_separator()

file.add_command(label="Save", command=saveFile)
file.add_separator()

file.add_command(label="Save As", command=saveAudioFile)
file.add_separator()

file.add_command(label="Exit", command=main.quit)
file.add_separator()

menubar.add_cascade(label="File",menu=file)

#Editmenu declaration with cascade/items
edit=Menu(menubar, tearoff=0)

edit.add_command(label="Undo")
edit.add_separator()

edit.add_command(label="Undo")
edit.add_separator()

edit.add_command(label="Redo")
edit.add_separator()

edit.add_command(label="Copy")
edit.add_separator()

edit.add_command(label="Paste")
edit.add_separator()

edit.add_command(label="Cut")
edit.add_separator()

edit.add_command(label="Select All")
edit.add_separator()

edit.add_command(label="Replace All")
edit.add_separator()

menubar.add_cascade(label="Edit", menu=edit)

menubar.add_command(label="Read", command=read_all)

# Helpmenu declaration with cascade

help=Menu(menubar,tearoff=0)

help.add_command(label="About")
help.add_separator()

help.add_command(label="Help")
help.add_separator()

menubar.add_cascade(label="help", menu=help)


#   Text widget for the editing
main.config(menu=menubar)


main.mainloop()