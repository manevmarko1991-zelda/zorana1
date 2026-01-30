import tkinter as tk
from tkinter import messagebox

#Hauptfenster
root = tk.Tk()
#Erzeugt ein Fenster mit dem Namen root
#= tk. => Aufruf der Bibliothek tkinter
#.Tk() => Auf für das Hauptfenster (so heißt die Klasse)

root.geometry("720x420")        #Startgröße des Fensters
root.config(bg="darkgrey")      #Farbe des Hintergrunds (bg = background) festlegen
root.title("Meine erste App")   #Titel/Name des Fensters festlegen
#root.resizable(False, False)



#Funktion zum Zählen
count=0
def click():
    global count
    count += 1
    label.config(text=f"Klicks: {count}")

def ende():
    if messagebox.askyesno("Beenden?", "Programm wirklich beenden?"):
        root.destroy()

#Widgets
label = tk.Label(root, text="Klicks: 0", bg="grey")
#label => Name / Bezeichner
#tk.Label => Klasse aus tkinter - Schriftzug (Preisschild / Etikettiergerät)
#root => Verweis auf das Elternobjekt (Hauptfenster)
#text => Was soll auf unserem Schriftzug stehen?!
#bg => background Farbe
#fg => forground Farbe
#font ("Arial", 16) => Schriftart und Schriftgröße festlegen

#Platzieren des Labels - 3 Möglichkeiten
#pack = Automatisch
#place = Pixelgenau platzieren
#grid = Raster (Zeilen / Spalten - Anlehnung an Excel)

#label.pack(pady=100)
#label.place(x=335, y=205)
label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)



#Knopf zum Klicken

button = tk.Button(root, text="Klick Mich!", bg="black", fg="#ffffff", command=click)
#button => Name/Bezeichner
#tk.Button => Klasse aus tkinter
#root => Elternobjekt (Verweis, wo der Button erscheinen soll)

button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


#Knopf zum Beenden

beenden = tk.Button(root, text="Beenden", command=ende)
beenden.place(relx=0.1, rely=0.9, anchor=tk.CENTER)



root.mainloop()
