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
import itertools

# kalimat = pd.read_excel('data/budayaku.xlsx')
data_csv = pd.read_csv("E:\Tugas Coeg!!\TUGAS AKHIR!!!\pertanyaan_2.csv")
# print(data_csv)
kalimat = data_csv["Jawaban"]
# print(kalimat)

# new_Data = pd.DataFrame(columns=('index', 'artikel'))
# new_Data1 = pd.DataFrame(columns=('index', 'artikel'))
# new_DataFreq = pd.DataFrame(columns=('index', 'artikel'))
# new_DataAggregation = pd.DataFrame(columns=('index', 'artikel'))
# new_Matriks = pd.DataFrame(columns=('artikel'))
# matriks = pd.DataFrame(columns=('index','artikel'))

hasil_th = []
hasil_fltr = []
matriks = pd.DataFrame(columns=('index','knowledges'))
features = []
tf_value = []

#%%TOKENIZING
def getTokenize(sentence):
    preprocess = re.compile('[^a-zA-Z]+')
    x=sentence.translate(str.maketrans('','',string.punctuation)).lower()
    x = nltk.tokenize.word_tokenize(x)
    # print(x)
    return x

#%%FILTERING stop word
def getStopWord(words):
    data_stopwords = pd.read_csv("E:\Tugas Coeg!!\TUGAS AKHIR!!!\indonesian-stopwords-complete.txt")
    # listStopword =  set(stopwords.words('indonesian'))
    data_list_fix = data_stopwords.values
    removed = []
    
    for t in words:
        if t not in data_list_fix:
            removed.append(t)
    return removed

#%%UNIK
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
    # kata_stopwords = getStopWord(getTokenize(sentences))
    # kata_hasil = getStem(kata_stopwords)
    # print(kata_hasil)
    kemunculan = getFreq(kata_hasil)
    treshold = getTreshold(kemunculan)
    # return kata_hasil
    
    return getFilter(kemunculan,treshold)

#%%Aggregation
# kalimat = "Yang, aku sayang kamu"
# temp = getHasilFilterThreshold(kalimat)
# print(temp)

for idx, kal in enumerate(kalimat):
    temp = getHasilFilterThreshold(kal)
    # print(temp)
    tf_value.append(temp)
    features = [x[0] for x in temp]

features = list(OrderedDict.fromkeys(features))

for feature in features:
    matriks.insert(len(matriks.columns),feature, None, True)

for idx, kal in enumerate(kalimat):
    row_value = list(itertools.chain(*[[kal.replace("<p>"," ").replace("</p>"," ")],[x[1] for x in tf_value[idx]]]))
    columns_name = list(itertools.chain(*[["knowledges"],[x[0] for x in tf_value[idx]]]))

    new_row = pd.DataFrame([row_value], columns=columns_name)
    matriks = matriks.append(new_row, ignore_index=True)

matriks = matriks.fillna(0)
# print(matriks)
matriks.to_excel("tes_aggregasi_2.xlsx", index=False)