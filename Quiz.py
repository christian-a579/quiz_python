perguntas = [
    {
        'Pergunta': 'Qual é a linguagem que utiliza o Framework Django para desenvolvimento web?',
        'Opcao': ['PHP', 'PYTHON', 'C#', 'JAVA'],
        'Resposta': 'PYTHON',
    },
    {
        'Pergunta': 'Qual é o principal uso do JSON?',
        'Opcao': ['Estilizar páginas web', 'Trocar dados entre sistemas', 'Criar bancos de dados relacionais'],
        'Resposta': 'Trocar dados entre sistemas',
    },
    {
        'Pergunta': 'Quais tipos de dados o JSON pode armazenar?',
        'Opcao': ['Somente texto', 'Texto, números e imagens', 'Texto, números, booleanos, arrays e objetos'],
        'Resposta': 'Texto, números, booleanos, arrays e objetos',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    # Exibe as opções numeradas
    opcoes = pergunta['Opcao']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    # Solicita a escolha do usuário
    escolha = input('Escolha uma opção: ')
    print()

    # Valida se a escolha é um número dentro do intervalo de opções
    if escolha.isdigit() and 0 <= int(escolha) < len(opcoes):
        escolha_int = int(escolha)
        if opcoes[escolha_int] == pergunta['Resposta']:
            qtd_acertos += 1
            print('Meus Parabéns, Você Acertou!!')
        else:
            print('Você Errou.')
    else:
        print('Escolha inválida. Você Errou.')

    print()

# Exibe o resultado final
print(f'Você Acertou {qtd_acertos} de {len(perguntas)} perguntas.')