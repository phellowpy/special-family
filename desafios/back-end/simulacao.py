"""Classe para representar um usuário do sistema Special Family."""
"""Class to represent a user of the Special Family system."""
class Usuario:
    def __init__(self, nome, email, senha, tipo):
        """
        Inicializa um novo usuário.

        Args:
            nome (str): O nome do usuário.
            email (str): O endereço de e-mail do usuário.
            senha (str): A senha do usuário.
            tipo (str): O tipo de usuário ('pai', 'apoiador', 'profissional', 'admin').
        """
        """
        Initializes a new user.

        Args:
            nome (str): The name of the user.
            email (str): The email address of the user.
            senha (str): The password of the user.
            tipo (str): The type of user ('pai', 'apoiador', 'profissional', 'admin').
        """
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def __str__(self):
        """
        Retorna uma representação em string do objeto Usuario.

        Returns:
            str: Uma string formatada contendo o nome, e-mail e tipo do usuário.
        """
        """
        Returns a string representation of the Usuario object.

        Returns:
            str: A formatted string containing the name, email, and type of the user.
        """
        return f"Nome: {self.nome}, Email: {self.email}, Tipo: {self.tipo.capitalize()}"

class Profissional:
    """Classe para representar um profissional de apoio."""
    """Class to represent a support professional."""
    def __init__(self, nome, especialidade):
        """
        Inicializa um novo profissional.

        Args:
            nome (str): O nome do profissional.
            especialidade (str): A especialidade do profissional.
        """
        """
        Initializes a new professional.

        Args:
            nome (str): The name of the professional.
            especialidade (str): The specialty of the professional.
        """
        self.nome = nome
        self.especialidade = especialidade

    def __str__(self):
        """
        Retorna uma representação em string do objeto Profissional.

        Returns:
            str: Uma string formatada contendo o nome e a especialidade do profissional.
        """
        """
        Returns a string representation of the Profissional object.

        Returns:
            str: A formatted string containing the name and specialty of the professional.
        """
        return f"{self.nome} ({self.especialidade})"

