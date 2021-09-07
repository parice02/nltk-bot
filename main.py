# coding: utf8
from datetime import datetime
from nltk_bot import MyChat


def echo(match, resp, *args, **kwargs):
    print(match, resp)


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
    [r"(.*)", ["apparemment je peux pas t'aider"], None],
]

bot = MyChat(pairs=pairs)


if __name__ == "__main__":
    print("A simple chatbot with nlkt. (no ai)\n")
    bot.converse(quit="quit")
