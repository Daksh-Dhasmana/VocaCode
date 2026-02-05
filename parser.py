import ply.yacc as yacc
from lexer import tokens

def p_statement(p):
    'statement : DECL TYPE ID ASSIGN NUMBER'
    p[0] = ('assign',p[3],p[5])

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
