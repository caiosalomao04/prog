#QUESTAO 1
def eq_segundo_grau(a,b,c):
    return (b**2)-(4*a*c)


a= float(input('Informe o parâmetro a da equação: '))
b= float(input('Informe o parâmetro b da equação: '))
c= float(input('Informe o parâmetro c da equação: '))
delta=eq_segundo_grau(a,b,c)
raiz1 = (-b + delta**(1/2)) / (2*a)
raiz2 = (-b - delta**(1/2) ) / (2*a)

print(raiz1,raiz2)

def bissexto(ano):
    if (ano%4)==0:
        return True
    elif (ano%100)==0:
        return True
    elif (ano%400)==0:
        return True
    else:
        return False

ano=int(input('Digite um ano: '))
print(bissexto(ano))

#QUESTAO 2

def calcula_salario(valor_hora,num_horas):
    irpf=0.275
    produto=valor_hora*num_horas
    return (produto*irpf)*30

print(calcula_salario(20,8))















