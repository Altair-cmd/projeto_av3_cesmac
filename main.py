from bd import cadastrar_produto
from bd import cadastrar_usuario
from bd import atualizar_produto
from bd import buscar_produto_por_nome
from bd import exibir_produto_por_id
from bd import login
from bd import remover_produto


print("Exemplo de uso:")
print("1. Cadastrar Usuário")
nome = input("Nome: ")
email = input("Email: ")
senha = input("Senha: ")
cadastrar_usuario(nome, email, senha)

print("\n2. Realizar Login")
email_login = input("Email: ")
senha_login = input("Senha: ")
usuario_logado = login(email_login, senha_login)

if usuario_logado:
    print(f"\nBem-vindo, {usuario_logado[1]}!\n")
    while True:
        print("Menu Interno:")
        print("1. Cadastrar Produto")
        print("2. Alterar Produto")
        print("3. Remover Produto")
        print("4. Buscar Produto")
        print("5. Exibir 1 Produto")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_produto = input("Nome do Produto: ")
            preco_produto = float(input("Preço do Produto: "))
            cadastrar_produto(nome_produto, preco_produto)

        elif escolha == "2":
            id_produto = int(input("ID do Produto a ser alterado: "))
            nome_produto = input("Novo Nome do Produto: ")
            preco_produto = float(input("Novo Preço do Produto: "))
            atualizar_produto(id_produto, nome_produto, preco_produto)
            

        elif escolha == "3":
            id_produto = int(input("ID do Produto a ser removido: "))
            remover_produto(id_produto)

        elif escolha == "4":
            nome_produto = input("Nome do Produto a ser buscado: ")
            produtos_encontrados = buscar_produto_por_nome(nome_produto)
            print("Produtos Encontrados:")
            for produto in produtos_encontrados:
                print(produto)

        elif escolha == "5":
            id_produto = int(input("ID do Produto a ser exibido: "))
            produto = exibir_produto_por_id(id_produto)
            print("Produto Encontrado:")
            print(produto)

        elif escolha == "6":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

else:
    print("Login falhou. Verifique suas credenciais.")