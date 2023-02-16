def response(hey_bob):
    hey_bob = hey_bob.strip()
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    Yelling = hey_bob.isupper()
    Question = hey_bob[-1] == "?"
    if Yelling:
        if Question:
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    if Question:
        return "Sure."
    return "Whatever."