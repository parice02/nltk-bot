# -*- coding: utf8 -*

from nltk_bot import MyChat
from tools import pairs

chat_bot = MyChat(pairs=pairs)

if __name__ == "__main__":
    print("A simple chatbot with nltk. (no ai)\n")
    chat_bot.converse(quit="quit")
