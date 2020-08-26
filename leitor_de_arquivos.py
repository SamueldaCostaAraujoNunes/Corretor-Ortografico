import nltk
import os

class LeitorDeArquivos:
    def __init__(self):
        self.__lista = []

        
    def __criar_lista_palavras(self, texto):
        lista_palavras = nltk.tokenize.word_tokenize(texto)
        return lista_palavras
    
    def ler_o_arquivo(self, filename='palavras.txt'):
        with open(filename, 'r', encoding='utf-8') as f:
            texto = f.read()
        return self.__criar_lista_palavras(texto)

    def ler_a_pasta(self, path = "Livros"):
        for filename in os.listdir(path):
            if filename.endswith(".txt"):
                self.__lista += self.ler_o_arquivo(f"{path}/{filename}")
        return self.__lista