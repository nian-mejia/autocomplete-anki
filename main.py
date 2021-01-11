import pandas as pd 
import ipa
import translator
import polly

if __name__ == "__main__":
    words = pd.read_csv("words_anki.csv")
    words.columns = ["word"]
    words["word"] = words["word"].apply(lambda x: x.lower())
    words["word"].str.strip()
    #words = words_no_clean["word"].drop_duplicates()
    print(words.size)
    words["ipa"] = words["word"].apply(ipa.ipa_cmu)
    print("IPAS is ready now")
    words["translate"] = words["word"].apply(translator.googletrans)
    print("Translate is ready now")
    words["taskid"] = words["word"].apply(polly.polly_tarea)
    words["word"] = words["taskid"].apply(lambda x: polly.status(x, words["word"]))
    print("Sound is ready now")
    words.drop(["taskid"], axis=1)
    words = words[["word", "translate", "ipa"]]
    words.to_csv('data_clean.csv', index=False)
