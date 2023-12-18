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
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

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



