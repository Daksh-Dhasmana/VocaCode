from normalizer import normalize
from speech_to_text import get_voice
from lexer import lexer
from parser import parser, print_tree
from intermediate import generate_ir
from codegen import generate_c

raw = get_voice()
text = normalize(raw)
print("Normalized:",text)


print("INPUT TEXT:", text)

lexer.input(text)

print("\nTOKENS:")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

tree = parser.parse(text)

print("\nParse Tree:")
if tree:
    print_tree(tree)

if tree is None:
    print("Parsing failed. Your sentence does not match grammar.")
    exit()

ir = generate_ir(tree)
print("IR:", ir)

c_code = generate_c(ir)

with open("output.c","w") as f:
    f.write(c_code)

print("\nGenerated C Code:\n", c_code)
