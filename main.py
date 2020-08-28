from leitor_de_arquivos import LeitorDeArquivos
from limpador_de_lista import LimpadorDeLista
from corretor import Corretor

lista_de_palavras = LeitorDeArquivos().ler_a_pasta()  # .ler_o_arquivo()#
lista_de_palavras = LimpadorDeLista(lista_de_palavras).limpar()
lista_de_palavras_conjunto = sorted(list(set(lista_de_palavras)))

n_frase = ''
corretor = Corretor(lista_de_palavras)

while True:
    frase = input("Escreva a frase a ser corrigida: ")
    palavras_da_frase = frase.split(" ")

    for palavra in palavras_da_frase:
        corretor.set_palavra(palavra)
        if(corretor.is_correct()):
            n_frase += palavra + " "
        else:
            n_frase += corretor.corrigir() + " "

    print(n_frase)
    n_frase = '' 
