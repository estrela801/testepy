import funcs as fn
lista = []
dic = dict()
feita = ''
nFeira =''
menu = 'Menu:'
print('''1: Adicionar tarefa
2: Remover tarefa'
3: Marcar tarefa como concluida
4: Listar Todas as Tarefas
5: Listar Tarefas Concluidas
6: Listar Tarefas Não Concluidas
7: Sair
      ''')

sair = False

while sair == False: # se ele não disser que quer parar, ele tem que digitar uma opção
    userChoice =int(input('Escolhauma opção: '))
    

    if userChoice == 7:
      sair = True

    if userChoice == 1:# se a escolhar for 1
        userAns = input('Diga a tarefa: ')
        fn.add(userAns,lista)
        # print(f'A tarefa {userAns} foi adicionada')
        
    if userChoice == 2: # se a escolha for 2
        print(lista)
        userAns = input('Qual deseja remover: ')
        fn.remove(userAns,lista)
        
    if userChoice == 3:
        userAns = input('Qual deseja marcar: ')
        feita = userAns
        fn.marcar(userAns,dic)
        
        
    if userChoice == 4:
        fn.mostrar(lista)
       
    if userChoice == 5:

        fn.feita(dic,feita)


    if userChoice == 6:
        fn.nFeita(dic,lista)

    
      
        
