import eng_to_ipa as engipa

def cleaner(ipa):
    ipa = ipa.replace("r", "ɹ")
    if not ipa:
        return ipa
    elif "/" not in ipa:
        ipa = "/"+ipa+"/"

    return ipa

def ipa_cmu(word_input):
    def palabra(word):
        palabra = engipa.ipa_list(word)
        return palabra 

    def frase(word):
        oracion = engipa.convert(word)
        oracion = cleaner(oracion)
        return str(oracion)

    word = word_input.lower()
    word_list = word.split()

    if len(word_list) == 1:
        palabra = " ".join(map(str, palabra(word)))
        p = palabra.replace("[", "")
        p = p.replace("]", "")
        return p
    elif len(word_list) >= 2:
        frase = ''.join(map(str, frase(word)))
        return frase
    else:
        return None
