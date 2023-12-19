class CombinadorPalabras:
    def __init__(self):
        self.palabras_clave = ["parque", "hospital", "cine", "universidad","plaza","hotel", "uno", "dos", "tres", "cuatro", "cinco",
                               "seis", "siete", "ocho", "nueve"]

        self.numeros_en_literal = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7,
                                   "ocho": 8, "nueve": 9}

    def combinar_palabras(self, lista_palabras):
        palabras_encontradas = [palabra for palabra in lista_palabras if palabra in self.palabras_clave]

        # Verificar si hay suficientes elementos en la lista
        if len(palabras_encontradas) >= 3:
            # Verificar si los índices existen antes de acceder a ellos
            palabra_0 = palabras_encontradas[0] if len(palabras_encontradas) > 0 else ""
            palabra_2 = palabras_encontradas[2] if len(palabras_encontradas) > 2 else ""

            resultado = palabra_0 + palabra_2
            return resultado
        else:
            return "parque"

# Ejemplo de uso
if __name__ == "__main__":
    combinador = CombinadorPalabras()
    lista_palabras = ['quiero', 'ir', 'al', 'parque', 'tres']
    resultado_combinado = combinador.combinar_palabras(lista_palabras)

    print(resultado_combinado)