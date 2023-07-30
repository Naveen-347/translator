from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES

root = Tk()
root.geometry('980x500')
root.resizable(0,0)
root.title("Language Translator")
root.config(bg = 'gray')

Label(root, text = "LANGUAGE TRANSLATOR FROM ONE LANGUAGE TO ANOTHER LANGUAGE", font = "arial 15 bold", fg='black', bg='blue').pack()
Label(root,text =" naveen Translator", font = 'arial 16', fg='blue', bg='black' , height = '5', width = '20').pack(side = 'bottom')

Input_text = Text(root,font = 'arial 14', height = 11, fg= 'blue', bg='pink', wrap = WORD, padx=5, pady=5, width = 30)
Input_text.place(x=50,y = 100)

Output_text = Text(root,font = 'arial 14', height = 11, fg= 'black', bg='pink', wrap = WORD, padx=3, pady=3, width = 30)
Output_text.place(x = 600 , y = 100)
 

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= ('Telugu','Tamil','English','Hindi','Dutch','Bengali','Urdu','French','Spanish','Japanese','German','Portugese','Kannada','Malayalam'), width =22)
src_lang.place(x=100,y=60)
src_lang.set('Select input language')
src_lang.configure(state='readonly')

dest_lang = ttk.Combobox(root, values= ('Telugu','Tamil','English','Hindi','Dutch','Bengali','Urdu','French','Spanish','Japanese','German','Portugese','Kannada','Malayalam'), width =22)
dest_lang.place(x=700,y=60)
dest_lang.set('Select output language')
dest_lang.configure(state='readonly')

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
   
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate ,fg='blue', bg = 'black', activebackground = 'grey',width=8)
trans_btn.place(x = 455, y = 180)

def Clear():
    Input_text.delete(0.0, END)
    Output_text.delete(1.0, END)
    dest_lang.set('Choose language')

clear_btn = Button(root, text='Clear', font='arial 12 bold', pady=5, command=Clear, fg='white', bg='blue', activebackground='grey',width=8)
clear_btn.place(x=455, y=250)


root.mainloop()