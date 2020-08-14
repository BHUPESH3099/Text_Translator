import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

recog1 = spr.Recognizer()
recog2 = spr.Recognizer()

mc = spr.Microphone(device_index=1)

with mc as source:
    print("Speak 'Hello' to initiate the Translation!")
    print("---------------------------")
    audio = recog1.listen(source)


if 'hello' in recog1.recognize_google(audio):
    recog1 = spr.Recognizer()
    translator = Translator()
    from_lang = 'en'
    to_lang = 'ge'
    with mc as source:
        print('Speak a sentence...')
        audio = recog2.listen(source)
        get_sentence = recog2.recognize_google(audio)

        try:
            get_sentence = recog2.recognize_google(audio)
            print('Phrase to be Translated: ' + get_sentence)
            text_to_translate = translator.translate(get_sentence, src = from_lang, dest = to_lang)
            text = text_to_translate.text
            speak = gTTS(text = text, lang = to_lang, slow = False)
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")
        except spr.UnknownValueError:
            print("Unable to understand the input")
        except spr.RequestError as e:
            print("Unable to provide required output".format(e))
