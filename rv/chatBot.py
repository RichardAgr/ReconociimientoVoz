import re
import random

class ChatBot:
    def __init__(self):
        self.highest_prob = {}
        self.initialize_responses()

    def initialize_responses(self):
        self.response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response=True)
        self.response('Estoy bien y tú?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        self.response('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        self.response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

         # Saludos y preguntas iniciales
        self.response("hola", ["hola", "klk", "saludos", "buenas"], single_response=True)
        self.response("estoy bien y tú?",["como", "estas", "va", "vas", "sientes"],required_words=["como"],)
        self.response("que bien", ["igual", "bien", "igualemente"], single_response=True)
        # Sobre el servicio del taxi
        self.response("si estoy de servicio",["servicio", "disponible", "Esta libre"],required_words=["esta"],)
        self.response("esta bien, subase", ["direccion", "destino", "ubicacion", "lugar"], required_words=["direccion"],)
        # Preguntas sobre costos y tarifas
        self.response("lo siento, pero nuestros precios son fijos",["regatear", "costo", "descuento", "rebajar", "negociar"],required_words=["descuento"],)
        self.response("el costo dependerá del destino y la distancia",["cuanto", "costo", "precio", "tarifa", "cobra"],required_words=["cuanto"], )
        # Tiempo estimado de llegada
        self.response("llegaremos en aproximadamente 10 minutos",["cuanto", "tiempo", "llegar", "demora"],required_words=["tiempo"],)
        # Sobre el método de pago
        self.response("aceptamos efectivo y tarjetas",["pago", "efectivo", "tarjeta", "metodo"],single_response=True,)
        # Fin de la carrera
        self.response("hemos llegado a su destino",["llegamos", "aqui", "destino", "final"],single_response=True,)
        # Dejar comentarios
        self.response("si desea puede dejar un comentario o valoración sobre nuestro servicio en nuestra pagina",["comentario", "valoracion", "opinion"],required_words=["comentario"],)
        # Objetos perdidos
        self.response("Si ha olvidado algo en el vehículo puedo buscarlo ahora",["olvidado", "objeto", "perdido"],required_words=["olvidado"],)
        #salir o aceptar el viaje
        self.response("esta bien saldremos a su destino", ["vamos", "rápido"],required_words=["vamos"])
        # Agradecimientos y despedidas
        self.response("siempre a la orden",["gracias", "agradezco", "thanks"],single_response=True,)
        self.response("que tenga un buen dia",["adios", "chao", "hasta", "luego"],single_response=True,)

        self.response("iremos al destino que seleciono con gusto", ["iremos", "destino"],required_words=["destino"])

        self.response("estamos saliendo de la estacion de taxi del norte", ["norte"],required_words=["norte"])

    def get_response(self ,user_input):
        split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        response = self.check_all_messages(split_message)
        return response

    def message_probability(self,user_message, recognized_words, single_response=False, required_word=[]):
        message_certainty = 0
        has_required_words = True

        for word in user_message:
            if word in recognized_words:
                message_certainty +=1

        percentage = float(message_certainty) / float (len(recognized_words))

        for word in required_word:
            if word not in user_message:
                has_required_words = False
                break
        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def response(self, bot_response, list_of_words, single_response=False, required_words=[]):
        self.highest_prob[bot_response] = self.message_probability(
            self.highest_prob.get("message", []), list_of_words, single_response, required_words)

    def check_all_messages(self, message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = self.message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('Estoy bien y tu?', ['cómo', 'estas', 'va', 'vas', 'sientes'], required_words=['cómo'])
        response('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        response('ella no te ama',['amor','querida','alegre'], required_words=['amor'])
        # Saludos y preguntas iniciales
        response("hola", ["hola", "klk", "saludos", "buenas"], single_response=True)
        response("estoy bien y tú?",["como", "estas", "va", "vas", "sientes"],required_words=["como"],)
        response("que bien", ["igual", "bien", "igualemente"], single_response=True)
        # Sobre el servicio del taxi
        response("si estoy de servicio",["servicio", "disponible", "Esta libre"],required_words=["esta"],)
        response("esta bien, subase", ["direccion", "destino", "ubicacion", "lugar"], required_words=["direccion"],)
        # Preguntas sobre costos y tarifas
        response("lo siento, pero nuestros precios son fijos",["regatear", "costo", "descuento", "rebajar", "negociar"],required_words=["descuento"],)
        response("el costo dependerá del destino y la distancia",["cuanto", "costo", "precio", "tarifa", "cobra"],required_words=["cuanto"], )
        # Tiempo estimado de llegada
        response("llegaremos en aproximadamente 10 minutos",["cuanto", "tiempo", "llegar", "demora"],required_words=["tiempo"],)
        # Sobre el método de pago
        response("aceptamos efectivo y tarjetas",["pago", "efectivo", "tarjeta", "metodo"],single_response=True,)
        # Fin de la carrera
        response("hemos llegado a su destino",["llegamos", "aqui", "destino", "final"],single_response=True,)
        # Dejar comentarios
        response("si desea puede dejar un comentario o valoración sobre nuestro servicio en nuestra pagina",["comentario", "valoracion", "opinion"],required_words=["comentario"],)
        # Objetos perdidos
        response("Si ha olvidado algo en el vehículo puedo buscarlo ahora",["olvidado", "objeto", "perdido"],required_words=["olvidado"],)
        #salir o aceptar el viaje
        response("esta bien saldremos a su destino", ["vamos", "rápido"],required_words=["vamos"])
        # Agradecimientos y despedidas
        
        response("siempre a la orden",["gracias", "agradezco", "thanks"],single_response=True,)
        response("que tenga un buen dia",["adios", "chao", "hasta", "luego"],single_response=True,)
        

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return self.unknown() if highest_prob[best_match] < 1 else best_match


    def unknown(self):
        response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
        return response
    



# Pruebas
if __name__ == "__main__":
    chatbot = ChatBot()
    while True:
        user_input = input('You: ')
        response = chatbot.get_response(user_input)
        print("Bot: " + response)



