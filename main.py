import pandas as pd 
import ipa
import translator
import polly

if __name__ == "__main__":
    words = pd.read_csv("words_anki.csv", sep='\t')
    words.columns = ["word"]
    words["word"] = words["word"].apply(lambda x: x.lower())
    print(words.size)
    words["ipa"] = words["word"].apply(ipa.ipa_cmu)
    print("IPAS is ready now")
    words["translate"] = words["word"].apply(translator.googletrans)
    print("Translate is ready now")
    words["taskid"] = words["word"].apply(polly.polly_tarea)
    words["word"] = words.apply(lambda x:  polly.status(x["taskid"], x["word"]), axis=1)
    print("Sound is ready now")
    words = words[["word", "translate", "ipa"]]
    words.to_csv('data_clean.csv', index=False)
