def normalize(text):
    if not text:
        return ""

    text = text.lower()

    # We map both SYMBOLS and SPOKEN SYNONYMS to your Lexer's exact reserved words
    replacements = {
        "=": " equals ",
        "equal to": " equals ",
        
        "+": " plus ",
        "add": " plus ",
        
        "-": " minus ",
        "subtract": " minus ",
        
        "*": " multiply ",
        "times": " multiply ",
        "multiplied by": " multiply ",
        
        "/": " divide ",
        "divided by": " divide "
    }

    # Convert spelled-out numbers to digits for the NUMBER token
    numbers = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"
    }

    # 1. Replace symbols and synonyms with reserved words
    for k, v in replacements.items():
        text = text.replace(k, v)

    # 2. Split into a list of words to safely convert numbers
    words = text.split()
    fixed = []
    
    for w in words:
        fixed.append(numbers.get(w, w))

    # 3. Join them back together with clean spacing
    return " ".join(fixed)