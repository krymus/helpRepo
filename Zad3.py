import openpyxl
import shelve


workbook = openpyxl.load_workbook("tabliczka.xlsx")
sheet = workbook.active

listaB = []
krotkaC = ()
dictDE = {}

#odczytywanie wartosci w kazdym wierszu
for row in sheet.iter_rows(min_row=2, values_only=True):
    listaB.append(row[1])
    krotkaC += (row[2],)
    dictDE[row[3]] = row[4]

workbook.close()


#zapisywanie
with shelve.open("data") as shelf:
    shelf['listaB'] = listaB
    shelf['krotkaC'] = krotkaC
    shelf['dictDE'] = dictDE


#odczytywanie
with shelve.open("data") as shelf:
    listaB = shelf['listaB']
    krotkaC = shelf['krotkaC']
    dictDE = shelf['dictDE']

#wyswietlanie
print("Lista B:", listaB)
print("Krotka C:", krotkaC)
print("Dictionary DE:", dictDE)
