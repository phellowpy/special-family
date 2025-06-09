def sistema_login():
    # Dicionário para armazenar usuários e senhas.
    # Em um sistema real, as senhas seriam armazenadas de forma segura (hash).
    usuarios_cadastrados = {
        "admin": "senha123",
        "usuario1": "abc@123",
        "teste": "minhasenha"
    }

    print("Bem-vindo ao sistema de login!")

    while True:
        nome_usuario = input("Digite seu nome de usuário: ").lower() # Converte para minúsculas
        senha = input("Digite sua senha: ")

        if nome_usuario in usuarios_cadastrados:
            if usuarios_cadastrados[nome_usuario] == senha:
                print(f"\nLogin bem-sucedido! Bem-vindo(a), {nome_usuario}!")
                break # Sai do loop após o login
            else:
                print("Senha incorreta. Tente novamente.")
        else:
            print("Nome de usuário não encontrado. Tente novamente ou cadastre-se.")

# Chama a função para iniciar o sistema de login
sistema_login()
