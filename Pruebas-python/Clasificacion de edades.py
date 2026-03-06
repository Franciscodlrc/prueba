edad= int(input("Introduzca su edad: "))
if edad <0 or edad >120:
    print("Edad no válida.")
elif edad >=0 and edad <=11:
    print("Niño.")
elif edad >=12 and edad <=17:
    print("Adolescente.")
elif edad >=18 and edad <=64:
    print("Adulto.")
else:
    print("Senior.")