# Datenschicht
class FerienhausDatenzugriffsschicht:
    def __init__(self):
        self.ferienhaeuser = {}

    def ferienhaus_hinzufuegen(self, haus_id, haus_daten):
        self.ferienhaeuser[haus_id] = haus_daten

    def ferienhaus_abrufen(self, haus_id):
        return self.ferienhaeuser.get(haus_id, None)

    def ferienhaus_aktualisieren(self, haus_id, haus_daten):
        self.ferienhaeuser[haus_id] = haus_daten

    def alle_ferienhaeuser_auflisten(self):
        return self.ferienhaeuser.values()


# Logikschicht
class FerienhausGeschaeftslogikSchicht:
    def __init__(self, daten_zugriffsschicht):
        self.daten_zugriffsschicht = daten_zugriffsschicht

    def neues_ferienhaus_hinzufuegen(self, haus_id, name, ort, preis_pro_nacht, kapazitaet):
        if self.daten_zugriffsschicht.ferienhaus_abrufen(haus_id) is None:
            haus_daten = {
                'id': haus_id,
                'name': name,
                'ort': ort,
                'preis_pro_nacht': preis_pro_nacht,
                'kapazitaet': kapazitaet,
                'verfuegbarkeit': True
            }
            self.daten_zugriffsschicht.ferienhaus_hinzufuegen(haus_id, haus_daten)
            return True
        else:
            return False

    def ferienhaus_suchen(self, haus_id):
        return self.daten_zugriffsschicht.ferienhaus_abrufen(haus_id)

    def ferienhaus_buchen(self, haus_id):
        haus = self.daten_zugriffsschicht.ferienhaus_abrufen(haus_id)
        if haus and haus['verfuegbarkeit']:
            haus['verfuegbarkeit'] = False
            self.daten_zugriffsschicht.ferienhaus_aktualisieren(haus_id, haus)
            return True
        else:
            return False

    def ferienhaus_stornieren(self, haus_id):
        haus = self.daten_zugriffsschicht.ferienhaus_abrufen(haus_id)
        if haus and not haus['verfuegbarkeit']:
            haus['verfuegbarkeit'] = True
            self.daten_zugriffsschicht.ferienhaus_aktualisieren(haus_id, haus)
            return True
        else:
            return False

    def alle_ferienhaeuser_abrufen(self):
        return self.daten_zugriffsschicht.alle_ferienhaeuser_auflisten()


# Präsentationsschicht
class FerienhausPraesentationsSchicht:
    def __init__(self, geschaeftslogik_schicht):
        self.geschaeftslogik_schicht = geschaeftslogik_schicht

    def menue_anzeigen(self):
        print("\nFerienhaus-Vermietungssystem")
        print("1. Ferienhaus hinzufügen")
        print("2. Ferienhaus suchen")
        print("3. Ferienhaus buchen")
        print("4. Ferienhaus stornieren")
        print("5. Alle Ferienhäuser auflisten")
        print("6. Beenden")

    def benutzereingabe_verarbeiten(self):
        while True:
            self.menue_anzeigen()
            wahl = input("Bitte wählen Sie eine Option: ")

            if wahl == "1":
                self.ferienhaus_hinzufuegen_schnittstelle()
            elif wahl == "2":
                self.ferienhaus_suchen_schnittstelle()
            elif wahl == "3":
                self.ferienhaus_buchen_schnittstelle()
            elif wahl == "4":
                self.ferienhaus_stornieren_schnittstelle()
            elif wahl == "5":
                self.alle_ferienhaeuser_auflisten_schnittstelle()
            elif wahl == "6":
                print("Programm wird beendet...")
                break
            else:
                print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

    def ferienhaus_hinzufuegen_schnittstelle(self):
        haus_id = input("Geben Sie die Ferienhaus-ID ein: ")
        name = input("Geben Sie den Namen des Ferienhauses ein: ")
        ort = input("Geben Sie den Ort des Ferienhauses ein: ")
        preis_pro_nacht = float(input("Geben Sie den Preis pro Nacht ein: "))
        kapazitaet = int(input("Geben Sie die Kapazität (Anzahl der Personen) ein: "))

        if self.geschaeftslogik_schicht.neues_ferienhaus_hinzufuegen(haus_id, name, ort, preis_pro_nacht, kapazitaet):
            print(f"Ferienhaus '{name}' erfolgreich hinzugefügt.")
        else:
            print(f"Ferienhaus mit ID '{haus_id}' existiert bereits.")

    def ferienhaus_suchen_schnittstelle(self):
        haus_id = input("Geben Sie die Ferienhaus-ID ein: ")
        haus = self.geschaeftslogik_schicht.ferienhaus_suchen(haus_id)
        if haus:
            verfuegbarkeit = "Ja" if haus['verfuegbarkeit'] else "Nein"
            print(
                f"Ferienhaus gefunden: {haus['name']} in {haus['ort']} - Preis pro Nacht: {haus['preis_pro_nacht']}€ - Verfügbar: {verfuegbarkeit}")
        else:
            print(f"Kein Ferienhaus mit der ID '{haus_id}' gefunden.")

    def ferienhaus_buchen_schnittstelle(self):
        haus_id = input("Geben Sie die Ferienhaus-ID ein, um es zu buchen: ")
        if self.geschaeftslogik_schicht.ferienhaus_buchen(haus_id):
            print(f"Ferienhaus mit der ID '{haus_id}' erfolgreich gebucht.")
        else:
            print(f"Ferienhaus mit der ID '{haus_id}' ist nicht verfügbar oder existiert nicht.")

    def ferienhaus_stornieren_schnittstelle(self):
        haus_id = input("Geben Sie die Ferienhaus-ID ein, um die Buchung zu stornieren: ")
        if self.geschaeftslogik_schicht.ferienhaus_stornieren(haus_id):
            print(f"Buchung für Ferienhaus mit der ID '{haus_id}' erfolgreich storniert.")
        else:
            print(f"Ferienhaus mit der ID '{haus_id}' existiert nicht oder ist bereits verfügbar.")

    def alle_ferienhaeuser_auflisten_schnittstelle(self):
        haeuser = self.geschaeftslogik_schicht.alle_ferienhaeuser_abrufen()
        print("Ferienhäuser in der Datenbank:")
        for haus in haeuser:
            verfuegbarkeit = "Ja" if haus['verfuegbarkeit'] else "Nein"
            print(
                f"{haus['id']}: {haus['name']} in {haus['ort']} - Preis pro Nacht: {haus['preis_pro_nacht']}€ - Verfügbar: {verfuegbarkeit}")


# Hauptprogramm
if __name__ == "__main__":
    # Initialisierung der Schichten
    dal = FerienhausDatenzugriffsschicht()
    bll = FerienhausGeschaeftslogikSchicht(dal)
    pl = FerienhausPraesentationsSchicht(bll)

    # Start der Benutzerschnittstelle2

    pl.benutzereingabe_verarbeiten()

