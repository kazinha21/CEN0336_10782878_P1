#!/usr/bin/env python3

#Importando biblioteca sys
import sys

#Testando o número de argumentos
if len(sys.argv) == 3: 

#Inserindo dois número inteiros
    numero1 = sys.argv[1]
    numero2 = sys.argv[2]

#Verificando se os números são inteiros, positivos e menores que 500
    if numero1.isdigit() and numero2.isdigit():
        numero1 = int(numero1) #Transformando os dados de strings para inteiros 
        numero2 = int(numero2)
        if 0 < numero1 < 500 and 0 < numero2 < 500:

#Calculando a área
            area = (numero1*numero2)/2

#Imprimir o valor da área
            print (f'A área do triangulo retângulo com lados a={numero1} e b={numero2}, é {area}')
    
        else:
            print ('São esperados números positivos e menores que 500')
    else:
        print('São esperados números inteiros')
else: 
    print('São esperados dois argumentos')

