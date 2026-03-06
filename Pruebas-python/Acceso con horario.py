hora= int(input("Introduzca la hora: "))
if hora <0 or hora >23:
    print("Hora no válida.")
elif hora >=6 and hora <=11:
    print("Buenos días.")
elif hora >=12 and hora <=19:
    print("Buenas tardes.")
elif hora >=20 and hora <=23:
    print("Buenas noches.")
else:
    print("Buenas noches.")