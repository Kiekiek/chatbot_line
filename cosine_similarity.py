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

# X = "I love horror movies"
# Y = "Lights out is a horror movie"

query = "Gangguan kecemasan itu apa?"
data_csv = pd.read_csv("E:\Tugas Coeg!!\TUGAS AKHIR!!!\pertanyaan.csv")
kalimat = data_csv[["Jawaban"]]
# print(kalimat)

hasil_th = []
hasil_fltr = []
matriks = pd.DataFrame(columns=('index','knowledges'))
features = []
tf_value = []

# %%TOKENIZING
def getTokenize(sentence):
    preprocess = re.compile('[^a-zA-Z]+')
    x = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    x = nltk.tokenize.word_tokenize(x)
    # print(x)
    return x

# %%FILTERING stop word
def getStopWord(words):
    data_stopwords = pd.read_csv("E:\Tugas Coeg!!\TUGAS AKHIR!!!\indonesian-stopwords-complete.txt")
    # listStopword =  set(stopwords.words('indonesian'))
    data_list_fix = data_stopwords.values
    removed = []

    for t in words:
        if t not in data_list_fix:
            removed.append(t)
    return removed

# %%UNIK
def getUnique(words):
    return list(OrderedDict.fromkeys(words))


# %%STEMMING
def getStem(words):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stem = []

    for t in words:
        y = (stemmer.stem(t))
        stem.append(y)
    return stem

# %%HITUNG FREKUENSI
def getFreq(words):
    return nltk.FreqDist(words).most_common()

# %%TRESHOLD
def getTreshold(words):
    return words[0][1] / 2

# %%FILTER
def getFilter(word, th):
    hasil = [x for x in word if x[1] >= th]
    return hasil

# %%MATRIKS
def getHasilFilterThreshold(sentences):
    kata_hasil = getStem(getStopWord(getTokenize(sentences.replace("<p>", " ").replace("</p>", " "))))
    # kata_stopwords = getStopWord(getTokenize(sentences))
    # kata_hasil = getStem(kata_stopwords)
    # print(kata_hasil)
    kemunculan = getFreq(kata_hasil)
    treshold = getTreshold(kemunculan)
    # return kata_hasil

    # return kata_hasil
    return getFilter(kemunculan, treshold)

filter_query = getHasilFilterThreshold(query)
print(filter_query)

# for idx, kal in enumerate(kalimat['Jawaban']):
#     temp = getHasilFilterThreshold(kal)

# X_list = word_tokenize(X)
# Y_list = word_tokenize(Y)
# print(X_list)
# print(Y_list)
#
# sw = stopwords.words('english')
# l1 =[];l2 =[]
#
# X_set = {w for w in X_list if not w in sw}
# Y_set = {w for w in Y_list if not w in sw}
#
# print("X set : ")
# print(X_set, "\n")
# print("Y set : ")
# print(Y_set, "\n")
#
# rvector = X_set.union(Y_set)
# print(rvector)
# for w in rvector:
#     if w in X_set: l1.append(1)
#     else: l1.append(0)
#     if w in Y_set: l2.append(1)
#     else: l2.append(0)
# c = 0
#
# # print(l1)
# # print(l2)
#
# for i in range(len(rvector)):
#         c+= l1[i]*l2[i]
# cosine = c / float((sum(l1)*sum(l2))**0.5)
# print("similarity: ", cosine)