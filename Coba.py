import nltk
import string
import pandas as pd
import numpy as np
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

data_csv = pd.read_csv("E:\Tugas Coeg!!\TUGAS AKHIR!!!\pertanyaan.csv")
data_stopwords = pd.read_csv("E:\Tugas Coeg!!\TUGAS AKHIR!!!\indonesian-stopwords-complete.txt")
data_list_fix = data_stopwords.values
# print(data_list_fix)

coba = pd.DataFrame(data_csv, columns=["Jawaban"])
# print(coba)

factory_stemmer = StemmerFactory()
factory_stopwords = StopWordRemoverFactory()
stemmer = factory_stemmer.create_stemmer()
stopwords = factory_stopwords.create_stop_word_remover()

query_iteration = 0
while query_iteration < len(coba):
    query1 = coba.values[query_iteration][0]
    print(query1, "\n")
    hasil_punctuation = query1.translate(str.maketrans("","",string.punctuation))

    print("Hasil Punctuation :")
    print(hasil_punctuation, "\n")

    case_folding = hasil_punctuation.lower()
    print("Hasil Case :")
    print(case_folding, "\n")

    tes = case_folding.split(' ')
    print("Hasil Tokenization :")
    print(tes, "\n")

    for word in tes:
        if word in data_list_fix:
            # print(word)
            tes.remove(word)
    print("Hasil Stop")
    print(tes, "\n")

    gabung_string = ""
    for i in tes:
        gabung_string += i + " "
    print("Kalimat digabungkan menjadi String :")
    print(gabung_string, "\n")

    hasil_stemmer = stemmer.stem(gabung_string)
    print("Hasil Stemmer :")
    print(hasil_stemmer, "\n")

    # bagOfWordsA = query1.split(' ')
    bagOfWords = hasil_stemmer.split(' ')
    uniqueWords = set(bagOfWords).union(set(bagOfWords))
    print(uniqueWords, "\n")

    numOfWords = dict.fromkeys(uniqueWords, 0)
    for word in bagOfWords:
        numOfWords[word] += 1
    print(numOfWords, "\n")

    listOfWords = list(numOfWords.items())
    # print(listOfWords, "\n")

    sorted_by_second = sorted(listOfWords, key=lambda tup: tup[1],reverse=True)
    print(sorted_by_second, "\n")

    value = sorted_by_second[0][1]
    treshold = value / 2

    i = 0
    while i < len(sorted_by_second):
        # print(treshold)
        if value < treshold:
            del sorted_by_second[i]
            # print("asdad")
        i+=1

    print("Hasil tresholdnya adalah :",treshold)

    query_iteration+=1

# hasil_punctuation = query1.translate(str.maketrans("","",string.punctuation))
# print(hasil_punctuation)
#
# case_folding = hasil_punctuation.lower()
# # print("Hasil Case")
# print(case_folding, "\n")
# tes = case_folding.split(' ')
# print(tes)
#
# for word in tes:
#     if word in data_list_fix:
#         # print(word)
#         tes.remove(word)
# print("Hasil Stop")
# print(tes, "\n")
#
# gabung_string = ""
# for i in tes:
#     gabung_string += i + " "
# print("Kalimat digabungkan menjadi String :")
# print(gabung_string, "\n")
#
# hasil_stemmer = stemmer.stem(gabung_string)
# print("Hasil Stemmer :")
# print(hasil_stemmer, "\n")
#
# # bagOfWordsA = query1.split(' ')
# bagOfWords = hasil_stemmer.split(' ')
# uniqueWords = set(bagOfWords).union(set(bagOfWords))
# print(uniqueWords)
#
# numOfWords = dict.fromkeys(uniqueWords, 0)
# for word in bagOfWords:
#     numOfWords[word] += 1
# print(numOfWords)
#
# listOfWords = list(numOfWords.items())
#
# print(listOfWords)
#
# sorted_by_second = sorted(listOfWords, key=lambda tup: tup[1],reverse=True)
# print(sorted_by_second)
#
# i = 0
# while i < len(sorted_by_second):
#     treshold = sorted_by_second[i][1] / 2
#     print(treshold)
#     i+=1

# def selection_port(x):
#     for i in range(len(x)):
#         swap = i + np.argmin(x[i:])
#         (x[i], x[swap]) = (x[swap], x[i])
#     return x

