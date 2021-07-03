from tkinter import *
import random
root=Tk()
root.geometry("500x500")
root.title("❤︎Background changer❤︎")


ColourDictionary={'colurs':
    ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1",
"deep pink","cyan"]
}
    
def change_background():
    random_no= random.randint(1, 8)
    random_color=ColourDictionary["colurs"][random_no]
    root.configure(background = random_color)

    
btn = Button(root,text="Click me to see magic!",command=change_background)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()