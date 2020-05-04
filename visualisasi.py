from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

app = Flask(__name__)
bot = ChatBot("Kiek")
bot.set_trainer(ListTrainer)

for files in os.listdir("E:\Tugas Coeg!!\TUGAS AKHIR!!!\Teknis Chatbot\english"):
    data = open("E:\Tugas Coeg!!\TUGAS AKHIR!!!\Teknis Chatbot\english" + files, 'r').readlines()
    bot.train(data)

while True:
    message = input('\t\t\tYou:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('Kiek: ', reply)
    if message.strip() == 'Bye':
        print('Kiek: Bye')
        break