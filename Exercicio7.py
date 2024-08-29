# Solicita o nome do arquivo
file_name = input('Digite o nome do arquivo: ')

# Inicializar variáveis
campus_c = {}
ano_c = {}
curso_c = {}
total_alunos = 0

# Abrir e ler o arquivo
with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Processar as linhas do arquivo
for line in lines:
    parts = line.strip().split(';')
    if len(parts) >= 8:
        campus = parts[7].strip()
        ano = parts[5][:4].strip()
        curso = parts[4].strip()
        
        # Contagem por campus
        if campus:
            if campus not in campus_c:
                campus_c[campus] = 0
            campus_c[campus] += 1
        
        # Contagem por ano
        if ano:
            if ano not in ano_c:
                ano_c[ano] = 0
            ano_c[ano] += 1
        
        # Contagem por curso 
        if curso and campus:
            if campus not in curso_c:
                curso_c[campus] = {}
            if curso not in curso_c[campus]:
                curso_c[campus][curso] = 0
            curso_c[campus][curso] += 1
        
        total_alunos += 1

# Salvar a lista de campus em um arquivo
campus_list = [[campus, count, round((count / total_alunos) * 100, 2)] for campus, count in campus_c.items()]
with open('alunos_ifrn_campus.csv', 'w', encoding='utf-8') as file:
    for item in campus_list:
        file.write(f"{item[0]};;{item[1]};;{item[2]}\n")

# Salvar a lista de anos em um arquivo
ano_list = [[ano, count] for ano, count in ano_c.items()]
with open('alunos_ifrn_ano.csv', 'w', encoding='utf-8') as file:
    for item in ano_list:
        file.write(f"{item[0]};;{item[1]}\n")

# Listar campus e pedir escolha do usuário
print("Aqui estão os campi disponíveis:")
for campus in campus_c.keys():
    print(campus)

escolha = input("Digite o nome do campus desejado: ").strip()

# Verificar se a escolha é válida
if escolha in curso_c:
    # Salvar a lista de cursos no campus escolhido em um arquivo
    curso_list = [[curso, count] for curso, count in curso_c[escolha].items()]
    with open('alunos_ifrn_campus_curso.csv', 'w', encoding='utf-8') as file:
        for item in curso_list:
            file.write(f"{item[0]};{item[1]}\n")
else:
    print("O campus selecionado não é válido.")
