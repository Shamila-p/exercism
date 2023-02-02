from string import ascii_lowercase
alphabets = set(ascii_lowercase)
def is_pangram(string):
    return alphabets.issubset(string.lower())
