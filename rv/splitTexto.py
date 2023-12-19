import re

class ProcesadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def obtener_palabras(self):
        palabras = re.findall(r'\b\w+\b', self.texto)
        return palabras