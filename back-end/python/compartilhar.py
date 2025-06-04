posts = [
    {"nome_post": "Navegando o Autismo: Dicas para Pais", "texto_post": "Entenda e apoie seu filho no espectro autista.", "categoria": "pais"},
    {"nome_post": "TDAH e Disciplina Positiva", "texto_post": "Estratégias eficazes para lidar com o TDAH em casa.", "categoria": "pais"},
    {"nome_post": "Inclusão Escolar para Crianças Neurodivergentes", "texto_post": "Como garantir um ambiente de aprendizado acolhedor.", "categoria": "profissionais"},
    {"nome_post": "A Importância da Rotina para Crianças com TEA", "texto_post": "Estrutura e previsibilidade para o bem-estar.", "categoria": "rotina"},
    {"nome_post": "Como Conversar Sobre Neurodiversidade com a Família", "texto_post": "Dicas para promover a compreensão e o apoio.", "categoria": "conselhos"},
    {"nome_post": "Recursos e Apoio para Pais de Filhos Neurodivergentes", "texto_post": "Onde encontrar ajuda e comunidades.", "categoria": "dicas"},
    {"nome_post": "Celebrando as Diferenças: A Força da Neurodiversidade", "texto_post": "Valorizando as perspectivas únicas.", "categoria": "historia"},
    {"nome_post": "Meu Dia com um Filho Típico e um Neurodivergente", "texto_post": "Desafios e alegrias da rotina familiar.", "categoria": "dia a dia"},
    {"nome_post": "Desenvolvimento Atípico: Entendendo os Marcos", "texto_post": "Observando e apoiando o crescimento único de cada criança.", "categoria": "profissionais"},
    {"nome_post": "Rotina Matinal com Crianças Autistas", "texto_post": "Passos para uma manhã tranquila e previsível.", "categoria": "rotina"},
    {"nome_post": "Conselhos para o Desenvolvimento da Fala em Crianças Atípicas", "texto_post": "Estratégias e atividades para estimular a comunicação.", "categoria": "conselhos"},
    {"nome_post": "A História da Neurodiversidade: Da Exclusão à Aceitação", "texto_post": "Um olhar sobre como a percepção mudou ao longo do tempo.", "categoria": "historia"},
    {"nome_post": "Dicas para Adaptar o Ambiente de Casa para o TDAH", "texto_post": "Organização e redução de distrações para o foco.", "categoria": "dicas"},
    {"nome_post": "Desafios e Vitórias: Relatos de Pais de Crianças Neurodivergentes", "texto_post": "Histórias inspiradoras e experiências de vida.", "categoria": "dia a dia"},
    {"nome_post": "Profissionais da Educação Inclusiva: O Papel dos Especialistas", "texto_post": "Entenda quem são e como eles podem ajudar seu filho.", "categoria": "profissionais"},
    {"nome_post": "Como Lidar com Crises de Regulação Emocional em Crianças com TEA", "texto_post": "Técnicas de acalmar e prevenir comportamentos desafiadores.", "categoria": "pais"},
    {"nome_post": "Ferramentas Digitais para Apoio ao Aprendizado Neurodivergente", "texto_post": "Aplicativos e softwares que auxiliam no desenvolvimento.", "categoria": "dicas"},
    {"nome_post": "A Rotina do Sono: Importância para Crianças Neurodivergentes", "texto_post": "Estratégias para uma noite de sono mais reparadora.", "categoria": "rotina"},
    {"nome_post": "Dia a Dia com um Filho com Síndrome de Down", "texto_post": "Vivenciando a jornada e promovendo a autonomia.", "categoria": "dia a dia"},
    {"nome_post": "O Impacto da Alimentação na Neurodiversidade", "texto_post": "Discussão sobre dietas e sensibilidades alimentares.", "categoria": "conselhos"},
]
#filtra e ordena em ordem alfabetica
def filtrar_posts_por_categoria(lista_posts):
    categorias_disponiveis = set(post["categoria"] for post in lista_posts)
    categorias_exibir = sorted(list(categorias_disponiveis))
#exibe as categorias disponiveis
    while True:
        print("\n--- Categorias Disponíveis ---")
        for categoria in categorias_exibir:
            print(f"- {categoria.capitalize()}") #coloca letra maiscula no começo pra ficar mais bonito visualmente
        print("----------------------------")

#aparece um input para voce digitar a categoria
        categoria_escolhida = input("Digite a categoria que você deseja filtrar (ou 'sair' para encerrar): ").lower().strip()
#o codigo para
        if categoria_escolhida == 'sair':
            print("Encerrando o filtro de posts. Até mais!")
            break
#verifica a categoria q a gente escolheu e ve se tem posts com ela
        if categoria_escolhida in categorias_disponiveis:
            posts_filtrados = [
                post for post in lista_posts if post["categoria"] == categoria_escolhida
            ]

            print(f"\n--- Posts na categoria: '{categoria_escolhida.capitalize()}' ---")
            #exibe os posts
            for post in posts_filtrados:
                print(f"Título: {post['nome_post']}")
                print(f"Texto: {post['texto_post']}")
                print(f"Categoria: {post['categoria'].capitalize()}")
                print("-" * 30)
                #se nao tiver post na categoria exibe isso
            if not posts_filtrados:
                print(f"Não foram encontrados posts para a categoria '{categoria_escolhida}'.")
                #se digitar algo invalido aparece isso
        else:
            print(f"\n'{categoria_escolhida}' não é uma categoria válida. Por favor, tente uma das categorias listadas.")

#inicia o codigo com base na funçao de filtrar
filtrar_posts_por_categoria(posts)