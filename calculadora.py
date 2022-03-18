

def add(x, y):
    return x+y

def subtr(x, y):
    return x-y

def div(x, y):
    return x/y

def mult(x,y):
    return x/y


print("\nEscolha a operação desejada")
print(" 1 - Adição")
print(" 2 - Subtração")
print(" 3 - Divisão")
print(" 4 - Multiplicação")

escolha = input("\nEscolha uma opção entre 1/2/3/4")

num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))

if escolha == "1":
    print (add(num1, num2))
elif escolha == "2":
    print (subtr(num1, num2))
elif escolha == "3":
    print (div(num1, num2))
elif escolha == "4":
    print (mult(num1, num2))
else:
    print("Escolha errada.")
