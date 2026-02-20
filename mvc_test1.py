class FerienhausDatenzugriffsschicht:
class FerienhausGeschaeftslogikSchicht:
class FerienhausPraesentationsSchicht(bll)





















if __name__ == "__main__":
    # Initialisierung der Schichten
    dal = FerienhausDatenzugriffsschicht()
    bll = FerienhausGeschaeftslogikSchicht(dal)
    pl = FerienhausPraesentationsSchicht(bll)

    # Start der Benutzerschnittstelle2

    pl.benutzereingabe_verarbeiten()