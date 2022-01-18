#wir erstellen eine CSV Datei
import csv

#Datei anlegen
file1 = open("daten1.csv", "w")

#CSV Handler anlegen
writer = csv.writer(file1, delimiter=";")
writer.writerow(["ID", "vorname", "nachname"])
writer.writerow([1, "Max", "Meier"])
writer.writerow([2, "Hans", "Schmidt"])
file1.close()
