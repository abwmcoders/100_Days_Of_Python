from tkinter import *


window = Tk()
window.title("Starting with GUI")
window.minsize(width=500, height= 300)


# Label
my_label = Label(text="I'am the made", font= ("Arial", 24, "italic"))
my_label.pack()
my_label["text"] = "Hello GUI"
my_label.config(text="Berry GUI")

# Button

def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text

button = Button(text="Button", command=button_clicked)
button.pack()


# Entry

input = Entry(width=15)
input.get()
input.pack()




window.mainloop()