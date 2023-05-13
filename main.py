# GERADOR DE SENHAS ALEATORIA
import random
import string

caracteres = int(input('Quantos caracteres voce deseja na sua senha? '))
print('Okay, vou te dar umas opçoes de senha agora')

escolhas = string.digits + string.ascii_uppercase
resultado = ''
for i in range(caracteres):
    resultado += random.choice(escolhas)
print(resultado)

escolhas_2 = string.ascii_lowercase + string.digits
resultado2 = ''
for i in range(caracteres):
    resultado2 += random.choice(escolhas_2)
print(resultado2)

escolhas_3 = string.punctuation + string.digits
resultado3 = ''
for i in range(caracteres):
    resultado3 += random.choice(escolhas_3)
print(resultado3)

escolhas_4 = string.digits
resultado4 = ''
for i in range(caracteres):
    resultado4 += random.choice(escolhas_4)
print(resultado4)

escolhas_5 = string.ascii_lowercase + string.ascii_uppercase + string.digits
resultado5 = ''
for i in range(caracteres):
    resultado5 += random.choice(escolhas_5)
print(resultado5)
