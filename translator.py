from googletrans import Translator
from deep_translator import GoogleTranslator


def solicitud(word):
    word = word.lower()

    translator = Translator()
    language = translator.detect(word)
    language = language.lang

    if type(language) == list:
        if language[0] == "en" or language[0] == "es":
            return word, language[0]
        else:
            solicitud(word)
    else:
        if language == "en" or language == "es":
            return word, language
        else:
            solicitud(word)


def do_translat(translator, word):
    try:
        word, language = solicitud(word)
    except TypeError:
        word, language = solicitud(word)

    if language == "en":
        dest = "es"
    else:
        dest = "en"
    
    try:
        translated = translator(source=language, target=dest).translate(word)
        return translated
    except:
        print("error")
        return "error"

def googletrans(word):
    translated = do_translat(GoogleTranslator, word)
    print(translated.capitalize())
    return translated.capitalize()

