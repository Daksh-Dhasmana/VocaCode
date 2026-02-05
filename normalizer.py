def normalize(text):

    replacements = {
        "=": " equals ",
        "+": " plus ",
        "-": " minus ",
        "*": " multiply ",
        "/": " divide "
    }

    numbers = {
        "one":"1","two":"2","three":"3","four":"4","five":"5",
        "six":"6","seven":"7","eight":"8","nine":"9","ten":"10"
    }

    text = text.lower()

    for k,v in replacements.items():
        text = text.replace(k,v)

    words = text.split()

    fixed = []
    for w in words:
        fixed.append(numbers.get(w,w))

    return " ".join(fixed)
