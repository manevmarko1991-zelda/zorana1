import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.config(bg="slateBlue1")
root.title("Hallo Welt Aufgabe")

def change():
    label.config(text="Wurde geklickt!")

label = tk.Label(
    root,
    text="Hallo Welt!",
    bg="slateBlue1",
    fg="black",
    font=("Courier", 30, "bold")
)
label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

button = tk.Button(
    root,
    text="Klick mich!",
    bg="black",
    fg="slateBlue1",
    font=("Courier", 20, "bold"),
    command=change
)
button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

root.mainloop()
