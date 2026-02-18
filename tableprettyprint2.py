def prettyTablePrint(data):
    # Spaltenbreiten berechnen
    #print([0] * 5)

    col_widths = [0] * len(data[0])

    for row in data:
        for i, cell in enumerate(row):
            #print(i, cell, len(str(cell)))
            cell_length = len(str(cell))
            col_widths[i] = max(col_widths[i], cell_length)
    print("Col_Widths", col_widths)

    # Trennlinie definieren
    dashes = []
    for width in col_widths:
        dashes.append('-' * width)
    print(dashes)
    separator_parts = ['-+-'.join(dashes)]
    print(separator_parts)
    separator = '+-' + separator_parts[0] + '-+'

    def format_row(row):
        formatted_cells = []
        for i in range(len(row)):
            # Zelle aus der Zeile holen
            cell = row[i]
            # Breite aus den Spaltenbreiten holen
            width = col_widths[i]
            # Zelle in einen String konvertieren
            cell_str = str(cell)
            # Den formatierten Zellenstring erstellen
            formatted_cell = f'{cell_str:<{width}}'
            #print(formatted_cell)
            # Den formatierten Zellenstring zur Liste der formatierten Zellen hinzufügen
            formatted_cells.append(formatted_cell)
        row_string = ' | '.join(formatted_cells)
        return '| ' + row_string + ' |'

    print(separator)
    print(format_row(data[0]))
    print(separator)
    for row in data[1:]:
        print(format_row(row))
    print(separator)

# Test der Funktion mit den gegebenen Daten
data = [
    ["Name", "Alter", "Beruf", "Wohnort"],
    ["Max", 28, "Ingenieur", "Darmstadt"],
    ["Anna", 22, "Studentin", "Stuttgart"],
    ["Hans", 34, "Lehrer", "München"],
    ["Mike", 77, "Fachinformatiker", "Hannover"],
    ["Hans-Peter", 50, "Gas und Wasserinstallateur", "HamburgBerlinStuttgartMuenchenRavensburgGoettingenSchweizFranqfurtnfgfzretrue"]
]
prettyTablePrint(data)
'''
import csv

# Öffnen der Datei im Lese-Modus ('r')
with open('gemuese_eigen.csv', 'r', encoding='utf-8') as file:
    # Erstellen Sie einen CSV-Reader
    reader = list(csv.reader(file))
    # print(reader)

prettyTablePrint(reader)
'''