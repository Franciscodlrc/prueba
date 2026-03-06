login = input("Introduzca usuario: ")
password = input("introduzca contraseña: ")
if login== "admin" and password == "1234":
    print("Reconocido usuario administrador.")
elif login== "invitado":
    print("Reconocido invitado, bienvenido." )
else:
    print("Usuario o contraseña no reconocidos.")