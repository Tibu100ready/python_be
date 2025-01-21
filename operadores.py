# print(3<4 and "hola">"adios")
# print(3>4 and "hola">"adios")
# print(3>4 or 2>1)
# print(3<4 or "adios">"hola")

# print(10 % 11)

# print(12 // 11)
# print(9 ** 3)
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
