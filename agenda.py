import os

def adicionar_contato(contatos, nome_contato="", telefone_contato="", email_contato="", favorito_contato="N"):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": favorito_contato }
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado.")
    return

def ver_contatos(contatos):
    print("\nLista de Contatos")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "✔" if contato["favorito"]=="Y" else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice} - {nome_contato} - {telefone_contato} - {email_contato} - Favorito[{favorito}]")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
    if indice_tarefa < 1 or indice_tarefa > len(tarefas):
        os.system("clear")
        print(f"Tarefa {indice_tarefa} inexistente")
        return
    else:
        os.system("clear")
        indice_tarefa = indice_tarefa - 1
        tarefas[indice_tarefa]["tarefa"] = novo_nome
        print(f"Tarefa atualizada para {novo_nome}.")
    return
def atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email, novo_favorito):
    os.system("clear")
    indice_contato = indice_contato - 1
    contatos[indice_contato]["nome"] = novo_nome
    contatos[indice_contato]["telefone"] = novo_telefone
    contatos[indice_contato]["email"] = novo_email
    contatos[indice_contato]["favorito"] = novo_favorito
    print(f"Contato atualizado com sucesso!")
    return

def favoritar_contato(contatos, indice_contato):
    if indice_contato < 1 or indice_contato > len(contatos):
        os.system("clear")
        print(f"Contato {indice_contato} inexistente")
        return
    else:
        os.system("clear")
        indice_contato = indice_contato - 1
        contatos[indice_contato]["favorito"] = "Y"
        print(f"Contato {indice_contato+1} agora é um favorito.")
    return

def ver_contatos_favoritos(contatos):
    print("\nLista de Contatos")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]=="Y":
            favorito = "✔" if contato["favorito"]=="Y" else " "
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(f"{indice} - {nome_contato} - {telefone_contato} - {email_contato} - Favorito[{favorito}]")
    return

def deletar_contatos(contatos, indice_contato):
    if indice_contato < 1 or indice_contato > len(contatos):
        os.system("clear")
        print(f"Contato {indice_contato} inexistente")
        return
    else:
        os.system("clear")
        indice_contato = indice_contato - 1
        del contatos[indice_contato]
        print(f"Contato {indice_contato+1} apagado.")
    return
    

tarefas = []
contatos = []

os.system("clear")
def saudacao(nome):
    os.system("clear")
    print(f"\nOlá, {nome}!")

saudacao(input("Digite seu nome: "))

while True:
    print("\nMenu do gerenciador de contatos")
    print("1. Adicionar um contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar um contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Ver lista de contatos Favoritos")
    print("6. Apagar um contato")
    print("7. Sair")
    escolha = input("Digite a sua escolha: ")
    
    if escolha == "1":
        os.system("clear")
        nome_contato = input("Digite o nome: ")
        telefone_contato = input("Digite o telefone: ")
        email_contato = input("Digite o email: ")
        favorito_contato = input(f"'{nome_contato}' é um contato favorito? (Y/N) ")
        os.system("clear")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, favorito_contato)
    elif escolha == "2":
        os.system("clear")
        ver_contatos(contatos)
    elif escolha == "3":
        os.system("clear")
        print("Estes são seus contatos:")
        ver_contatos(contatos)
        num_contato = int(input("\nQual contato deseja atualizar?: "))
        if num_contato < 1 or num_contato > len(contatos):
            os.system("clear")
            print(f"Contato {num_contato} inexistente")
        else:
            novo_nome = input(f"\nQual o novo nome do contato {num_contato} ?: ")
            novo_telefone= input(f"\nQual o novo telefone do contato {num_contato} ?: ")
            novo_email = input(f"\nQual o novo email do contato {num_contato} ?: ")
            novo_favorito= input(f"\nO contato {num_contato} é favorito? (Y/N): ")
            atualizar_contato( contatos, num_contato, novo_nome, novo_telefone, novo_email, novo_favorito)
    elif escolha == "4":
        os.system("clear")
        print("Estes são seus contatos:")
        ver_contatos(contatos)
        num_contato = int(input("\nQual contato deseja marcar como favorito?"))
        favoritar_contato(contatos, num_contato)    
    elif escolha == "5":
        os.system("clear")
        ver_contatos_favoritos(contatos)
    elif escolha == "6":
        os.system("clear")
        print("Estes são seus contatos:")
        ver_contatos(contatos)
        num_contato = int(input("\nQual contato deseja apagar?"))
        deletar_contatos(contatos, num_contato)
    elif escolha == "7":
        os.system("clear")
        break


print ("Programa finalizado")