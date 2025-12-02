wiederstand=float(0)
ampere=float(0)
spannung=float(0)
print("Diese program deint  zum Berechnung  vom Elektrishe Wiederstand")
spannung = float(input("Volt eingeben: ").replace(",","."))
ampere = float(input("Ampere eingeben: ").replace(",","."))
wiederstand = spannung/ampere
print(f"Der berechnete Widerstand beträgt ist {wiederstand}")
wiederstand = round(2)