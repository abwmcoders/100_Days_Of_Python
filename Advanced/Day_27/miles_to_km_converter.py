from tkinter import *


def miles_km():
    miles = float(miles_input.get())
    km  = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


miles_label = Label(text="Miles")
miles_label.grid(column=1, row=0)
miles_label.pack()


miles_input = Entry()
miles_input.grid(column=3, row=0)
miles_input.pack()


is_equal_label = Label(text="Is equal to:")
is_equal_label.pack()


kilometer_result_label = Label(text="0")
kilometer_result_label.pack()


kilometer_label = Label(text="KM")
kilometer_label.pack()


calc_button = Button(text="Calculate", command=miles_km)
calc_button.pack()


window.mainloop()