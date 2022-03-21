print('Digite as notas para cálculo da média e saber se foi aprovado ou reprovado')
nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))
nota3 = int(input('Digite a nota 3: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 5:
    print('Sua média é %.f. Você está aprovado!' % media)
else:
    print('Sua média é %.f. Você está reprovado!' % media)
