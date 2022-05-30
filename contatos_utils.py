import csv, pickle, json
from contato import Contato
from abc import ABC, abstractmethod


def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id, nome, email = linha                 #pode ser escrito também:
                                                    #id = linha[0]            
                                                    #nome = linha[1]            
            contato = Contato(id, nome, email)      #email = linha[2]
            contatos.append(contato)

    return contatos


def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)

    
def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
       contatos = pickle.load(arquivo)

    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=lambda contato: contato.__dict__)

#o parametro 'defaut' serve para receber um objeto invocável, podendo assim receber uma função(lambda)/função sem nome,
#podendo assim fazer o chamado dict, como mostrado em 'contatos_para_json, logo acima. O def abaixo tem exatamente a mesma chama de 'lambda'
#def _contato_para_json(contato):
     #return contato.__dict__


def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:   #os dois * indicam pro python desempacotar os arquivos ali citados
            c = Contato(**contato)      #**por baixo dos panos é(id=contato['id'], nome=contato['nome'], email=contato['email'])
            contatos.append(c)

    return contatos


class ContatoDao(ABC):

    @abstractmethod
    def buscar_todos(self, caminho):
        pass

    @abstractmethod
    def salvar(self, contatos, caminho):
        pass


class ContatoDaoJSON(ContatoDao):

    @abstractmethod
    def buscar_todos(self, caminho):
        contatos = []
        with open(caminho, mode='r') as arquivo:
            contatos_json = json.load(arquivo)
            for contato in contatos_json:
                        c = Contato(**contato)
                        contatos.append(c)

        return contatos   


    @abstractmethod
    def salvar(self, contatos, caminho):
        with open(caminho, mode='w') as arquivo:
            json.dump(contatos, arquivo, default=lambda objeto: objeto.__dict__) 