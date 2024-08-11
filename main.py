import os
import time

nota = []

while True:
    print('Escolha uma opção\n')
    print('1 - Inserir nota')
    print('2 - Exibir média')
    print('3 - Sair da calculadora')

       
    opcao = int(input('Digite a opção: '))
    
    match opcao:
        case 1:
            os.system('cls') 
            inserir_nota = int(input('Digite a nota, por favor: ')) 
            if inserir_nota >= 0 and inserir_nota <= 10:
                nota.append(inserir_nota)
                print('Nota inserida com sucesso')
            else:
                print('Nota não inserida, por favor insira notas entre 0 e 10 ')
            continue
        case 2:
            os.system('cls') 
            media = sum(nota)/len(nota)
            print(f'\n A média é: {media}\n')
            continue
        case 3:
            os.system('cls')
            print('\nsaindo...')
            time.sleep(1)
            os.system('cls')
            time.sleep(1)
            print('Até...logo')
            break
        case _:
            print('Alguma coisa deu errada')
