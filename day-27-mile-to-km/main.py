from tkinter import *


def convert():
    """
    Converts miles to kilometers and updates the result label.
    """
    miles = float(miles_entry.get())
    km = miles * 1.60934
    result_label.config(text=str(km))


# Create the main window
window = Tk()
window.title("Mile to km Converter")  # Set the window title

# Create the labels and input fields
miles_label = Label(text="Miles:")  # Label for miles input field
miles_label.grid(row=0, column=2, pady=(20,0))  # Position the label in the grid

miles_entry = Entry(width=10)  # Input field for miles
miles_entry.grid(row=0, column=1, pady=(20,0))  # Position the input field in the grid

# Create the convert button and attach the convert function to it
convert_button = Button(text="Calculate", command=convert)
convert_button.grid(row=2, column=1, pady=(0,20))  # Position the button in the grid

# Create the result label
result_label = Label(text="0")  # Label for the result
result_label.grid(row=1, column=1)  # Position the label in the grid

equal_label = Label(text="is equal to")  # Label for the equal sign
equal_label.grid(row=1, column=0)  # Position the label in the grid

km_label = Label(text="km")  # Label for kilometers
km_label.grid(row=1, column=2)  # Position the label in the grid
window.mainloop()  # Start the main event loop