class SpecialFamily:
    """Classe principal para o sistema Special Family."""
    """Main class for the Special Family system."""
    def __init__(self):
        """Inicializa o sistema Special Family."""
        """Initializes the Special Family system."""
        self.usuarios = []
        self.profissionais = []
        self.senha_admin = "admin123" # Senha de segurança para administradores
        """Security password for administrators"""

    def cadastrar_usuario(self, nome, email, senha, confirma_senha, tipo):
        """Cadastra um novo usuário no sistema."""
        """Registers a new user in the system."""
        tipo = tipo.lower()
        if tipo not in ['pai', 'apoiador', 'profissional', 'admin']:
            print("Erro: Tipo de usuário inválido. Escolha entre 'pai', 'apoiador', 'profissional' ou 'admin'.")
            """Error: Invalid user type. Choose between 'pai', 'apoiador', 'profissional' or 'admin'."""
            return None

        if senha != confirma_senha:
            print("Erro: A senha e a confirmação de senha não coincidem.")
            """Error: The password and password confirmation do not match."""
            return None

        if not (6 <= len(senha) <= 10):
            print("Erro: A senha deve ter entre 6 e 10 dígitos.")
            """Error: The password must be between 6 and 10 digits long."""
            return None

        if tipo == 'admin':
            senha_seguranca = input("Digite a senha de segurança do sistema: ")
            """Enter the system security password:"""
            if senha_seguranca != self.senha_admin:
                print("Erro: Senha de segurança incorreta.")
                """Error: Incorrect security password."""
                return None

        if not any(domain in email for domain in ['@gmail.com', '@yahoo.com', '@outlook.com', '@hotmail.com']):
            print("Erro: E-mail inválido. O e-mail deve ser de um dos seguintes domínios: gmail.com, yahoo.com, outlook.com ou hotmail.com.")
            """Error: Invalid email. The email must be from one of the following domains: gmail.com, yahoo.com, outlook.com or hotmail.com."""
            return None

        for usuario in self.usuarios:
            if usuario.email == email:
                print("Erro: Este e-mail já está cadastrado.")
                """Error: This email is already registered."""
                return None

        novo_usuario = Usuario(nome, email, senha, tipo)
        self.usuarios.append(novo_usuario)
        print(f"Usuário {novo_usuario.nome} cadastrado com sucesso como {novo_usuario.tipo}.")
        """User {novo_usuario.nome} successfully registered as {novo_usuario.tipo}."""
        return novo_usuario

    def listar_profissionais(self):
        """Lista todos os profissionais cadastrados."""
        """Lists all registered professionals."""
        if not self.profissionais:
            print("Nenhum profissional cadastrado.")
            """No professionals registered."""
            return
        print("\n--- Profissionais de Apoio ---")
        """\n--- Support Professionals ---"""
        for i, profissional in enumerate(self.profissionais):
            print(f"{i+1}. {profissional}")
            """{i+1}. {profissional}"""

    def cadastrar_profissional(self, nome, especialidade):
        """Cadastra um novo profissional no sistema."""
        """Registers a new professional in the system."""
        novo_profissional = Profissional(nome, especialidade)
        self.profissionais.append(novo_profissional)
        print(f"Profissional Dr. {novo_profissional.nome} ({novo_profissional.especialidade}) cadastrado com sucesso.")
        """Professional Dr. {novo_profissional.nome} ({novo_profissional.especialidade}) successfully registered."""
        return novo_profissional

    def interagir(self, usuario):
        """Permite que o usuário interaja com o sistema baseado no seu tipo."""
        """Allows the user to interact with the system based on their type."""
        if not usuario:
            print("Nenhum usuário logado para interagir.")
            """No user logged in to interact."""
            return

        print(f"\n--- Interação para {usuario.nome} ({usuario.tipo.capitalize()}) ---")
        """\n--- Interaction for {usuario.nome} ({usuario.tipo.capitalize()}) ---"""
        if usuario.tipo == 'pai':
            quer_falar = input("Gostaria de falar com um profissional? (Sim/Não): ").lower()
            """Would you like to speak with a professional? (Yes/No):"""
            if quer_falar == 'sim':
                self.falar_com_profissional()
            else:
                quer_comentar = input("Quer comentar sobre o assunto? (Sim/Não): ").lower()
                """Do you want to comment on the subject? (Yes/No):"""
                if quer_comentar == 'sim':
                    comentario = input("Digite seu comentário: ")
                    """Enter your comment:"""
                    print("Obrigado pelo seu comentário.")
                    """Thank you for your comment."""
                    # Aqui você pode adicionar a lógica para armazenar o comentário
                    """Here you can add the logic to store the comment"""
                else:
                    print("Ok, obrigado.")
                    """Ok, thank you."""
        elif usuario.tipo == 'apoiador':
            print("Opções:")
            """Options:"""
            print("1. Doar")
            """1. Donate"""
            opcao = input("Escolha uma opção (digite o valor em R$): ")
            """Choose an option (enter the value in BRL):"""
            try:
                valor_doacao = float(opcao)
                print(f"Agradecemos imensamente sua doação de R$ {valor_doacao:.2f}!")
                """We greatly appreciate your donation of BRL {valor_doacao:.2f}!"""
                # Aqui poderia haver uma lógica para processar a doação
                """Here there could be logic to process the donation"""
            except ValueError:
                print("Opção inválida. Por favor, digite um valor numérico.")
                """Invalid option. Please enter a numeric value."""
        elif usuario.tipo == 'profissional':
            quer_atender = input("Gostaria de atender um pai agora? (Sim/Não): ").lower()
            """Would you like to attend to a parent now? (Yes/No):"""
            if quer_atender == 'sim':
                self.atender_pai()
            else:
                print("Ok, aguardando.")
                """Ok, waiting."""
        elif usuario.tipo == 'admin':
            print("Opções:")
            """Options:"""
            print("1. Ver dados do sistema (S/N)")
            """1. See system data (Y/N)"""
            opcao = input("Escolha uma opção: ")
            """Choose an option:"""
            if opcao == 'S':
                self.ver_dados_sistema()
            else:
                print("Opção inválida.")
                """Invalid option."""
        else:
            print("Tipo de usuário não reconhecido para interação.")
            """User type not recognized for interaction."""

    def falar_com_profissional(self):
        """Simula a interação de um pai para falar com um profissional."""
        """Simulates a parent's interaction to speak with a professional."""
        if not self.profissionais:
            print("Nenhum profissional disponível no momento.")
            """No professionals available at the moment."""
            return
        print("\n--- Profissionais Disponíveis ---")
        """\n--- Available Professionals ---"""
        self.listar_profissionais()
        escolha = input("Digite o número do profissional com quem gostaria de falar (ou 'voltar'): ").lower()
        """Enter the number of the professional you would like to speak with (or 'back'):"""
        if escolha != 'voltar':
            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(self.profissionais):
                    profissional_escolhido = self.profissionais[indice]
                    assunto = input(f"Digite o assunto sobre o qual gostaria de falar com {profissional_escolhido.nome}: ")
                    """Enter the subject you would like to discuss with {profissional_escolhido.nome}:"""
                    meet_link = "https://meet.google.com/ytf-meha-cwc"  # Link fictício
                    """Fictitious link"""
                    print(f"Você será direcionado para uma conversa com {profissional_escolhido.nome} em breve: {meet_link}")
                    """You will be directed to a conversation with {profissional_escolhido.nome} shortly: {meet_link}"""
                    # Aqui você poderia adicionar a lógica para realmente conectar o pai e o profissional
                    """Here you could add the logic to actually connect the parent and the professional"""
                else:
                    print("Opção inválida. Por favor, digite um número da lista ou 'voltar'.")
                    """Invalid option. Please enter a number from the list or 'back'."""
            except ValueError:
                print("Opção inválida. Por favor, digite um número ou 'voltar'.")
                """Invalid option. Please enter a number or 'back'."""
        else:
            print("Voltando ao menu principal.")
            """Returning to the main menu."""

    def doar(self):
        """Simula o processo de doação de um apoiador."""
        """Simulates the donation process of a supporter."""
        try:
            valor_doacao = float(input("Digite o valor que deseja doar (em R$): "))
            """Enter the amount you want to donate (in BRL):"""
            print(f"Agradecemos imensamente sua doação de R$ {valor_doacao:.2f}!")
            """We greatly appreciate your donation of BRL {valor_doacao:.2f}!"""
            # Aqui poderia haver uma lógica para processar a doação
            """Here there could be logic to process the donation"""
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            """Invalid value. Please enter a number."""

    def atender_pai(self):
        """Simula o atendimento de um profissional a um pai."""
        """Simulates a professional attending to a parent."""
        if not self.usuarios:
            print("Nenhum usuário cadastrado no sistema.")
            """No users registered in the system."""
            return
        pais_cadastrados = [user for user in self.usuarios if user.tipo == 'pai' and user.nome.lower() == 'luís juski'] # Simula encontrar o pai 'Luís Juski'
        """Simulates finding the parent 'Luís Juski'"""
        if pais_cadastrados:
            meet_link = "https://meet.google.com/jmc-bnoo-qmm" # Outro link fictício para o Google Meet
            """Another fictitious Google Meet link"""
            print(f"Ok, você irá para uma reunião com Luís Juski em 5 minutos: {meet_link}")
            """Ok, you will go to a meeting with Luís Juski in 5 minutes: {meet_link}"""
            # Aqui poderia haver uma lógica para iniciar o meet
            """Here there could be logic to start the meet"""
        else:
            print("Nenhum pai com o nome 'Luís Juski' encontrado para atender.")
            """No parent with the name 'Luís Juski' found to attend to."""

    def ver_dados_sistema(self):
        """Exibe dados fictícios do sistema para o administrador."""
        """Displays fictitious system data for the administrator."""
        print("\n--- Dados Fictícios do Sistema ---")
        """\n--- Fictitious System Data ---"""
        print(f"Número de usuários cadastrados: {len(self.usuarios)}")
        """Number of registered users: {len(self.usuarios)}"""
        print(f"Número de profissionais cadastrados: {len(self.profissionais)}")
        """Number of registered professionals: {len(self.profissionais)}"""
        print("\n--- Lista de Usuários ---")
        """\n--- User List ---"""
        for usuario in self.usuarios:
            print(usuario)
            """{usuario}"""
        print("\n--- Lista de Profissionais ---")
        """\n--- Professional List ---"""
        for profissional in self.profissionais:
            print(profissional)
            """{profissional}"""
        # Adicione mais dados fictícios conforme necessário (e.g., número de doações, etc.)
        """Add more fictitious data as needed (e.g., number of donations, etc.)"""

