from datetime import datetime
from nltk_bot import MyChat


def echo(match, response):
    """should return a response"""
    return f"{match} - {response}"


def what_time(match, response):
    """ """
    time = datetime.now().time().isoformat(timespec="minutes")
    return response + "\t" + time


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
        ["il est"],
        what_time,
    ],
    [
        r"(.*)",
        ["apparemment je peux pas t'aider", "je ne suis qu'un simple bot sans IA"],
        None,
    ],
]


