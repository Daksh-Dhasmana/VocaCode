from normalizer import normalize
from speech_to_text import get_voice
from lexer import lexer
from parser import parser
from intermediate import generate_ir
from codegen import generate_c


def process_speech():
    raw = get_voice()
    text = normalize(raw)

    print("Normalized:", text)
    print("INPUT TEXT:", text)

    return text


def perform_lexing(text):
    lexer.input(text)

    print("\nTOKENS:")
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
        print(tok)

    return tokens


def perform_parsing(text):
    tree = parser.parse(text)

    print("\nParse Tree:", tree)

    if tree is None:
        print("Parsing failed. Your sentence does not match grammar.")
        return None

    return tree


def generate_code(tree):
    ir = generate_ir(tree)
    print("IR:", ir)

    c_code = generate_c(ir)

    with open("output.c", "w") as f:
        f.write(c_code)

    print("\nGenerated C Code:\n", c_code)


def main():
    text = process_speech()

    tokens = perform_lexing(text)

    tree = perform_parsing(text)

    if tree is None:
        return

    generate_code(tree)


if __name__ == "__main__":
    main()