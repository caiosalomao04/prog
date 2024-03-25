#EX 1
def determina_tipo_triangulo(l1,l2,l3):
    if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
        return "Não é um triangulo"
    elif l1==l2 and l1==l3:
        return "Equilatero"
    elif l1==l2 or l1==l3 or l2==l3:
        return "Isósceles"
    else:
        return "Escaleno"
    

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo
    return


testa_triangulo()

#EX 2

def dia_semana(num):
    if num <1 or num >7:
        return ""
    if num == 1:
        return "Domingo"
    elif num == 2:
        return "Segunda"
    elif num == 3:
        return "Terça"
    elif num == 4:
        return "Quarta"
    elif num == 5:
        return "Quinta"
    elif num == 6:
        return "Sexta"
    elif num == 7:
        return "Sábado"


def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

testa_dia_semana()


#EX 3

def soma(n1,n2):
    return n1+n2
def subtracao(n1,n2):
    return n1-n2
def multiplicacao(n1,n2):
    return n1*n2
def divisao(n1,n2):
    return n1/n2

def cli(op):
    n1=float(input("Informe um número: "))
    n2=float(input("Informe outro número: "))
    op=input("Informe a operação: ")
    if op=="soma":
        return soma
    elif op=="multiplicação":
        return multiplicacao
    elif op=="subtração":
        return subtracao
    elif op=="divisão":
        return divisao
    else:
        return "operação inválida"

print(cli)

    
    
    

    


    
