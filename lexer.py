# lexer.py - Lexical Analyzer for Voice-to-Code Compiler
"""
Lexical Analyzer: Tokenizes input text.

Features:
- Recognizes reserved keywords
- Handles natural language comparisons (smaller than, greater than)
- Proper token precedence

Pipeline Position:
  Input → Lexer → Parser
"""

import ply.lex as lex

# Define tokens
tokens = (
    'DECL', 'TYPE', 'ID', 'ASSIGN', 'NUMBER',
    'PLUS', 'PRINT', 'STRING', 'AND', 'LPAREN', 'RPAREN',
    'IF', 'THEN', 'ELSE', 'ENDIF', 'LOOP', 'FROM', 'TO', 'ENDLOOP',
    'GREATER', 'LESS'
)

# Reserved words mapping
reserved = {
    'declare': 'DECL',
    'integer': 'TYPE',
    'equals': 'ASSIGN',
    'plus': 'PLUS',
    'print': 'PRINT',
    'and': 'AND',
    'of': 'AND',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'endif': 'ENDIF',
    'loop': 'LOOP',
    'from': 'FROM',
    'to': 'TO',
    'endloop': 'ENDLOOP',
    'greater': 'GREATER',
    'less': 'LESS',
    'smaller': 'LESS',
    'bigger': 'GREATER',
    'more': 'GREATER',
}

# Define tokens with regex
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Simple tokens
t_PLUS = r'plus'
t_PRINT = r'print'
t_AND = r'and|of'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignored characters
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test
if __name__ == "__main__":
    test = "declare integer x equals 5 if x smaller than 60 then print x else print y"
    lexer.input(test)
    print("Testing lexer:")
    for tok in lexer:
        print(f"{tok.type}: {tok.value}")