import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import sys


def find_cur_crypto(words):
    cur_crypto = ""
    file = open("cryptocurrencies.txt" , "r")

    # creates list of all cryptos from cryptocurrencies.txt
    cryptos = [item.strip() for item in file.readlines()]

    # assigns cur_crypto to any crypto found in cryptos
    for word in words:
        if word in cryptos:
            cur_crypto = word

    if not cur_crypto:
        cur_crypto = "null"

    return cur_crypto;

def find_question(words):
    question = ""
    file = open("price_words.txt" , "r")

    # creates list of all 'price question' indicators from price_words.txt
    price_words = [item.strip() for item in file.readlines()]

    # assigns question to 'price' if a price indicator is found
    for word in words:
        if word in price_words:
            question = "price"

    return question;


if __name__ == '__main__':
    while True:
        # takes in input from command line
        query = input("> ")
        if query == "q":
            break;

        # tokenizes input sentence
        words = nltk.tokenize.word_tokenize(query)
        stopWords = set(nltk.corpus.stopwords.words("english"))
        for word in words:
            if word in stopWords:
                words.remove(word)

        cur_crypto = find_cur_crypto(words)
        question = find_question(words)

        # determines default question
        if not question:
            if cur_crypto != "null":
                question = "about"
            else:
                question = "off topic"

        print("~ will call '" +  question  + "' function on '" + cur_crypto + "' crypto ~\n")
