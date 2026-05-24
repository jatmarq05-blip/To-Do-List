#this a trial commit

import tkinter as tk

#root is the window we are creating. tk.Tk() is waht we are pulling fro tkinter library

root= tk.Tk()

root.geometry("600x400")
root.title("ToDoList")
#first thing in label is the parent object, in this case its the root, followed by named parameters, then design options like the font
#the font is in a tuple, first element is font family, second is font size, 
label= tk.Label(root,text="Welcome to my ToDoList!",font= ('Arial', 18))
# pad x and y add distance from the edge of the window, adds
label.pack(padx=20, pady=20)

#image
img= tk.PhotoImage(file="emojimeme.png")
label = tk.Label(root,image=img)
label.pack()

button= tk.Button(root,text="Click Me to Start!", font=('Arial',15))
button.pack()
label.pack(padx=10, pady=10)

root.mainloop()