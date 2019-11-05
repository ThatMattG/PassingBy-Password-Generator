import random
from errors import *

"""

Please refer to main.py for important infromation about this tool's security.

"""


class PasswordGenerator:

    __letters = "qwertyuiopasdfghjklzxcvbnm"
    __capital_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    __numbers = "1234567890"
    __special_chars = "!@#$%&"
    __words = list(open("filtered_words.txt", "r"))

    __default_sources = (
        # __letters,
        __capital_letters,
        __numbers,
        # __special_chars,
        __words
    )

    __default_properties = {
        "length": 18,
        "min_word_length": 4,
        "max_word_length": 10,
        "letters_to_numbers": True,
        "letters_to_special_chars": False
    }

    __affirmative = [
        "True", "true", "yes", "y", "1"
    ]

    __negative = [
        "False", "false", "none", "no", "n", "0", "-1"
    ]

    def __init__(self, args):
        if args == None:
            pass

        self._sources = []
        self.set_sources(args)

        self.set_properties(args)

        self._rng = random.SystemRandom()

        if self._min_word_length > self._max_word_length:
            raise InvalidWordLength

    def set_sources(self, args):
        if args == None:
            self._sources = list(self.__class__.__default_sources)
            return

        available_sources = {
            self.__class__.__letters: args.letters,
            self.__class__.__capital_letters: args.capital_letters,
            self.__class__.__numbers: args.numbers,
            self.__class__.__special_chars: args.special_chars,
        }

        for source, arg in available_sources.items():
            if self.using_source(source, arg):
                self._sources.append(source)

        if self.using_source(self.__class__.__words, args.words):
            self._sources.append(self.__class__.__words)

    def set_properties(self, args):
        if args == None:
            self.set_default_properties()
            return

        defaults = self.__class__.__default_properties

        self._length = self.initial_property_value(
            args.length, defaults["length"]
        )
        self._min_word_length = self.initial_property_value(
            args.min_word_length, defaults["min_word_length"]
        )
        self._max_word_length = self.initial_property_value(
            args.max_word_length, defaults["max_word_length"]
        )
        self._letters_to_numbers = self.initial_property_value(
            args.letters_to_numbers, defaults["letters_to_numbers"]
        )
        self._letters_to_special_chars = self.initial_property_value(
            args.letters_to_special_chars, defaults["letters_to_special_chars"]
        )

    def using_source(self, source, argument):
        using = False

        if source in self.__class__.__default_sources:
            using = True

        if self.is_affirmative(argument):
            using = True
        elif self.is_negative(argument):
            using = False
        elif argument is not None:
            raise InvalidArgumentValue(
                f"Invalid argument value '{argument}'. To enable, use 'true' or '1'. To disable, use 'false' or '0'"
            )

        return using

    def initial_property_value(self, argument, default):
        if argument is None:
            value = default
        elif self.is_affirmative(argument):
            value = True
        elif self.is_negative(argument):
            value = False
        elif argument.isdigit and type(default) == int:
            value = abs(int(argument))
        else:
            raise InvalidArgumentValue(
                f"Invalid argument value '{argument}'. To enable, use 'true' or '1'. To disable, use 'false' or '0'"
            )

        return value

    @classmethod
    def is_affirmative(cls, string):
        return string in cls.__affirmative

    @classmethod
    def is_negative(cls, string):
        return string in cls.__negative

    def set_default_properties(self):
        properties = self.__class__.__default_properties
        self._length = properties["length"]
        self._min_word_length = properties["min_word_length"]
        self._max_word_length = properties["max_word_length"]
        self._letters_to_numbers = properties["letters_to_numbers"]
        self._letters_to_special_chars = properties["letters_to_special_chars"]

    def produce_password(self):
        password = ""
        desired_length = self._length

        if len(self._sources) < 2:
            raise InsufficientSources("Please allow at least two sources")

        while len(password) < desired_length:
            length_difference = desired_length - len(password)
            password += self.make_password_component(length_difference)

        return password

    def make_password_component(self, max_length):
        source = self._rng.choice(list(self._sources))
        selection = random.choice(source).strip()

        if not self.component_length_ok(selection, max_length):
            selection = ""

        selection = self.replace_letters_with_numbers(selection)
        selection = self.replace_letters_with_special_chars(selection)

        return selection

    def component_length_ok(self, component, max_length):
        if len(component) > max_length:
            return False
        if len(component) > self._max_word_length:
            return False
        if len(component) > 1 and len(component) < self._min_word_length:
            return False

        return True

    def replace_letters_with_numbers(self, component):
        if not self._letters_to_numbers:
            return component

        if len(component) < 2:
            return component

        new_component = ""

        for letter in component:
            new_component += self.random_replace_letter_with_number(letter)

        return new_component

    def replace_letters_with_special_chars(self, component):
        if not self._letters_to_special_chars:
            return component

        if len(component) < 2:
            return component

        new_component = ""

        for letter in component:
            new_component += self.random_replace_letter_with_special_char(letter)

        return new_component

    def random_replace_letter_with_number(self, letter):
        letter_replacements = {
            "l": "1", "o": "0", "s": "5"
        }

        letter = self.random_replace_letter_from_dict(letter, letter_replacements)
        return letter

    def random_replace_letter_with_special_char(self, letter):
        letter_replacements = {
            "a": "@", "i": "!", "s": "$", "t": "+"
        }

        letter = self.random_replace_letter_from_dict(letter, letter_replacements)
        return letter

    def random_replace_letter_from_dict(self, letter, letter_replacements):
        if letter not in letter_replacements:
            return letter

        if self._rng.random() < 0.5:
            letter = letter_replacements[letter]
        return letter

    @classmethod
    def get_default_properties(cls):
        return list(cls.__default_properties)

    @classmethod
    def get_default_sources(cls):
        return list(cls.__default_sources)
