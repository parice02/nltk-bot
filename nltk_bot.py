# coding: uft8


import random
from re import compile, IGNORECASE as i
from typing import List, Dict

from nltk.chat.util import Chat, reflections

random.seed(0)

abrv: Dict[str, str] = {
    'slt': 'salut',
    'xlt': 'salut',
    'bsr': 'bonsoir',
    'bjr': 'bonjour',
    'helo': 'hello',
    'a plus': 'à plus',
    'aplus': 'à plus',
    'àplus': 'à plus',
    'cmt': 'comment',
    'cmmt': 'comment'
}

reflect: Dict[str, str] = {
    'tu es': 'je suis',
    'tu vas': 'je vais',
}


class MyChat(Chat):
    """
    * nltk.chat.util.Chat extension
    * url: https://www.nltk.org/_modules/nltk/chat/util.html
    """

    def __init__(self, pairs: List, reflections: Dict = reflections) -> None:
        self._pairs = [(compile(x, i), y, z) for (x, y, z) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def replace_abrv(self, string: str)->str:

        if not isinstance(string, str):
            raise TypeError()

        for word in string.split():
            if word in abrv:
                string = string.replace(word, abrv[word])

        return string

    def respond(self, str_: str) -> str:
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        str_ = self.replace_abrv(str_)
        for (pattern, response, callback_) in self._pairs:
            match = pattern.match(str_)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"

                # execute the callback
                if callback_:
                    callback_(match.string, resp)

                ##
                return resp

    # Hold a conversation with a chatbot
    def converse(self, quit: str = "quit", prompt: str = ">> you:  ") -> None:
        user_input = ""
        while user_input != quit:
            try:
                user_input = input(prompt)
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.?":
                    user_input = user_input[:-1]
                print(self.respond(user_input))
