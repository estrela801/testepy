def add(tarefa, lista):
    lista.append(tarefa)
    print(f'A tarefa "{tarefa}" foi adicionada')

def remove(tarefa, lista):
    if tarefa in lista:
        lista.remove(tarefa)
        print(f'A tarefa "{tarefa}" foi removida')
    else:
        print(f'A tarefa "{tarefa}" não foi encontrada na lista')
    print(lista)

def marcar(tarefa, dic):
    dic['concluida'] = tarefa
    print(f'Tarefa "{tarefa}" marcada como concluída')
    print(dic)

def mostrar(lista):
    print("Lista de tarefas:")
    for tarefa in lista:
        print(f'- {tarefa}')

def feita(dic):
    print("Tarefas concluídas:")
    print(dic)

def nFeita(dic, lista):
    for chave in dic:
        if dic[chave] in lista:
            lista.remove(dic[chave])
    print(lista)
    print('acabou')