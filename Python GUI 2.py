import tkinter as tk

root = tk.Tk()
root.title("Formular")
root.geometry("680x420")


#Frame für die Nutzereingabe
frame = tk.LabelFrame(root, text="Name:", pady=5, padx=10)
frame.pack(fill="x")
eingabe = tk.Entry(frame, font=("Arial", 16), fg="red")
eingabe.pack(side="left", fill="x", expand=True)

#Frame für Geschlecht
nocheinframe= tk.LabelFrame(root, text="Geschlecht")
nocheinframe.pack(fill="x")
#LabelFrame erlaubt ein Beschriftungslabel oben links in der Ecke

#Erstellen einer Variable, um den Wert der verschiedenen Buttons zu speichern
auswahl = tk.StringVar(value="Keine Angabe")
#Wir vergeben einen default Wert

#Radiobuttons erlauben immer nur eine Auswahl, also ein klassisches ODER

radiobtn = tk.Radiobutton(nocheinframe, text="männlich", value="männlich", variable=auswahl)
#variable gibt den "Speicherort" an, also in welcher Variablen
# soll das Ergebnis gespeichert werden
radiobtn.pack(side="left")
radiobtn2 = tk.Radiobutton(nocheinframe, text="weiblich", value="weiblich", variable=auswahl)
radiobtn2.pack(side="left")
radiobtn3 = tk.Radiobutton(nocheinframe, text="divers", value="divers", variable=auswahl)
radiobtn3.pack(side="left")

#Frame für Hobbys
dannnocheiner = tk.LabelFrame(root, text="Hobbys", padx=10, pady=5)
dannnocheiner.pack(fill="x")

#Checkbuttons erlauben mehrere Auswahlmöglichkeiten gleichzeitig
chckbtn1 = tk.Checkbutton(dannnocheiner, text="Hobbyhorsing")
chckbtn1.pack(side="left")
chckbtn2 = tk.Checkbutton(dannnocheiner, text="Zocken")
chckbtn2.pack(side="left")
chckbtn3 = tk.Checkbutton(dannnocheiner, text="Schlafen")
chckbtn3.pack(side="left")
chckbtn4 = tk.Checkbutton(dannnocheiner, text="repeat")
chckbtn4.pack(side="left")

#Frame für Zufriedenheit
#Erste Idee: 10 Radiobuttons für eine Skala von 1 bis 10
#Das wird bei größeren Skalen schwierig
#Und es gibt eine Skala in tkinter!

einweitererframe = tk.LabelFrame(root, pady=5, padx=10, text="Zufriedenheit:")
einweitererframe.pack(fill="x")

#Scale erzeugt eine einfache Skala,
#default ist die Ausrichtung vertikal und geht von 0 (oben) bis 100 (unten)
skala = tk.Scale(einweitererframe, from_=1, to=10, orient="horizontal")
skala.set(5)
skala.pack(side="left", fill="x", expand=True)

#Frame für Kommentare
#Kommentare sind meist länger, als eine Zeile
#tk.Entry() erlaubt nur eine Zeile, wir brauchen aber mehr!
letzterframe = tk.LabelFrame(root, pady=5, padx=10, text = "Kommentar:")
letzterframe.pack(fill="both", expand=True)

#Um mehrere Zeilen Eingabe zu erlauben, nutzen wir tk.Text()
kommentare = tk.Text(letzterframe, height=4, font=("Arial", 16))
kommentare.pack(fill="both", expand=True)


#Skizze für die Ausgabe

#Namen abspeichern
name= eingabe.get()

#Geschlecht abspeichern
geschlecht = auswahl.get()

#Zufriedenheit abspeichern
zufriedenheit = skala.get()

#Kommentar abspeichern
kommentar = kommentare.get("1.0", tk.END).strip()
#Bei Textfeldern mit mehreren Zeilen muss .get() mit den Start und Endwert
#erweitert werden. "1.0" gibt den Startpunkt an, tk.END wieder das Ende
#.strip() entfernt Steuerzeichen wie Zeilenumbrüche

root.mainloop()
TXT Dateien Python GUI
Feiberg, Roman - DAA<Roman.Feiberg@daa.de>
​Feiberg, Roman - DAA <Roman.Feiberg@daa.de>​
Hallo liebe Teilnehmer,



anbei die .txt-Dateien für Python GUI.



Beste Grüße



Roman Feiberg



DAA Deutsche Angestellten-Akademie GmbH
Geschäftsführung: Dr. Tina Jessica Classen
Sitz der Gesellschaft: Hamburg, HRB 81257

Die Deutsche Angestellten-Akademie ist ein gemeinnütziger, bundesweit tätiger und zertifizierter Träger beruflicher Bildung.
Informationen zum Bildungsangebot der DAA finden Sie unter www.daa.de