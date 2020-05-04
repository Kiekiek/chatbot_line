#%%coba
import pandas as pd
import nltk
import re
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from collections import OrderedDict
from scipy import spatial


test = "budaya khas dari jawa timur"
artikel = pd.read_csv('data/matriks.csv',sep=";")
hasil_th = []
hasil_fltr = []
matriks = [] 
features = []
tf_value = []
#%%TOKENIZING
def getTokenize(sentence):
    #preprocess = re.compile('[^a-zA-Z]+')
    x=sentence.translate(str.maketrans('','',string.punctuation)).lower()
    x = nltk.tokenize.word_tokenize(x)
    return x
#%%FILTERING stop word
def getStopWord(words):
    listStopword =  set(stopwords.words('indonesian'))
    removed = []
    
    for t in words:
        if t not in listStopword:
            removed.append(t)
    return removed

#%%UNIQUE
def getUnique(words):
    return list(OrderedDict.fromkeys(words))

#%%STEMMING
def getStem(words):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stem = []

    for t in words:
        y=(stemmer.stem(t))
        stem.append(y)
    return stem

#%%HITUNG FREKUENSI
def getFreq(words):
    return nltk.FreqDist(words).most_common()
#%%TRESHOLD
def getTreshold(words):
     return words[0][1]/2

#%%FILTER
def getFilter(word,th):
    hasil = [x for x in word if x[1]>=th]
    return hasil

#%%MATRIKS
def getHasilFilterThreshold(sentences):
    kata_hasil = getStem(getStopWord(getTokenize(sentences.replace("<p>"," ").replace("</p>"," "))))
    kemunculan = getFreq(kata_hasil)
    treshold = getTreshold(kemunculan) 
    return getFilter(kemunculan,treshold)

def getHasil(sentences):
    kata_hasil = getStem(getStopWord(getTokenize(sentences.replace("<p>"," ").replace("</p>"," "))))
    kemunculan = getFreq(kata_hasil)
    return kemunculan
#%%
hasil = getHasilFilterThreshold(test)
hasil


# %%
                                                                                                                                                                                                                                                                                                                    
def similarity(feature,key,value):
    dist = []
    

    kamus_selected = feature[key]

    for key, kam in kamus_selected.iterrows():
        feature = list(kam.values)
        result = 1 - spatial.distance.cosine(value, feature)
        dist.append(result)

    word_df = artikel[['article']].copy()
    word_df['dist'] = dist

    return word_df

kata_tes = []
sim_1 = []
sim_2 = []
sim_3 = []
sim_4 = []
sim_5 = []
sim_6 = []
sim_7 = []
sim_8 = []
sim_9 = []
sim_10 = []


# print(key, data.values[0].lower())
kata = test.lower()
key = getHasil(kata)


art = artikel['article'].tolist()
kata = list(artikel.columns)
feature = artikel.drop('article', axis=1)

query_key = [] 
query_val = [] 
for k in key:
    query_key.append(k[0])
    query_val.append(k[1])

sim = similarity(feature, query_key, query_val)
sim = sim.sort_values(by=['dist'], ascending=False)
sim = sim[:10].values
print(sim)

#%%
dataset = pd.DataFrame({'Artikel': sim[:, 0], 'Similarity': sim[:, 1]})
print(dataset)


#dataset.to_excel('data/coba1.xlsx')

