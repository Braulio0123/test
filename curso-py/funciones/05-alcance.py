saludo = "Hola global"

def saludar():
    global saludo
    saludo = "Hola a todos"

def saludoPer():
    saludacion = "Saludos persona"
    print(saludacion)

print(saludo)
saludar()
print(saludo)
# saludoPer()