def transform(old_data):
    shiny_scrabble= {}
    for score, letters in old_data.items():
        for letter in letters:
            shiny_scrabble[letter.lower()] = score
    return shiny_scrabble
