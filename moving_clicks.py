# import tkinter and give it the short name "tk"
# tkinter is used to build windows (GUI)
import tkinter as tk

# import messagebox for popup windows (yes / no)
from tkinter import messagebox

# import random to create random positions for the button
import random


# -------------------------------
# MAIN WINDOW (root)
# -------------------------------

# create the main window
root = tk.Tk()

# set the window size to 720x420 pixels
root.geometry("720x420")

# set background color of the window
root.config(background="red")

# set the window title
root.title("Meine erste App!")


# -------------------------------
# GLOBAL VARIABLES
# -------------------------------
# these variables remember the state of the program

count = 0          # how many times the button was clicked
timer_id = None    # stores the timer so we can stop it later
running = False    # tells us if the timer is already running
groesse = 20       # base font size of the button text
zaehler = 0        # counter used to make the font smaller


# -------------------------------
# FUNCTION: CLICK
# -------------------------------
# this function runs when the user clicks the button

def click():
    # we want to change global variables
    global count, groesse, zaehler

    # increase click counter by 1
    count += 1

    # update the label text with the new count
    label.config(text=f"Klicks: {count}")

    # start or restart the timer (button moves)
    timer()

    # if clicks are more than 25
    # then the button text becomes smaller
    if count > 25:
        button.config(font=("Arial", groesse - zaehler))
        zaehler += 1   # make it even smaller next time


# -------------------------------
# FUNCTION: TIMER
# -------------------------------
# this function moves the button again and again

def timer():
    global timer_id, running, count

    # if timer was not running before, mark it as running
    if not running:
        running = True

    # move the button to a random position
    # random.random() gives a number between 0 and 1
    button.place(relx=random.random(), rely=random.random())

    # if a timer already exists, cancel it
    # this prevents multiple timers running at the same time
    if timer_id:
        root.after_cancel(timer_id)

    # if click count is less than 40
    # make the button move faster and faster
    if count < 40:
        timer_id = root.after(2000 - (count * count), timer)
    else:
        # after 40 clicks, move every 300 ms
        timer_id = root.after(300, timer)


# -------------------------------
# FUNCTION: RESET
# -------------------------------
# resets everything to the starting state

def reset():
    global count, zaehler, running, timer_id

    # reset click counter
    count = 0

    # update label text
    label.config(text="Klicks: 0")

    # reset button font size
    button.config(font=("Arial", 20))

    # move button back to the center
    button.place(relx=0.5, rely=0.6)

    # reset helper variables
    zaehler = 0
    running = False

    # stop the timer if it exists
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None


# -------------------------------
# FUNCTION: BEENDEN (EXIT)
# -------------------------------
# asks the user if they really want to quit

def beenden():
    # show yes/no popup window
    if messagebox.askyesno("Beenden", "Sind Sie sicher?"):
        # close the window and stop the program
        root.destroy()


# -------------------------------
# LABEL (TEXT DISPLAY)
# -------------------------------

# create a label that shows the click count
label = tk.Label(
    root,                     # parent window
    text="Klicks: 0",          # label text
    background="white",        # background color
    foreground="black",        # text color
    font=("Arial", 20)         # font style and size
)

# place the label in the window (center top)
label.place(relx=0.5, rely=0.2, anchor="center")


# -------------------------------
# MAIN BUTTON
# -------------------------------

# create the main button
button = tk.Button(
    root,                     # parent window
    text="Klick Mich!",        # button text
    bg="white",                # background color
    fg="black",                # text color
    font=("Arial", 20),        # font
    command=click,             # function called on click
    activebackground="purple"  # color while clicking
)

# place the button in the window
button.place(relx=0.5, rely=0.6, anchor="center")


# -------------------------------
# RESET BUTTON
# -------------------------------

reset_button = tk.Button(
    root,
    text="Reset",
    bg="white",
    fg="black",
    command=reset,
    activebackground="red"
)

# bottom-left corner
reset_button.place(relx=0.01, rely=0.9)


# -------------------------------
# EXIT BUTTON
# -------------------------------

beenden_button = tk.Button(
    root,
    text="Beenden",
    bg="white",
    fg="black",
    command=beenden,
    activebackground="green"
)

# bottom-right corner
beenden_button.place(relx=0.91, rely=0.9)


# -------------------------------
# START THE PROGRAM
# -------------------------------

# this keeps the window open
# and listens for user actions (clicks, buttons, etc.)
root.mainloop()
