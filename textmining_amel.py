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

kalimat = pd.read_excel('data/budayaku.xlsx')
new_Data = pd.DataFrame(columns=('index', 'artikel'))
new_Data1 = pd.DataFrame(columns=('index', 'artikel'))
new_DataFreq = pd.DataFrame(columns=('index', 'artikel'))
new_DataAggregation = pd.DataFrame(columns=('index', 'artikel'))
new_Matriks = pd.DataFrame(columns=('artikel'))
matriks = pd.DataFrame(columns=('index','artikel'))
hasil_th = []
hasil_fltr = []
matriks = [] 
features = []
tf_value = []
#%%TOKENIZING
def getTokenize(sentence):
    preprocess = re.compile('[^a-zA-Z]+')
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
    kemunculan = getFreq(kata_hasil)
    treshold = getTreshold(kemunculan) 
    
    return getFilter(kemunculan,treshold)


#%%Aggregation
for kal in kalimat['post_content']:
    temp = getHasilFilterThreshold(kal)
    tf_value.append(temp)
    features = [x[0] for x in temp]

features = list(OrderedDict.fromkeys(features))
for feature in features:
    matriks.insert(len(matriks.columns),feature, None, True)

for idx, kal in enumerate(kalimat['post_content']):
    row_value = list(itertools.chain(*[[kal.replace("<p>"," ").replace("</p>"," ")],[x[1] for x in tf_value[idx]]]))
    columns_name = list(itertools.chain(*[["article"],[x[0] for x in tf_value[idx]]]))
    
    new_row = pd.DataFrame([row_value], columns=columns_name)
    matriks = matriks.append(new_row, ignore_index=True)

matriks = matriks.fillna(0)

matriks.to_excel("hasilaggregation.xlsx", index=False)