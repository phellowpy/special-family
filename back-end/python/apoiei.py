# Mensagem de boas-vindas
print("Bem-vindo ao Special Family.")
print("Segue abaixo os requisitos formais para se poder fazer a doação, contamos com sua colaboração. Obrigado.")
print("")

# Coleta de dados pessoais
nome = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")
email = input("Digite seu e-mail: ")

print("\nSeus dados foram guardados com segurança.\n")

# Escolha da forma de pagamento
print("Agora escolha a forma de pagamento digitando o número correspondente:")
print("1 - Cartão de Débito")
print("2 - Cartão de Crédito")
print("3 - PIX")
forma_pagamento = input("Digite 1, 2 ou 3: ")

# Se escolheu cartão, pedir dados do cartão
if forma_pagamento == "1" or forma_pagamento == "2":
    print("\nAgora preencha os dados do cartão:")
    nome_cartao = input("Nome completo no cartão: ")
    numero_cartao = input("Número do cartão: ")
    validade = input("Data de validade (MM/AA): ")
    banco = input("Nome do banco: ")
    
    print("\nOs dados do cartão foram salvos com segurança.")
    print("O cartão está pronto e configurado para realizar a doação.\n")

elif forma_pagamento == "3":
    print("\nVocê escolheu PIX.")
    print("Copie a chave abaixo e cole no app do seu banco para fazer a doação.")
    print("Chave PIX: doacoes@specialfamily.org\n")
else:
    print("\nOpção inválida.")
    exit()

# Escolha do valor da doação
print("Agora escolha o valor da doação:")
valor = input("Digite o valor (R$): ")

# Confirmação
confirmar = input("Digite 'confirmar' para enviar a transação: ")

if confirmar.lower() == "confirmar":
    print("\nTransação enviada com sucesso!")
    print("Para sua segurança e nosso profissionalismo, seu comprovante será enviado no seu e-mail:", email)
else:
    print("\nTransação cancelada.")
