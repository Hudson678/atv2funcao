# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

numero = int(input("insira um valor: "))
def verificar_paridade(numero):
    if numero %2 == 0:
        return f"o numero {numero} é par"
    else:
        return f"o numero {numero} é impar"

numero2 = verificar_paridade(numero)
print(numero2)


