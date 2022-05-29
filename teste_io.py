arquivo = open('dados/contatos.csv', encoding='latin_1')

print(type(arquivo.buffer))

texto_em_bytes = bytes('Esse é um texto em bytes', encoding='latin_1')
print(texto_em_bytes)
print(type(texto_em_bytes))

arquivo.close()
