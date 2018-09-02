# Function check_pass verifies whether a word matches certain password criteria
def check_pass(word):
    # Check password length
    if len(word) < 6 or len(word) > 12:
        return False

    # Check for each type of character
    criteria = {
        "lower": False,
        "upper": False,
        "number": False,
        "special": False,
    }
    for l in word:
        if l.islower():
            criteria["lower"] = True
        if l.isupper():
            criteria["upper"] = True
        if l.isdigit():
            criteria["number"] = True
    if "$" in word or "#" in word or "@" in word:
        criteria["special"] += 1

    # Check if there are at least 1 of each type of character
    for n in criteria:
        if not criteria[n]:
            return False
    return True
