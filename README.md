# PassingBy-Password-Generator
A configurable password generator built on 14 May 2019 by ThatMattG.

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

Please note: while SystemRandom has been used to aid in random number
generation, there is NO guarantee that this tool is cryptographically
secure as a whole. Therefore, it is not recommended that this tool is
used to produce real passwords - it is only for educational purposes.

Thanks to the Kids Open Dictionary Builder for its public domain
dictionary being used by this project. Website:
  http://dictionary.k12opened.com/index.php
