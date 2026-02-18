""" Schritt 001 """


# ----------------------------------------------------------------------
# 01. Ich initialisiere die Mutterklasse Buecherr;
# ----------------------------------------------------------------------
class Buecher:
    buecher_gesamnt = 0

    # ----------------------------------------------------------------------
    # 02. Ich initialisiere den Konstruktor der Mutterklasse, damit ich die Attribute für jedes Buch festlegen kann
    # ----------------------------------------------------------------------

    def __init__(self, titel, author, isbn):  # Der Konstruktor nimmt die wichtigsten Infos über das Buch entgegen,
        # damit wir sie später in der Bibliothek nutzen können

        self.titel = titel  # a. Wir werden ein Titel Attribut haben, damit wir wissen, wie das Buch heißt;
        self.author = author  # b. Wir werden ein Author Attribut haben, damit wir wissen, wer das Buch geschrieben hat;
        self.isbn = isbn  # c. Wir werden ein ISBN Attribut haben, damit wir wissen, welche ISBN das Buch hat;
        # ISBN ist eine eindeutige Nummer, die jedes Buch hat. Sowie ein Unique KEY in Datenbanken.
        self.ist_verliehen = False  # Anfangs ist das Buch verfügbar,also False, also noch nicht ausgeliehen;
        Buecher.buecher_gesamnt += 1  # Jedes Mal, wenn ein Buch erstellt wird, erhöhen wir den Zähler.
        # --> Aus 0 von anfang, werden wir haben 1, dann 2, etc!

    # ----------------------------------------------------------------------
    # 01 - Ich muss eine Methode verleihen() erstellen, damit ich ein Buch ausleihen kann, wenn es verfügbar ist,
    #     und eine Fehlermeldung bekomme, wenn es schon weg ist.
    # ----------------------------------------------------------------------

    def verleihen(self):
        if not self.ist_verliehen:
            self.ist_verliehen = True
            print(f"'{self.titel}' wurde verliehen.")
        else:
            print(f"'{self.titel}' ist bereits verliehen.")

    # def verleihen erkläre ich mir selbst:
    # - Diese Methode überprüft zuerst, ob das Buch bereits verliehen ist (also ob self.ausgeliehen == False).
    # - Wenn es verfügbar ist, wird der Status auf True gesetzt (jetzt ist es verliehen) und eine Erfolgsmeldung wird ausgegeben.
    # - Wenn es bereits verliehen ist, wird eine Fehlermeldung ausgegeben, die besagt, dass das Buch nicht verfügbar ist.

    # ----------------------------------------------------------------------
    # 02 - Ich muss eine Methode zur Verfügbarkeit erstellen, damit ich wissen kann, ob das Buch verfügbar ist oder nicht.
    # ----------------------------------------------------------------------

    # Nutze "__str__", damit wir ein Buch anschauen können, sonst würde es so aussehen: <__main__.Buecher object at 0x...>.
    def __str__(self):
        ist_verfuegbar = "JA" if not self.ist_verliehen else "NEIN"
        return f"{self.titel} | Verfügbar: {ist_verfuegbar}"


""" Schritt 002 """

# ----------------------------------------------------------------------
# 00 - Was ich bis jetzt habe:
# ist die Mutterklasse Buecher,
# die die grundlegenden Eigenschaften und Methoden für alle Bücher definiert.
# - Ich habe ein Attribut ausgeliehen und jetzt auch Methoden, um es zu ändern und anzuzeigen. Sehr wichtig.
# ----------------------------------------------------------------------

""" Schritt 003 """


# ----------------------------------------------------------------------
# 01 - Ich erstelle eine Unterklasse Roman, die von Buecher erbt, damit ich spezielle Eigenschaften für Romane hinzufügen kann.
# Zum Beispiel: Genre, wie Krimi, Liebesroman, etc.
# ----------------------------------------------------------------------

class Roman(Buecher):

    def __init__(self, titel, author, isbn, genre):
        super().__init__(titel, author, isbn)
        # super ist eine Funktion, die es uns ermöglicht, die Methoden und Eigenschaften
        # der Mutterklasse (Buecher) in der Unterklasse (Roman) zu verwenden.
        # Also damit rufen wir die Mutterklasse (Buecher) auf und sagen einfach" Mach die standard Arbeit
        # wie (Titel,Autor,Isbn) und denn rest mache ich, also ich kümmere mich um das Genre später.
        self.genre = genre


""" Schritt 004 """


# ----------------------------------------------------------------------
# 01 - Ich brauche einen Ort, der die Liste aller Bücher verwalten kann,
# damit ich Bücher hinzufügen, entfernen und suchen kann.
# ----------------------------------------------------------------------


class Buecherei:  # Warum diese Verwaltungsklasse? Weil ich eine zentrale Stelle brauche, um alle Bücher zu verwalten.
    def __init__(self, name):
        self.name = name
        self.alle_buecher = []  # Hier werde ich alle Buch-Objekte speichern, die zur Bibliothek gehören.
        #  Im moment ist es eine leere Liste, aber ich werde später Methoden hinzufügen,
        #  um Bücher hinzuzufügen und zu entfernen.
        # !!!! Also das ist jetzt mein Regal,leer, wo ich später die Bücher reinlegen werde.

    """ Schritt 005 """

    # ----------------------------------------------------------------------
    # 01 - Ich erstelle eine Methode buch_hinzufuegen(), damit ich neue Bücher zur Bibliothek hinzufügen kann.
    # ----------------------------------------------------------------------

    def buch_hinzufuegen(self, neues_buch):
        self.alle_buecher.append(neues_buch)  # append nimmt ein fertiges Buch Objekt und schiebt es in unsrere Liste.


""" Schritt 006 """

# ----------------------------------------------------------------------
# 01 - Ich teste es alles aus, damit ich sicher sein kann, dass es funktioniert.
# ----------------------------------------------------------------------

# 1. Erstelle eine Bibliothek ODER eine Bibliothek gründen, damit ich einen Ort habe, um meine Bücher zu verwalten.
meine_buech = Buecherei("Dorfbuecherei")

# 2. Erstelle ein paar Bücher, damit ich etwas zum Verwalten habe.
buch1 = Buecher("Der Alchimist", "Paulo Coelho", "978-0061122415")
buch2 = Roman("Der Name der Rose", "Umberto Eco", "978-0156001311", "Krimi")
buch3 = Buecher("Sapiens", "Yuval Noah Harari", "978-0062316097")

# 3. Diese Bücher müssen in die Bibliothek stehen, also in das Leere Regal von oben, damit ich sie später verwalten kann.

meine_buech.buch_hinzufuegen(buch1)
meine_buech.buch_hinzufuegen(buch2)
meine_buech.buch_hinzufuegen(buch3)

# 4. Ich kann irgend eine oder alle Bücher ausleihen, mit meine methode verleihen(),
#    damit ich testen kann, ob die Methode funktioniert.

buch1.verleihen()  # Ich leihe das erste Buch aus, mit meine Methode von oben, damit ich testen kann, ob es funktioniert.
buch2.verleihen()
# 5. Ich kontrolliere die Verfügbarkeit von buch1, damit ich sehen kann, ob es wirklich verliehen ist.

print(buch1)
print(buch2)
print(buch3)
