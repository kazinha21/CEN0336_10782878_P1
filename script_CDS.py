#!/usr/bin/env python3

#Importando biblioteca sys
import sys

#Testando o número de argumentos
if len(sys.argv) != 8:
    print ('São esperados sete argumentos')
    exit(1) #O programa finaliza se não houver sete argumentos

#Inserindo sete argumentos
DNA = (sys.argv[1])
n1 = (sys.argv[2])
n2 = (sys.argv[3])
n3 = (sys.argv[4])
n4 = (sys.argv[5])
n5 = (sys.argv[6])
n6 = (sys.argv[7])

#Transformando a sequência de DNA para maiúsculo
DNA = DNA.upper()

#Tamanho da sequência de DNA
tamanho = len(DNA)

#Verificando se os argumentos são números inteiros e positivos
if n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    n5 = int(n5)
    n6 = int(n6) #Transformando os dados de string da linha de comando para inteiros
    if not (0 < n1 <= tamanho and 0 < n2 <= tamanho and 0 < n3 <= tamanho and 0 < n4 <= tamanho and 0 < n5 <= tamanho and 0 < n6 <= tamanho):
        print ('São esperados números positivos e não maiores do que o tamanho da sequência de DNA')
        exit (1) #O programa finaliza se os números forem negativos ou maiores que o tamanho da sequência de DNA
else:
    print ('São esperados 6 números inteiros')
    exit (1) #O programa finaliza se os argumentos não forem inteiros

#Extraindo a sequência do CDS1 e conferindo se inicia com o códon ATG
cds1 = DNA[n1-1:n2] # Subtrai 1 pois a sequência em python inicia em 0
if cds1[:3] != 'ATG':
    print ('A sequência não inicia com o códon ATG')
    exit(1) #O programa finaliza se a sequência de DNA não iniciar com o códon ATG

#Extraindo a sequência do CDS2
cds2 = DNA[n3-1:n4]

#Extraindo a sequência do CDS3 e conferindo se termina com um dos códon de parada
cds3 = DNA[n5-1:n6]
if cds3[-3:] != 'TAG' and cds3[-3:] != 'TAA' and cds3[-3:] != 'TGA':
    print ('A sequência não finaliza com os códons de parada')
    exit(1) #O programa finaliza se a sequência de DNA não finalizar com os códons de parada

#Concatenando CDS1, CDS2 e CDS3
concat = cds1+cds2+cds3
print (concat)
