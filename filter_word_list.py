import sys
from errors import NoArgumentError

# Removes asterisks from all words source file and adds them to the 
# destination file if the remaining characters are all letters


def filter_words(source, destination):
	for line in source:
		line = line.replace("*", "")
		if not line[:-1:].isalpha():
			continue
		new.write(line)


if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		raise NoArgumentError
	
	source = open(sys.argv[1], "r")
	new = open("filtered_words.txt", "w")
	
	filter_words(source, new)
	
	source.close()
	new.close()
	
	print("Done")