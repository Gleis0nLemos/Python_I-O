arquivo = open('dados/contatos_escrita.csv', encoding='latin_1', mode='a+')

print(type(arquivo.buffer))

texto_em_bytes = bytes('Esse é um texto em bytes', encoding='latin_1')
# print(texto_em_bytes)
# print(type(texto_em_bytes))
conteudo = bytes('15,Verônica,veronica@veronica.com.br\n', encoding='latin_1')
arquivo.buffer.write(conteudo)

arquivo.close()
