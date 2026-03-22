import ply.lex as lex

tokens = (
    'DECL','TYPE','ID','ASSIGN','NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'PRINT'
)

reserved = {
    'declare':'DECL',
    'integer':'TYPE',
    'equals':'ASSIGN',
    'plus':'PLUS',
    'minus':'MINUS',
    'multiply':'TIMES',
    'divide':'DIVIDE',
    'print':'PRINT'
}

def t_NUMBER(t):
    r'\d+'
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'ID')
    return t

t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
