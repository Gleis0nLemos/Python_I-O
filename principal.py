try:
    with open('dados/contatos.csv', encoding='latin_1') as arquivo_contato:

        for linha in arquivo_contato:
            print(linha, end= '')

except FileNotFoundError:
    print('Arquivo csv não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
    