# --- Simulação de Uso do Sistema ---
"""--- System Usage Simulation ---"""
if __name__ == "__main__":
    sistema = SpecialFamily()

    # Cadastrar alguns profissionais para teste
    """Register some professionals for testing"""
    sistema.cadastrar_profissional("João Alves", "Psicólogo Infantil")
    sistema.cadastrar_profissional("Maria Souza", "Terapeuta Ocupacional")
    sistema.cadastrar_profissional("Carlos Pereira", "Fonoaudiólogo")
    sistema.cadastrar_usuario("Luís Juski", "luis@gmail.com", "senhaforte", "senhaforte", "pai")

    # Cadastro do usuário atual
    """Current user registration"""
    print("--- Cadastro de Usuário ---")
    """--- User Registration ---"""
    nome = input("Digite seu nome: ")
    """Enter your name:"""
    email = input("Digite seu e-mail: ")
    """Enter your email:"""
    senha = input("Digite sua senha (entre 6 e 10 dígitos): ")
    """Enter your password (between 6 and 10 digits):"""
    confirma_senha = input("Confirme sua senha: ")
    """Confirm your password:"""
    tipo = input("Como você quer se cadastrar (Pai, Apoiador, Profissional ou Admin)? ")
    """How do you want to register (Pai, Apoiador, Profissional or Admin)?"""

    if tipo.lower() == 'profissional':
        especializacao = input("Digite sua especialização: ")
        """Enter your specialization:"""
        novo_profissional = sistema.cadastrar_profissional(nome, especializacao)
        sistema.interagir(Usuario(nome, email, senha, tipo.lower()))
    else:
        novo_usuario = sistema.cadastrar_usuario(nome, email, senha, confirma_senha, tipo)
        if novo_usuario:
            sistema.interagir(novo_usuario)
        else:
            print("O cadastro não pôde ser concluído devido a erros.")
            """Registration could not be completed due to errors."""
