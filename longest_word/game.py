import random
import string
import requests

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = random.choices(string.ascii_uppercase, k=9)

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)


    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']
