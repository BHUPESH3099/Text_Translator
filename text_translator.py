#pip install googletrans                #if this module is not working use alpha version
#pip install googletrans==3.1.0a0       #alpha version
from googletrans import Translator


sentence = str(input("say ....... "))

translator = Translator()

translated_sentence = translator.translate(sentence, src='en', dest='ge')

print(translated_sentence)
