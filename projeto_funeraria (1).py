import json
from difflib import SequenceMatcher as SM

        

basicos = []
premiums = []

print("#####################################")
print("#         ☻☺ BEM VINDO ☺☻           #")
print("#   ◘ ESCOLHA SEU PLANO FUNERÁRIO ◘ #")
print("#####################################")

def menu():
    print('''
     
     .•*´¨`*•.¸¸.•*´¨`*
     °                °
     °   1 - basico   °
     °                °
     °   2 - premium  °
     °                °
    .•*´¨`*•.¸¸.•*´¨`*°
    ''')
    op=input("digite uma opção: ")
    return op
    

def basico():
    print('''
    
    ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠
                             ☠
    1 - cadrastrar           ☠ 
    2 - buscar               ☠
    3 - alterar              ☠
    4 - excluir              ☠
    5 - listar               ☠
    6 - salvar dados         ☠
    7 - sair                 ☠
                             ☠                                   
    ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ 
   ''')

    bas=input(" digite uma opção: ")
    return bas 
    
    
def cadastrar():
        print("======== ☻ NOME ☺ =======")
    
        n=input(" digite o novo nome: ")
    
        print("====== ☻ DATA_DE_NASCIMENTO ☺ ==========")
    
        d=input(" digite a nova data de nascimento: ")
    
        print("=================  ☻ TELEFONE  ☺  ==================")
    
        num=input(" digite o novo numero de telefone: ")
    
        print("==========  ☻ CPF ☺ =========") 
    
        cpf=input(" digite o novo cpf: ")
        
        print("============ ☺ CIDADE☻ ===============")
         
        c=input("digite a sua nova cidade: ")
    
        print("============ ☺ BAIRRO ☻ ===============")
    
        bairr=input(" digite o novo bairro: ")
    
        print("======= • cliente cadastrado com sucesso • ==============")
    
        cliente ={'nome':n,
              'nascimento':d,
              'fone':num,
              'cpf':cpf,
              'bairro':bairr,
              'cidade': c}          
        return cliente


def alterar(p):
    plano = basicos[p]
    n=input(" digite o novo nome ")
    d=input(" digite a nova data de nascimento ")
    num=input(" digite o novo numero de telefone ")
    cpf=input(" digite o novo cpf ")
    c= input(" digite sua cidade ")
    bairr=input(" digite o novo bairro ")
    plano['nome'] = n
    plano['nascimento'] = d
    plano['fone'] = num
    plano['cpf'] = cpf
    plano['cidade'] = c
    plano['bairro'] = bairr
    
    
def excluir ():
    no=input("digite um nome para buscar: ")
    for p,e in enumerate(basicos):
        if e['nome'] == no:
            del(basicos[p])
            print(" excluido com sucesso ")
        else:
                 print("plano não encontrado")          
    return None
        
               
        

def busca():
    no=input("digite um nome para buscar: ")
    for p,e in enumerate(basicos):
        if e['nome'] == no:
            return p 
    return None


def listar_basico():
    print("================= LISTA DE PLANOS ==================== |")
    for plano in basicos:                                                                                    
        print("| Nome:", plano['nome'])                                                                  
        print("| Data de nascimento:", plano['nascimento'])                                     
        print("| Telefone:", plano['fone'])                                                                
        print("| Cpf:", plano['cpf'])                                                                         
        print("| c:", plano["cidade"])                                                                      
        print("| Bairro:", plano['bairro'])                                                                 
        print("======================================================")






def premium():
    print('''
    ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠
                             ☠
    1 - cadrastrar           ☠ 
    2 - buscar               ☠
    3 - alterar              ☠
    4 - excluir              ☠
    5 - listar               ☠
    6 - salvar dados         ☠
    7 - sair                 ☠
                             ☠                                   
    ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ 
        ''')
    pre=input(" digite uma opção: ")
    return pre
    
    
def cadastrar_premium():
        print("======== ☻ NOME ☺ =======")
    
        n=input(" digite o novo nome: ")
    
        print("====== ☻ DATA_DE_NASCIMENTO ☺ ==========")
    
        d=input(" digite a nova data de nascimento: ")
    
        print("=================  ☻ TELEFONE  ☺  ==================")
    
        num=input(" digite o novo numero de telefone: ")
    
        print("==========  ☻ CPF ☺ =========") 
    
        cpf=input(" digite o novo cpf: ")
        
        print("============ ☺ CIDADE☻ ===============")
         
        cc=input("digite a sua nova cidade: ")
    
        print("============ ☺ BAIRRO ☻ ===============")
    
        bairr=input(" digite o novo bairro: ")
    
        print("======= • cliente cadastrado com sucesso • ==============")
     
        
        p1=input('digite um nome de um participante: ')
        p2 =input('digite o nome do participante:')
        p3=input("digite o nome de outro participante:")
        p4=input("digite o nome de outro participante:")
        p5=input("digite o nome de outro participante:")
        print("======= participantes cadastrado =============")
        clientee ={'nome':n,
              'nascimento':d,
              'fone':num,
              'cpf':cpf,
              'bairro':bairr,
              'cidade':cc,
              'pessoa1':p1,
              'pessoa2':p2,
              'pessoa3':p3,
              'pessoa4':p4,
              'pessoa5':p5}          
        return clientee


