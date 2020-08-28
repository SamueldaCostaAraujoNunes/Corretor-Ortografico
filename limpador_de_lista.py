class LimpadorDeLista:

    def __init__(self, lista):
        self._lista = lista

    def limpar(self):
        lista_limpa = [item.lower() for item in self._lista if item.isalpha()]
        return lista_limpa
