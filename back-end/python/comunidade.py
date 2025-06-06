comunidade = [
    {"nome": "Entendendo o diagnóstico do seu filho", "texto": "Orientações sobre como entender relatórios médicos e psicológicos.", "categoria": "pais"},
    {"nome": "Estratégias educacionais para autistas", "texto": "Métodos de ensino adaptados para crianças no espectro autista.", "categoria": "educação"},
    {"nome": "Terapias complementares para TDAH", "texto": "Abordagens terapêuticas para desenvolvimento de crianças com TDAH.", "categoria": "terapeutico"},
    {"nome": "Inclusão escolar: real x ideal", "texto": "Desafios da inclusão escolar de crianças neurodivergentes.", "categoria": "debate"},
    {"nome": "Transição para a vida adulta", "texto": "Como ajudar adolescentes neurodivergentes na independência.", "categoria": "pais"},
    {"nome": "Direitos legais das crianças", "texto": "Direitos garantidos por lei a crianças neurodivergentes.", "categoria": "profissionais"},
    {"nome": "Autocuidado para pais", "texto": "Importância da saúde mental de pais de crianças especiais.", "categoria": "terapeutico"},
    {"nome": "Tecnologias assistivas", "texto": "Aplicativos e dispositivos para auxiliar no desenvolvimento.", "categoria": "educação"},
    {"nome": "Explicando para irmãos", "texto": "Como ajudar irmãos neurotípicos a entender a neurodivergência.", "categoria": "pais"},
    {"nome": "Profissionais essenciais", "texto": "Especialistas que compõem a equipe multidisciplinar.", "categoria": "profissionais"},
    {"nome": "Rotinas para crianças autistas", "texto": "Como estabelecer rotinas que ajudam no desenvolvimento.", "categoria": "pais"},
    {"nome": "Comunicação alternativa", "texto": "Métodos para crianças com dificuldades de comunicação verbal.", "categoria": "educação"},
    {"nome": "Atividades sensoriais", "texto": "Ideias de atividades para crianças com necessidades sensoriais.", "categoria": "terapeutico"},
    {"nome": "Escola regular ou especial?", "texto": "Prós e contras de cada modelo educacional.", "categoria": "debate"},
    {"nome": "Preparando para consultas", "texto": "Como preparar crianças neurodivergentes para consultas médicas.", "categoria": "pais"}
]

def filtrar_comunidade(categoria):
    return [comunidade for comunidade in comunidade if comunidade["categoria"] == categoria.lower()]

def mostrar(comunidades_filtradas):
    if not comunidades_filtradas:
        print("\nNenhuma comunidade encontrada.")
    else:
        print(f"\n{len(comunidades_filtradas)} comunidade(s) encontrada(s):")
        for i, comunidade in enumerate(comunidades_filtradas, 1):
            print(f"\n{i}. {comunidade['nome']}\n{comunidade['texto']}\nCategoria: {comunidade['categoria']}\n{'─'*50}")

print("Filtro de Comunidades")
print(f"\nCategorias: educação, terapeutico, debate, profissionais, pais")
print(f"Digite 'sair' para encerrar o programa")

while True:
    categoria = input("\nDigite uma categoria: ").strip().lower()
    
    if categoria == 'sair':
        print("\nEncerrando o programa...")
        break
    
    if categoria not in ['educação', 'terapeutico', 'debate', 'profissionais', 'pais']:
        print("Categoria inválida. Por favor, escolha entre: educação, terapeutico, debate, profissionais, pais")
        continue
    
    mostrar(filtrar_comunidade(categoria))
