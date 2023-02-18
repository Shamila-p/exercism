def abbreviate(words):
    acronym = []
    words = words.replace('_', ' ').replace('-', ' ')
    words_split = words.split()
    acronym = [word[0] for word in words_split]
    result = ''.join(acronym).upper()
    return result
