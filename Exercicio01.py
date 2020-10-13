lista = [1,2,3,4]
def rotacionar(lst,x):
    copy = list(lst)
    while numero !=0:   
        for i in range(len(lst)):
            if x<0:
                lst[i+x] = copy[i]
        else:
            lst[i] = copy[i-x]   
numero = int(input("Digite um numero POSITIVO ou NEGATIVO: "))
rotacionar(lista, numero)

print(lista)