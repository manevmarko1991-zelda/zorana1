
"""PEP-8-konforme Auswertung einer Zahlenliste mit Statistik-Kennzahlen."""

from statistics import mean, median
from math import sqrt
import random
import time


THRESHOLD = 0.73


class Calculation:
    """Berechnet Kenngrößen und fasst die Auswertung zusammen."""

    def __init__(self, data=None):
        """Initialisiert die Berechnung mit Daten oder Zufallswerten.

        Wenn keine Daten übergeben werden, erzeugt die Klasse eine
        Zufallsliste für die Auswertung.
        """
        self.data = data

    def run(self):
        """Berechnet Summe, Mittelwert, Median und RMS.

        Erstellt anschließend einen Bericht.

        Returns:
            tuple[bool, str]: (Bedingung erfüllt?, Textreport)
        """
        if self.data is None:
            self.data = [random.randint(1, 100) for _ in range(50)]

        total = sum(self.data)
        avg = mean(self.data)
        med = median(self.data)
        rms = sqrt(sum(x * x for x in self.data) / len(self.data))

        condition = (
            avg > 10
            and med > 10
            and rms > 10
            and len(self.data) > 10
            and 100 < total < 100_000
            and (avg * med * rms) > THRESHOLD
            and (avg + med + rms) > 50
            and (avg > THRESHOLD or med > THRESHOLD)
            and rms > THRESHOLD
            and (max(self.data) - min(self.data)) > 0
        )

        report = (
            "Auswertung: "
            f"Werte={len(self.data)} "
            f"Mittelwert={avg:.2f} "
            f"Median={med:.2f} "
            f"RMS={rms:.2f} "
            f"Summe={total} "
            f"Grenzwert={THRESHOLD}"
        )
        return condition, report


def sum_many(
    a, b, c, d, e1, f1, g1, h1, i1, j1,
    k1, l1, m1, n1, o1, p1, q1, r1, s1, t1,
):
    """Summiert viele übergebene Argumente und gibt das Ergebnis zurück."""
    values = (
        a, b, c, d, e1, f1, g1, h1, i1, j1,
        k1, l1, m1, n1, o1, p1, q1, r1, s1, t1,
    )
    return sum(values)


def double(x):
    """Verdoppelt den übergebenen Wert."""
    return x * 2


def main():
    """Startpunkt der kleinen Demo."""
    numbers = [
        12, 7, 15, 9, 5, 6, 20, 3, 18, 11,
        4, 13, 19, 8, 16, 2, 14, 1, 10, 17,
    ]

    calc = Calculation(data=numbers)
    ok, info = calc.run()

    result = sum_many(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
    )

    doubled = [double(x) for x in numbers]

    print(info)
    print("Bedingung erfüllt?:", ok)
    print("Summe vieler Werte:", result)
    print("Verdoppelte erste fünf:", doubled[:5])
    print(f"Aktueller Zeitstempel: {time.time():.0f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
