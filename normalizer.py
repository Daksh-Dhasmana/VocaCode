def normalize(text):
    if not text:
        return ""

    text = text.lower()

    # Pre-pad raw symbols with spaces (Addresses Task 2: Formatting errors)
    # The speech API sometimes returns "x=5" or "1+1". This ensures they are split properly.
    for op in ['+', '-', '*', '/', '=']:
        text = text.replace(op, f" {op} ")

    # Expanded dictionary mapping SYMBOLS and broader SPOKEN SYNONYMS (Addresses Task 1)
    replacements = {
        # Assignment
        "=": " equals ",
        "equal to": " equals ",
        "equals to": " equals ",
        "set to": " equals ",
        "becomes": " equals ",
        
        # Addition
        "+": " plus ",
        "add": " plus ",
        "added to": " plus ",
        
        # Subtraction
        "-": " minus ",
        "subtract": " minus ",
        
        # Multiplication
        "*": " multiply ",
        "times": " multiply ",
        "multiplied by": " multiply ",
        "multiply by": " multiply ",
        
        # Division
        "/": " divide ",
        "divided by": " divide ",
        "divide by": " divide ",
        "over": " divide ",

        # Strip out conversational filler that might confuse the parser
        "variable": "", 
        "let": ""
    }

    # Expanded spelled-out numbers dictionary (Addresses Task 1)
    numbers = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
        "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14", 
        "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18", 
        "nineteen": "19", "twenty": "20", "thirty": "30", "forty": "40", 
        "fifty": "50", "sixty": "60", "seventy": "70", "eighty": "80", 
        "ninety": "90", "hundred": "100"
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