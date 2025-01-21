# def saludo(valor):
#     return "Hola, " + valor
# print(saludo("Peter"))

def saludo(nombre, apellido):
    return f"Hola, {nombre} {apellido}"
print(saludo("Peter","Parker"))

def pepe(nombre, apellido):
    print(f"hola, mi nombre es {nombre} {apellido}")

pepe("Peter", "Parker")
pepe("Victor", "Rodriguez")
pepe("Juan", "Perez")

# def menos(a=9,b=8):
#     return a+b
# print(menos(3,5))
# print(menos(3.5,5.5))
# print(menos(b=3))


def contador(x):
    count=0

    while count < x:
        count+=0.5
        print(count)

contador(18)
    



