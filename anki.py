import pandas as pd 
import ipa
import translator
import polly

def leer_csv(root):  
    data = pd.DataFrame(root)  
    data.columns = ["word"]
    return data


if __name__ == "__main__":
    #words = leer_csv("words_anki.csv")
    words = pd.DataFrame(["home", "paintbrushes"], columns = ["word"])
    words["ipa"] = words["word"].apply(ipa.ipa_cmu)
    words["translate"] = words["word"].apply(translator.googletrans)
    words["sounds"] = words["word"].apply(polly.polly_tarea)
    print(words)