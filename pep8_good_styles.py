
"""PEP-8-konforme Demo mit klaren Funktionen und sauberem Stil.

Diese Datei ist die bereinigte Version des vorherigen Beispiels.
"""

import time



PI = 3.14159  # Konstante in Großbuchstaben


def do_stuff(a, b=None, data=None):
    """Berechnet einen Beispielwert und erweitert das übergebene Dictionary.

    Args:
        a (int | float): Erster Eingabewert.
        b (int | float | None): Optionaler Wert. Falls None → wird 0 verwendet.
        data (dict | None): Optionales Dictionary mit Informationen.

    Returns:
        tuple: (berechneter_wert, aktualisiertes_dict)
    """
    if data is None:
        data = {}

    if b is None:
        b = 0

    y = (a + PI) * 2

    werte_liste = [i for i in range(5)]
    ergebnis = sum(werte_liste) + int(y)

    try:
        data["wert"] = ergebnis

        if (
                a > 10
                and b < 5
                and (ergebnis > 20 or a + b + ergebnis > 100)
                and ((a * b) + ergebnis + 12345 - 6789 + 42) > 0
        ):
            print("Bedingung erfüllt.")
    except Exception as exc:
        print(f"Fehler aufgetreten: {exc}")

    for n in range(3):
        print(n, end=" ")
    print()

    return ergebnis, data


def main():
    """Hauptprogramm der Demo."""
    print("Start")

    result, info = do_stuff(7, data={"info": "demo"})
    print("Result:", result)
    print("Daten:", info)

    result2, info2 = do_stuff(12)
    print("Nochmal:", result2, info2)

    msg = (
        f"Aktueller Zeitstempel: {time.time()}, "
        f"berechneter Wert: {result2}"
    )
    print(msg)

    namen = [
        "Anna", "Ben", "Clara", "David", "Emilia",
        "Friedrich", "Greta", "Hannah", "Jonas",
        "Lukas", "Mia", "Noah", "Paul", "Sophie", "Tim",
    ]
    print("Anzahl Namen:", len(namen))

    return 0


if __name__ == "__main__":
    main()
