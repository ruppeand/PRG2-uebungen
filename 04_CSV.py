import csv

#Datei anlegen
file1 = open("daten1.csv", "r")

#CSV Handler anlegen
reader = csv.reader(file1, delimiter=";")

for row in reader:
    print(row[1])
file1.close()