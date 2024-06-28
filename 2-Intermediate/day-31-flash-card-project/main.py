import tkinter
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
word = ""
# STEP 2.1 Read the data
data = pd.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")
flip = None

# STEP 2.2 Pick a random word
def pick_word():
    global word
    global flip
    word = random.choice(words)
    canvas.itemconfig(background, image=bg_white)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    flip =window.after(3000, flip_card)

# STEP 3 Flip the Cards
def flip_card():
    global word
    global flip
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    canvas.itemconfig(background, image=bg_green)
    window.after_cancel(flip)


# STEP 1 Create the User Interface with Tkinter
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_white = tkinter.PhotoImage(file="images/card_front.png")
bg_green = tkinter.PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=bg_white)
canvas.grid(column=0, row=0, columnspan=2)

lang_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

right_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_img, highlightthickness=0, command=pick_word)
right_button.grid(column=1, row=3)

wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=pick_word)
wrong_button.grid(column=0, row=3)

pick_word()

window.mainloop()

