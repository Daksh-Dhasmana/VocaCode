def normalize(text):

    replacements = {
        "=": " equals ",
        "+": " plus ",
        "-": " minus ",
        "*": " multiply ",
        "/": " divide ",
        " equal ": " equals ",
        ",": " , "
    }

    numbers = {
        "one":"1","two":"2","three":"3","four":"4","five":"5",
        "six":"6","seven":"7","eight":"8","nine":"9","ten":"10"
    }

    text = text.lower()

    # Replace symbols
    for k, v in replacements.items():
        text = text.replace(k, v)

    words = text.split()
    words = [numbers.get(w, w) for w in words]

    #  SPLIT STATEMENTS
    statements = []
    current = []

    for w in words:
        if w == ",":
            if current:
                statements.append(current)
                current = []
        else:
            current.append(w)

    if current:
        statements.append(current)

    fixed_statements = []

    for stmt in statements:
        # Add declare if missing
        if "declare" not in stmt:
            stmt.insert(0, "declare")

        # Add integer if missing
        if "integer" not in stmt:
            stmt.insert(1, "integer")

        fixed_statements.append(" ".join(stmt))

    text = " ".join(fixed_statements)

    #  HANDLE CONTINUOUS SPEECH
    words = text.split()

    statements = []
    current = []

    for w in words:
        if w in ["declare", "print"] and current:
            statements.append(" ".join(current))
            current = [w]
        else:
            current.append(w)

    if current:
        statements.append(" ".join(current))

    return " ".join(statements)