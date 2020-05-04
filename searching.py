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

knowledge = "apa itu depresi"
data_query = pd.read_csv("E:\Tugas Coeg!!\TUGAS AKHIR!!!\pertanyaan_2.csv")
# print(knowledge)
# print(data_query)
query_list = data_query["Jawaban"]
# print(query_list)
hasil_th = []
hasil_fltr = []
matriks = []
features = []
tf_value = []
query_key = []
query_val = []

#%%TOKENIZING
def getTokenize(sentence):
    #preprocess = re.compile('[^a-zA-Z]+')
    x=sentence.translate(str.maketrans('','',string.punctuation)).lower()
    x = nltk.tokenize.word_tokenize(x)
    return x
#%%FILTERING stop w*ord
def getStopWord(words):
    data_stopwords = pd.read_csv("E:\Tugas Coeg!!\TUGAS AKHIR!!!\indonesian-stopwords-complete.txt")
    # listStopword =  set(stopwords.words('indonesian'))
    data_list_fix = data_stopwords.values
    removed = []

    for t in words:
        if t not in data_list_fix:
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

# %%

def similarity(feature,key,value):
    dist = []

    kamus_selected = feature[key]

    for key, kam in kamus_selected.iterrows():
        feature = list(kam.values)
        result = 1 - spatial.distance.cosine(value, feature)
        dist.append(result)

    word_df = knowledge[['knowledges']].copy()
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

hasil = getHasilFilterThreshold(knowledge)

# print(key, data.values[0].lower())

art = data_query['knowledges'].tolist()
kata = list(data_query.columns)
feature = data_query.drop('knowledges', axis=1)

for idx, kal in enumerate(data_query):
    key = getHasil(kal)
    print(key, kal)

    for k in key:
        try:
            cek = feature[[k[0]]]
            query_key.append(k[0])
            query_val.append(k[1])
        except:
            continue

    sim = similarity(feature, query_key, query_val)
    sim = sim.sort_values(by=['dist'], ascending=False)
    sim = sim[:3].values
    print(sim, "\n")

    dataset = pd.DataFrame({'Knowledge': sim[:, 0], 'Similarity': sim[:, 1]})
    print(dataset)
    # dataset.to_excel('coba.xlsx')
# kata = test.lower()
# key = getHasil(test)
#
# art = knowledge['knowledges'].tolist()
# kata = list(knowledge.columns)
# # print(kata)
# print(feature)
#
# query_key = []
# query_val = []
# for k in key:
#     query_key.append(k[0])
#     query_val.append(k[1])
#
# sim = similarity(feature, query_key, query_val)
# sim = sim.sort_values(by=['dist'], ascending=False)
# sim = sim[:10].values
# print(sim)
#
# #%%
# print(dataset)

