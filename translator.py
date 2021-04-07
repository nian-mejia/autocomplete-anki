from deep_translator import GoogleTranslator

def googletrans(word):
    translater = GoogleTranslator(source="en", target="es")
    word_trans = translater.translate(word)
    print(word_trans)
    return word_trans

