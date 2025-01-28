# #Orden superior
def amigo(a):
    return "habla menor"

def ayuda(c):
    return "hey ayudeme"

def mensaje(x):
    return x ("hola")

def saludos(b):
    return "holis"

msj_1=mensaje(amigo)
msj_2=mensaje(ayuda)
msj_3=mensaje(saludos)
print(msj_1) 
print (msj_2)
print (msj_3)

# #Callback
# def cb_amigo():
#     return "habla menor"

# def cb_ayuda():
#     return "hey ayudeme"

# def mensaje(callback_a, callback_b):
#     return [callback_a(), callback_b()]

# ct=mensaje(cb_amigo, cb_ayuda)
# print(ct)

# def callback_1(a,b,c,d):
#     return a/b-c-d

# def callback_2(a,b,c,d):
#     return a*b+c+d

# def cb_calcular(fn,x,y,z,t):
#     return [fn(x,y,z,t)]

# c=cb_calcular(callback_1,10,5,5,5)
# d=cb_calcular(callback_2,10,5,5,5)
# print(c,d)
# print(type(c),type(d))