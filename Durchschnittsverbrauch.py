
print("wie viel liter has du gettankt:") #liter
gettankt=float(input())
print("wie viel km hast du gefahren:")
gefahren=float(input())
ergebnis=(gettankt / gefahren *100)
ergebnis=round(ergebnis,2)
print(f"Durchschnittsverbrauch an Kraftstoff {ergebnis} L/100km")
