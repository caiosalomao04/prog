a= float(input('Informe o parâmetro a da equação: '))
b= float(input('Informe o parâmetro b da equação: '))
c= float(input('Informe o parâmetro c da equação: '))

delta=(b**2)-(4*a*c)
raiz1 = (-b + delta**(1/2)) / (2*a)
raiz2 = (-b - delta**(1/2) ) / (2*a)

print((raiz1,raiz2))