# x = np.array([2, 5, 11, 1, 3])
# sort = numOfWords.so
# print(numOfWords)

# stop = stopwords.remove(case_folding)
# print(stop)

# tokens = nltk.tokenize.word_tokenize(stop)
# # print(tokens)
#
# gabung_string = ""
# for i in tokens:
#     gabung_string += i + " "
# print("Kalimat digabungkan menjadi String :")
# print(gabung_string, "\n")
#
# hasil_stemmer = stemmer.stem(gabung_string)
# print("Hasil Stemmer :")
# print(hasil_stemmer, "\n")
#
# bagOfWordsA = query1.split(' ')
# bagOfWordsB = hasil_stemmer.split(' ')
# uniqueWords = set(bagOfWordsB).union(set(bagOfWordsB))
# print(uniqueWords)
#
# numOfWordsB = dict.fromkeys(uniqueWords, 0)
# for word in bagOfWordsB:
#     numOfWordsB[word] += 1
# print(numOfWordsB)

# kalimat_1 = "[MOJOK.co] Manfaat jogging setiap pagi yang pertama adalah meredakan stres. Olahraga itu seperti kode bagi " \
#           "tubuh untuk memproduksi hormon endorfin, agen perangsang rasa bahagia. Dilakukan di pagi hari, ketika udara " \
#           "masih bersih, sejuk, jalanan lengang, gunung terlihat jelas di sebelah utara, manfaat jogging bisa kamu " \
#           "rasakan secara maksimal."
#
# kalimat_2 = "Valentino Rossi tampak sangat menyesal setelah terjatuh pada lap terakhir MotoGP Prancis 2017"
#
# # Input Kalimat
# input_coba = input("Masukkan Kalimat-nya : ")
#
# # Ini digunakan untuk membuat semua kalimat menjadi lowercase (huruf kecil semua)
# case_folding = input_coba.lower()
# print("\nKalimat yang sudah di Case Folding :")
# print(case_folding, "\n")
#
# # Proses StopWords Bahasa Indonesia
# stop = stopwords.remove(case_folding)
# print("Kalimat yang sudah di StopWords :")
# print(stop, "\n")
#
# # Proses Tokenization
# tokens = nltk.tokenize.word_tokenize(stop)
# print("Kalimat yang sudah di Tokenization :")
# print(tokens, "\n")
#
# # Menggabungkan output array token ke string kembali
# gabung_string = ""
# for i in tokens:
#     gabung_string += i + " "
# print("Kalimat digabungkan menjadi String :")
# print(gabung_string, "\n")
#
# # Proses Stemming Bahasa Indonesia
# hasil_stemmer = stemmer.stem(gabung_string)
# print("Hasil Stemming :")
# print(hasil_stemmer)
# # print(hasil_stemmer.split())

# Proses TF

# documentA = 'the man went out for a walk'
# documentB = 'the children sat around the fire'
#
# bagOfWordsA = documentA.split(' ')
# bagOfWordsB = documentB.split(' ')
#
# print(bagOfWordsA)
# print(bagOfWordsB)
#
# uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
# print(uniqueWords)
#
# numOfWordsA = dict.fromkeys(uniqueWords, 0)
# for word in bagOfWordsA:
#     numOfWordsA[word] += 1
# print(numOfWordsA)
#
# numOfWordsB = dict.fromkeys(uniqueWords, 0)
# for word in bagOfWordsB:
#     numOfWordsB[word] += 1
# print(numOfWordsB)
#
# def computeTF(wordDict, bagOfWords):
#     tfDict = {}
#     bagOfWordsCount = len(bagOfWords)
#     for word, count in wordDict.items():
#         tfDict[word] = count / float(bagOfWordsCount)
#     return tfDict
#
# tfA = computeTF(numOfWordsA, bagOfWordsA)
# print(tfA)

# Namun kemunculan tanda baca sebaiknya dihindari karena dapat nantinya mengganggu proses perhitungan dalam penerapan
# algoritma Text Mining, kita bisa melakukan filtering terhadap kalimat tersebut untuk menghilangkan tanda baca
# dan karakter non-alfabet.
# kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()

# Setelah melalui proses Tokenization kita bisa mendapatkan jumlah kemunculan setiap tokennya.
# kemunculan = nltk.FreqDist(tokens)
# print(tokens)
# print(kemunculan.most_common())