def alterar_premium(p):
    print("========== ALTERAR SEUS DADOS ============")
    plano = premiums[p]
    n=input(" digite o novo nome ")
    d=input(" digite a nova data de nascimento ")
    num=input(" digite o novo numero de telefone ")
    cpf=input(" digite o novo cpf ")
    c=input("digite a sua nova cidade")
    bairr=input(" digite o novo bairro ")
    p1=input('digite um nome de um participante ')
    p2 =input('digite o nome do participante:')
    p3=input("digite o nome de outro participante:")
    p4=input("digite o nome de outro participante:")
    p5=input("digite o nome de outro participante:")
    plano['nome'] = n
    plano['nascimento'] = d
    plano['fone'] = num
    plano['cpf'] = cpf
    plano['cidade'] = c
    plano['bairro'] = bairr
    plano['pessoa1']=p1
    plano['pessoa2']=p2
    plano['pessoa3']=p3
    plano['pessoa4']=p4
    plano['pessoa5']=p5
    
    
def excluir_premium():
    no=input("digite um nome para buscar: ")
    for p,e in enumerate(premiums):
        if e['nome'] == no:
            del(premiums[p])
            print(" excluido com sucesso ")
    return None

def busca_premium():
    no=input("digite um nome para buscar: ")
    for p,e in enumerate(premiums):
        if e['nome'] == no:
            return p
            print("================= BUSCAR PLANO ====================")
            print("| Nome:", plano['nome'])                            
            print("| Data de nascimento:", plano['nascimento'])          
            print("| Telefone:", plano['fone'])
            print("| Cpf:", plano['cpf'])
            print("| Bairro:", plano['bairro'])
            print("| participante1:",plano['pessoa1'])
            print("| participante2:",plano['pessoa2'])
            print("| participante3:",plano['pessoa3'])
            print("| participante4:",plano['pessoa4'])
            print("| participante5:",plano['pessoa5']) 
            print("======================================================")
    

        
    return None


def listar_premium():
    for plano in premiums:
        print("================= LISTA DE PLANOS ====================")
        print("| Nome:", plano['nome'])                             
        print("| Data de nascimento:", plano['nascimento'])
        print("| Telefone:", plano['fone'])
        print("| Cpf:", plano['cpf'])
        print("| cidade:", plano['cidade'])
        print("| Bairro:", plano['bairro'])
        print("======================================================")
        print("============= LISTAR PARTICIPANTES ====================")
        print("| participante1:",plano['pessoa1'])
        print("| participante2:",plano['pessoa2'])
        print("| participante3:",plano['pessoa3'])
        print("| participante4:",plano['pessoa4'])
        print("| participante5:",plano['pessoa5']) 
        print("======================================================")
    
op = menu()
while True:

    if op =="1":
        bas=basico()
        if bas=="1":
            cliente = cadastrar()
            basicos.append(cliente)
        elif bas == '2':
            p = busca()
            if p != None:
                print(basicos[p])
            else:
                print("Plano não encontrado!")
        
        elif bas == '5':
            listar_basico()
        elif bas == '7' :
            print("========== •plano basico finalizado• ===========")
            print("========= •OBRIGADO• ============")
            break
        elif bas == '3':
            p = busca()
            if p != None:
                alterar(p)
        elif bas == '4':
            excluir()
        elif bas== '6':
            print("========= DADOS GRAVADOS ==========")
            salvar_dados(basicos, "basico.json")
            
    elif op =="2":
        pre=premium()
        if pre=="1":
            clientee = cadastrar_premium()
            premiums.append(clientee)
        elif pre == '2':
            p = busca_premium()
            if p != None:
                print(premiums[p])
            else:
                print("Plano não encontrado!")
        
        elif pre == '5':
            listar_premium()
        elif pre == '7':
            print("========== •plano premium  finalizado• ===========")
            print("========= •OBRIGADO• ============")
            break
        elif pre == '6':
            print("========= DADOS GRAVADOS ==========")
            salvar_dados(premiums, "premium.json")
        elif pre == '3':
            p = busca_premium()
            if p != None:
                alterar_premium(p)
        elif pre == '4':
            excluir_premium()
    else :
        print('opção invalida')
        menu()
