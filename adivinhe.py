import random as r
numero = r.randint(1,9)
user = input('Vamos ver se você consegue acertar o número? Escolha um número de 1 a 9.: ')

while not user.isnumeric():
    print('Por favor, digite apenas números.')
    user = input('Digite um número de 1 a 9.')    

user = int(user)
    
if user == numero:
    print('Parabéns, você acertou!')
else:
    print(f'Que pena, o número sorteado era {numero}.')
