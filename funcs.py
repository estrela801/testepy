print('funcs')

def add(tarefa, lista):
    lista.append(tarefa)
    print(f'A tarefa {tarefa} foi adicionada')
   

def remove(tarefa,lista):
    remv = lista.remove(tarefa)
    print(f'A tarefa {tarefa} foi removida')
    # print(remv)
    print(lista)
    

def marcar(tarefa, dic):
       dic = {}
       dic['concluida'] = tarefa
       print(dic)
       

def  mostrar(lista): 
    print(lista)

def feita(dic,feita):
    
    print('teste')
    dic['concluida'] = feita
    feita in dic
    print(dic)
          
        
def nFeita(dic,lista):
   nFe = dic in lista 
   lista.pop(nFe)
   print(lista)