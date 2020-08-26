from leitor_de_arquivos import LeitorDeArquivos
from limpador_de_lista import LimpadorDeLista
from corretor import Corretor

def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    with open(nome_arquivo, encoding="utf8") as f:
        for linha in f:
            correta, errada = linha.strip().split(' ')
            lista_palavras_teste.append((correta, errada))
    return lista_palavras_teste

lista = cria_dados_teste('base_teste.txt')

lista_de_palavras = LeitorDeArquivos().ler_a_pasta()#.ler_o_arquivo()#
lista_de_palavras = LimpadorDeLista(lista_de_palavras).limpar()
lista_de_palavras_conjunto = sorted(list(set(lista_de_palavras)))

corretor = Corretor(lista_de_palavras)

acertou = 0

for correta, errada in lista:
    corretor.set_palavra(errada)
    palavra_corrigida = corretor.corrigir()
    if(palavra_corrigida == correta):
        acertou += 1
porcentagem = round((acertou/len(lista))*100, 2)
print(f"A taxa de acertos deste corretor é de: {porcentagem}% entre {len(lista)} palavras")

