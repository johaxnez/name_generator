from tkinter import *
import pandas
import random
from pygame import mixer
import pyperclip
from tkinter import messagebox

FONT = ("Times New Roman", 26, "italic")
about_text = Text(height=20, width=60)

# Names
given_name = ""
attribute = ""
place = ""
full_name = ""

data = pandas.read_csv("name_file/names_attribute_places.csv")
generation_dict = data.to_dict(orient="records")


# About
with open("about/about.csv", mode="r") as file:
    info = file.read()


# --------------------FUNCTIONS-------------------------#


def generate_name():
    global given_name, place_name_button, attribute_button
    place_name_button = Button(text="Place", command=generate_place)
    attribute_button = Button(text="Attribute", command=generate_attribute)
    first_generate = random.choice(generation_dict)
    given_name = first_generate["Given name"]
    generate_name_button.config(text="reset", command=reset_name)
    entry.insert(END, given_name)
    place_name_button.place(x=530, y=220)
    attribute_button.place(x=600, y=220)
    return given_name

def reset_name():
    global given_name_text, place_name_button, attribute_button, full_name
    copy_name_button.place(x=3000, y=4000)
    full_name = ""
    entry.delete(0, END)
    canvas.itemconfig(background, image=background_menu)
    generate_name_button.config(text="generate", command=generate_name)
    place_name_button.destroy()
    attribute_button.destroy()
    return full_name



def generate_attribute():
    global attribute, given_name, full_name
    copy_name_button.place(x=790, y=195)
    attribute_generate = random.choice(generation_dict)
    attribute = attribute_generate["Attribute"]
    entry.insert(END, f" the {attribute}")
    full_name = f"{str(given_name)} the {str(attribute)}"
    return full_name


def generate_place():
    global place, given_name, full_name
    copy_name_button.place(x=780, y=195)
    place_generate = random.choice(generation_dict)
    place = place_generate["Placenames"]
    entry.insert(END, f" from {place}")
    full_name = f"{str(given_name)} from {str(place)}"
    return full_name


def exit_game():
    window.quit()


def about():
    global canvas, state, about_text, canvas_id, entry, place_name_button, attribute_button
    entry.destroy()
    place_name_button.destroy()
    attribute_button.destroy()
    state = "about"
    canvas.itemconfig(background, image=about_bg)
    about_button.config(text="Menu", command=menu)
    generate_name_button.place(x=3000, y=3000)
    canvas_id = canvas.create_text(600, 240)
    canvas.itemconfig(canvas_id, text=info, width=780)
    canvas.itemconfig(canvas_id, font=("courier", 12, "bold"))
    canvas.insert(canvas_id, 12, "new ")
    #test_button.place(x=500, y=500)


def menu():
    global canvas, info, state, canvas_id, entry, place_name_button, attribute_button, generate_name_button
    entry = Entry(width=40)
    entry.place(x=530, y=200)
    about_text.destroy()
    canvas.delete(canvas_id)
    canvas.itemconfig(background, image=background_menu)
    about_button.config(text="About", command=about)
    #generate_name_button = Button(text="Generate name", command=generate_name)
    #generate_name_button.place(x=600, y=600)
    #generate_name_button = Button(text="Generate name", command=generate_name)
    generate_name_button.place(x=600, y=600)
    place_name_button = Button(text="Place", command=generate_place)
    attribute_button = Button(text="Attribute", command=generate_attribute)

def copy_clipboard():
    pyperclip.copy(full_name)
    messagebox.showinfo("Copy name", "The name has been copied to clipboard")


# ---------------------------UI------------------------#

window = Tk()
window.title("Name Generator")

# Background picture
canvas = Canvas(width=1280, height=720)
background_menu = PhotoImage(file="pictures/background.png")
background = canvas.create_image(640, 360, image=background_menu)
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)
canvas_id = canvas.create_text(600, 200)
given_name_text = canvas.create_text(600, 200)

about_bg = PhotoImage(file="pictures/background_gif.gif")


# music
mixer.init()
mixer.music.load("C:/Users/sleit/Music/No_More_Good_-_David_Fesliyan.mp3")
mixer.music.play(-1)

# Buttons
exit_button_image = PhotoImage(file="pictures/exit_game.png")
exit_button = Button(image=exit_button_image, command=exit_game)
exit_button.config(height=50, width=200)
exit_button.place(x=1050, y=650)

#about_button_image = PhotoImage(file="pictures/about_button.png")
about_button = Button(text="About", command=about)
about_button.place(x=1050, y=600)

#generate_name_image = PhotoImage(file="pictures/generate_name.png")
generate_name_button = Button(text="Generate Name", command=generate_name)
generate_name_button.place(x=600, y=600)

#place_name_image = PhotoImage(file="pictures/place_button.png")
place_name_button = Button(text="Place", command=generate_place)
attribute_button = Button(text="Attribute", command=generate_attribute)

copy_name_button = Button(text="Copy name", command=copy_clipboard)
#test_button = Button(text="text", command=reset_all)

entry = Entry(width=40)
#Add some text to begin with
entry.insert(END, string=given_name)
entry.place(x=530, y=200)


window.mainloop()