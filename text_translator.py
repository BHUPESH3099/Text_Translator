from googletrans import Translator


sentence = str(input("say ....... "))

translator = Translator()

translated_sentence = translator.translate(sentence, src='en', dest='ge')

print(translated_sentence)