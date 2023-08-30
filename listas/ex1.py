lista = []

while (True):
    print("\nOpções:")
    print("1. adicionar tarefa")
    print("2. executar tarefa")
    print("3. encerrar")
    
    codigo = int(input('digite uma opção: '))
    
    if(codigo == 1):
        nomeTarefa = input('digite o nome da tarefa: ')
        lista.append(nomeTarefa)
    elif(codigo == 2):
        lista.pop(0)
        print('tarefa sendo executada')
    elif(codigo == 3):
        break
    else:
        print('opção indisponivel')