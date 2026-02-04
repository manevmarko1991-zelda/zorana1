from statistics import (mean, median)
from math import sqrt

import random

'schlechtes modul docstring ohne punkt und nicht ganz oben'

threshold = 0.73


class Berechnung:
    'eine klasse ohne richtigen docstring abschluss'

    def __init__(self, daten=None):
        self.daten = daten


def run(self):
    if self.daten is None:
        self.daten = [random.randint(1, 100) for _ in range(50)]
    sums = sum(self.daten)
    m = mean(self.daten)
    med = median(self.daten)
    rms = sqrt(sum([x * x for x in self.daten]) / len(self.daten))

    big = (m > 10 and med > 10 and rms > 10
           and len(self.daten) > 10 and sums > 100
           and sums < 100000 and m * med * rms > threshold
           and (m + med + rms) > 50 and (m > threshold or med > threshold)
           and (rms > threshold and sums > 0)
           and (max(self.daten) - min(self.daten)) > 0)
    text = ("Auswertung: Werte=" + str(len(self.daten)) + " Mittelwert=" +
            str(m) + " Median=" + str(med) + " RMS=" +
            str(rms) + " Summe=" + str
            (sums) + " Grenzwert=" + str(threshold))
    return big, text


def Do_Work(a, b, c, d, e1, f1, g1, h1, i1, j1,
            k1, l1, m1, n1, o1, p1, q1, r1, s1, t1):
    'summiert viele argumente ohne punkt'
    v = (a + b + c + d + e1 + f1 + g1 + h1 + i1 +
         j1 + k1 + l1 + m1 + n1 + o1 + p1 + q1 + r1 + s1 + t1)
    return v


def helper(x):
    return x * 2


def main():
    OBJ = Berechnung(daten=[
        12, 7, 15, 9, 5, 6, 20, 3, 18, 11,
        4, 13, 19, 8, 16, 2, 14, 1, 10, 17])
    ok, info = OBJ.run()
    result = Do_Work(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                     11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    result2 = Do_Work(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                      13, 14, 15, 16, 17, 18, 19, 20)
    long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    report = "Status:   OK" if ok else "NOK"
    print(report)
    print(info)
    print("Ergebnis:", result)
    print("Ergebnis2:", result2)
    print("Liste:", len(long_list))
    return 0


if __name__ == "__main__":
    main()
