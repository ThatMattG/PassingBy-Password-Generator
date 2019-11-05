import argparse
from password_generator import PasswordGenerator

"""

Welcome to the PassingBy Password Generator.
This tool aims to demonstrate random but somewhat memorable passwords.

Usage: main.py
	[--batch_size BATCH_SIZE]								(how many passwords?)
	[--length LENGTH]										(how long is each?)
	[--min_word_length MIN_WORD_LENGTH]						(shortest words)
	[--max_word_length MAX_WORD_LENGTH]						(longest words)
	[--letters_to_numbers LETTERS_TO_NUMBERS]				(e.g. replace o with 0)
	[--letters_to_special_chars LETTERS_TO_SPECIAL_CHARS]	(e.g. replace s with $)
	[--letters LETTERS]										(want some extra letters?)
	[--capital_letters CAPITAL_LETTERS]						(want some capital letters?)
	[--numbers NUMBERS]										(want some numbers?)
	[--special_chars SPECIAL_CHARS]							(want special chars?)
	[--words WORDS]											(want words?)

for example:
	$ python main.py --special_chars 1 --letters_to_numbers 0 --batch_size 20
will produce 20 passwords which include special characters but
without letters replacing numbers inside words.

Words, capital letters and numbers are used by default.
Default length is 18. Batch size is 3. Letters may be replaced with numbers.

Please note: while SystemRandom has been used to aid in random number
generation, there is NO guarantee that this tool is cryptographically
secure as a whole. Therefore, it is not recommended that this tool is
used to produce real passwords - it is only for educational purposes.

"""

default_batch_size = 3

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--batch_size")

    for property in PasswordGenerator.get_default_properties():
        parser.add_argument("--" + property)

    parser.add_argument("--letters")
    parser.add_argument("--capital_letters")
    parser.add_argument("--numbers")
    parser.add_argument("--special_chars")
    parser.add_argument("--words")

    args = parser.parse_args()

    pgen = PasswordGenerator(args)

    try:
        batch_size = int(args.batch_size)
    except TypeError:
        batch_size = default_batch_size

    passwords = []
    print("\nGenerating...\n")
    for i in range(batch_size):
        new_password = pgen.produce_password()
        passwords.append(new_password)
    for password in passwords:
        print("-", password, "\n")
