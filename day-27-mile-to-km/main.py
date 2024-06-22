from tkinter import *


def convert():
    """
    Converts miles to kilometers and updates the result label.
    """
    miles = float(miles_entry.get())
    km = miles * 1.60934
    result_label.config(text=f"{miles} miles is equal to {km} km")


# Create the main window
window = Tk()
window.title("Mile to km Converter")  # Set the window title
window.minsize(width=300, height=200)  # Set the minimum size of the window

# Create the labels and input fields
miles_label = Label(text="Miles:")  # Label for miles input field
miles_label.grid(row=0, column=0)  # Position the label in the grid

miles_entry = Entry(width=10)  # Input field for miles
miles_entry.grid(row=0, column=1)  # Position the input field in the grid

# Create the convert button and attach the convert function to it
convert_button = Button(text="Convert", command=convert)
convert_button.grid(row=1, column=0, columnspan=2)  # Position the button in the grid

# Create the result label
result_label = Label(text="")  # Label for the result
result_label.grid(row=2, column=0, columnspan=2)  # Position the label in the grid

window.mainloop()  # Start the main event loop

