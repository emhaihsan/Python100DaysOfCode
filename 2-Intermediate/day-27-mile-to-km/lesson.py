from tkinter import *

window = Tk()
window.title("Mile GUI Program")
window.minsize(width=500, height=300)

# Labels

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))



my_label['text'] = 'New text'
my_label.config(text='Another text')
my_label.grid(column=0, row=0)
# Button
def button_clicked(): 
    global input   
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


# Entry
input = Entry(width=10)
input.focus_set()
input.grid(column=2, row=2)


window.mainloop()