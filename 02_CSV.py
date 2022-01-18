import csv

#Datei anlegen
#Dateien a -> wenn vorhanden,öffnen und anfügen sonst neu
file1 = open("daten1.csv", "a")

#CSV Handler anlegen
writer = csv.writer(file1, delimiter=";")
writer.writerow([3, "Fritz", "Geier"])
file1.close()
