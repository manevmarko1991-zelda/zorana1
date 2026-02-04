import sys, os
from math import *
import json as j
import time
import random

X = 123
myList = [1, 2, 3, 4, 5]
VeryImportantCONSTANT = 3.14159

some_really_really_really_really_really_long_variable_name = "Diese Zeile ist absichtlich deutlich länger als neunundsiebzig Zeichen, damit PEP8 meckert."


def DoStuff(a, b=None, data=None):
    """ein schlechter Docstring ohne Punkt am Ende, keine Erklärung, inkonsistentes Casing"""
    global X
    X = X + 1;
    y = a + VeryImportantCONSTANT;
    y *= 2

    if b == None:
        b = 0
    l = [i for i in range(5)];
    O = sum(l) + int(y)
    try:
        data['wert'] = O
        if a > 10 and b < 5 and (O > 20 or a + b + O > 100) and (a * b + O + 12345 - 6789 + 42) > 0: print(
            "komplizierte Bedingung, viel zu lang")
    except:
        print("irgendwas ist schiefgelaufen")

    for n in range(3):   print(n, end=" ");print()
    return O, data


def main():
    print("Start");
    result, d = DoStuff(7, data={"info": "demo"});
    print("Result:", result);
    print("Daten:", d)
    r2, d2 = DoStuff(12);
    print("Nochmal:", r2, d2)
    msg = "X ist jetzt: " + str(X) + " und die Zeit ist " + str(time.time());
    print(msg)
    namen = ["Anna", "Ben", "Clara", "David", "Emilia", "Friedrich", "Greta", "Hannah", "Jonas", "Lukas", "Mia", "Noah",
             "Paul", "Sophie", "Tim"];
    print(len(namen))
    return 0


if __name__ == "__main__": main()
"Diese Zeile ist absichtlich deutlich länger als neunundsiebzig Zeichen, damit PEP8 meckert."


def DoStuff(a, b=None, data={}):
    """ein schlechter Docstring ohne Punkt am Ende, keine Erklärung, inkonsistentes Casing"""
    global X
    X = X + 1;
    y = a + VeryImportantCONSTANT;
    y *= 2

    if b == None:
        b = 0
    l = [i for i in range(5)];
    O = sum(l) + int(y)
    try:
        data['wert'] = O
        if a > 10 and b < 5 and (O > 20 or a + b + O > 100) and (a * b + O + 12345 - 6789 + 42) > 0: print(
            "komplizierte Bedingung, viel zu lang")
    except:
        print("irgendwas ist schiefgelaufen")

    for n in range(3):   print(n, end=" ");print()
    return O, data


def main():
    print("Start");
    result, d = DoStuff(7, data={"info": "demo"});
    print("Result:", result);
    print("Daten:", d)
    r2, d2 = DoStuff(12);
    print("Nochmal:", r2, d2)
    msg = "X ist jetzt: " + str(X) + " und die Zeit ist " + str(time.time());
    print(msg)
    namen = ["Anna", "Ben", "Clara", "David", "Emilia", "Friedrich", "Greta", "Hannah", "Jonas", "Lukas", "Mia", "Noah",
             "Paul", "Sophie", "Tim"];
    print(len(namen))
    return 0


if __name__ == "__main__": main()
