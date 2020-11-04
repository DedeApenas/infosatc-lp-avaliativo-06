variavel=" "
def recebeParametro():
    variavel=input("Insira os caracteres {[()]}: ")
    if "{[()]}" in variavel:
        print("Devidamente Aninhada!",True)
        return True
    elif "{[()()]}" in variavel:
        print("Devidamente Aninhada!",True)
        return True
    else:
        print("Erro",False)
        return False
recebeParametro()