import nltk

class Corretor:

    def __init__(self, bd, palavra = ''):
        self.__palavra = palavra.lower()
        self.__bd = bd
        self.frequencia = nltk.FreqDist(bd)
        self.tamanho = len(bd)

    def set_palavra(self, n_palavra):
        self.__palavra = n_palavra.lower()

    def is_correct(self):
        return self.__palavra in self.__bd

    def __inverte_letra(self, fatiado):
        esquerda, direita = fatiado
        if len(direita) > 1:
            palavra = esquerda + direita[1] + direita[0] + direita[2:]
            return [palavra]
        else: 
            return []

    def __insere_letra(self, fatiado):
        palavras = []
        alfabeto = 'abcdefghijklmnopqrstuvwxyzáâàãéêèíìîóôõòúûùç'
        esquerda, direita = fatiado
        for letra in alfabeto:
            palavras.append(f'{esquerda}{letra}{direita}')
        return palavras

    def __delete_letra(self, fatiado):
        esquerda, direita = fatiado
        palavra = esquerda + direita[1:]
        return [palavra]

    def __troca_letra(self, fatiado):
        palavras = []
        alfabeto = 'abcdefghijklmnopqrstuvwxyzáâàãéêèíìîóôõòúûùç'
        esquerda, direita = fatiado
        for letra in alfabeto:
            palavras.append(f'{esquerda}{letra}{direita[1:]}')
        return palavras

    def gerador_de_palavras(self, metodo):
        palavras = []
        for i in range(len(self.__palavra)+1):
            fatiado = (self.__palavra[:i], self.__palavra[i:])
            palavras += metodo(fatiado)
        return palavras


    def probabilidade(self, palavra_gerada):
        return self.frequencia[palavra_gerada]/self.tamanho
        
    def corrigir(self):
        palavras_geradas = self.gerador_de_palavras(self.__insere_letra)
        palavras_geradas += self.gerador_de_palavras(self.__delete_letra)
        palavras_geradas += self.gerador_de_palavras(self.__troca_letra)
        palavras_geradas += self.gerador_de_palavras(self.__inverte_letra)
        palavra_correta = max(palavras_geradas, key=self.probabilidade)
        return palavra_correta
