numero = int(input("insira um numero de 5 digitos: "))

d1 = numero // 10000
d2 = (numero // 1000) %10
d3 = (numero // 100) %10
d4 = (numero // 10) %10
d5 = numero  %10

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)