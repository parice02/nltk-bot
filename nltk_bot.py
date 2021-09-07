# -*- coding: utf8 -*

import random
from re import compile, I

from nltk.chat.util import Chat, reflections

random.seed(0)

abbreviation = {
    "slt": "salut",
    "xlt": "salut",
    "bsr": "bonsoir",
    "bjr": "bonjour",
    "helo": "hello",
    "a plus": "à plus",
    "aplus": "à plus",
    "àplus": "à plus",
    "cmt": "comment",
    "cmmt": "comment",
}

reflect = {
    "tu es": "je suis",
    "tu vas": "je vais",
}


class MyChat(Chat):
    """
    * nltk.chat.util.Chat extension
    * url: https://www.nltk.org/_modules/nltk/chat/util.html
    """

    def __init__(self, pairs=[], reflections=reflections):
        self._pairs = [(compile(x, I), y, z) for (x, y, z) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()
        

    def replace_abbreviation(self, statement: str) -> str:
        if not isinstance(statement, str):
            raise TypeError()

        for word in statement.split():
            if word in abbreviation:
                statement = statement.replace(word, abbreviation[word])

        return statement

    def respond(self, statement: str) -> str:
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        statement = self.replace_abbreviation(statement)
        for (pattern, responses, callback_) in self._pairs:
            match = pattern.match(statement)

            # did the pattern match?
            if match:
                response = random.choice(responses)  # pick a random response
                response = self._wildcards(response, match)  # process wildcards

                # fix munged punctuation at the end
                if response[-2:] == "?.":
                    response = response[:-2] + "."
                if response[-2:] == "??":
                    response = response[:-2] + "?"

                # execute the callback
                if callback_:
                    callback_(match.string, response)

                ##
                return response

    # Hold a conversation with a chatbot
    def converse(
        self, quit: str = "quit", prompt: str = ">> you (tape `quit` to exit):  "
    ):
        user_input = ""
        while user_input != quit:
            try:
                user_input = input(prompt)
            except EOFError:
                break
            if user_input:
                print(self.respond(user_input))
