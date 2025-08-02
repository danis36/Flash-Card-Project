from asyncio import current_task

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import csv
import random
to_learn = {}
#-------------------------------------------New_Word--------------------------------------------------------------------

try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words_to_learn.csv")
    to_learn = original_data.to_dict(orient="records")
else:
        to_learn = data.to_dict(orient="records")

current_card = {}


def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()
#----------------------------- UI SETUP --------------------------------------------------------------------------------#
window = Tk()

flip_timer = window.after(3000, func=flip_card)
window.title('Flashy')
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)
#--------------------------------------WORDS----------------------------------------------------------------------------

#---------------------------------------Buttons-------------------------------------------------------------------------
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=new_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,command=is_known)
known_button.grid(row=1, column=1)


new_word()


window.mainloop()