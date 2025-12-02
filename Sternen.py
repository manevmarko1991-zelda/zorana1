SternListe= ["*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"]

Sternenstaub = 2


while "*" in SternListe:

    for i in SternListe:

        print(i, end="")

    print()

    for _ in range(Sternenstaub):

     if "*" in SternListe:

        ersetzen = SternListe.index("*")

        SternListe[ersetzen]=" "

        SternListe.pop(0)