# -*- coding: utf8 -*

from datetime import datetime

from nltk_bot import MyChat


def echo(match, response):
    """should return a response"""
    return f"{match} - {response}"


pairs = [
    [
        r"(quit|au revoir|bye|à plus)",
        [
            "bye",
            "merci pour l'échange",
            "à la prochaine",
            "à plus",
            "bye bye",
            "au revoir",
        ],
        None,
    ],
    [
        r"(bon(jour|soir)|salut|hey|hello)([\.\!\? ]?)",
        ["salut", "bonjour", "hello"],
        echo,
    ],
    [
        r"comment (vas[- ]tu|allez[- ]vous|tu vas|vous allez)([\?\. ]?)",
        ["assez bien pour une machine", "assez d'électron en moi"],
        None,
    ],
    [
        r"(quelle heure est[- ]il)([\?\. ]?)",
        [f'il est {datetime.now().time().isoformat(timespec="minutes")}'],
        None,
    ],
    [
        r"(.*)",
        ["apparemment je peux pas t'aider", "je ne suis qu'un simple bot sans IA"],
        None,
    ],
]

bot = MyChat(pairs=pairs)


if __name__ == "__main__":
    print("A simple chatbot with nltk. (no ai)\n")
    bot.converse(quit="quit")
