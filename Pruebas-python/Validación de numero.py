número= int(input("Introduzca el número: "))
if número <-100 or número >100:
    print("Número no válido.")
elif número ==0:
    print("Cero.")
elif número >0 and número %2==0:
    print("Positivo par.")
elif número >0 and número %2!=0:
    print("Positivo impar.")
elif número <0 and número %2==0:
    print("Negativo par.")
else:
    print("Negativo impar.")