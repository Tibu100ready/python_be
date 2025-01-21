x= int(input("ingresa tu edad "))
if x >= 20:
    print("puedes pasar")
else:
    print("te quedaste")

condicion=input("Deseas seguir? (si/no): ")

while condicion == "si":
    x= int(input("reingresa tu edad "))
    if x >= 20:
        print("puedes pasar")
    else:
        print("te quedaste")
    condicion=input("Deseas continuar? (si/no): ")