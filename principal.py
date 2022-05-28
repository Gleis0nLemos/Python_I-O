arquivo_contato = open('dados/contatos.csv', encoding='latin_1')

for linha in arquivo_contato:
    print(linha, end= '')
