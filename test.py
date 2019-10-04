import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import sys


def find_cur_crypto(words):
    cur_crypto = ""
    file = open("cryptocurrencies.txt" , "r")

    cryptos = [item.strip() for item in file.readlines()]

    for word in words:
        if word in cryptos:
            cur_crypto = word

    return cur_crypto;

def find_question(words):
    question = ""
    file = open("price_words.txt" , "r")

    price_words = [item.strip() for item in file.readlines()]

    for word in words:
        if word in price_words:
            question = "price"

    return question;


if __name__ == '__main__':

    input = input("> ")

    #tokenizes input sentence
    words = nltk.tokenize.word_tokenize(input)
    stopWords = set(nltk.corpus.stopwords.words("english"))
    for word in words:
        if word in stopWords:
            words.remove(word)

    #determines crypto of input
    cur_crypto = find_cur_crypto(words)

    #determines question type of input
    question = find_question(words)


    if not question:
        if not cur_crypto:
            question = "idk"
        else:
            question = "about"

    if not cur_crypto:
        cur_crypto = "none"

    print("crypto: " + cur_crypto)
    print ("question type: " + question)
