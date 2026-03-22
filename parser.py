import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list_multiple(p):
    '''statement_list : statement_list statement'''
    p[1].append(p[2])
    p[0] = p[1]

def p_statement_list_single(p):
    '''statement_list : statement'''
    p[0] = [p[1]]

def p_statement_assign(p):
    'statement : DECL TYPE ID ASSIGN expression'
    p[0] = ('assign', p[3], p[5])

def p_statement_print(p):
    'statement : PRINT ID'
    p[0] = ('print', p[2])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])
    
def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

def print_tree(node, prefix="", is_last=True, label=""):
    connector = "└── " if is_last else "├── "
    if isinstance(node, tuple):
        name = str(node[0])
        print(prefix + connector + label + name)
        new_prefix = prefix + ("    " if is_last else "│   ")
        
        if name == 'binop':
            print(new_prefix + "├── [Op] " + str(node[1]))
            print_tree(node[2], new_prefix, False, "[L] ")
            print_tree(node[3], new_prefix, True, "[R] ")
        elif name == 'assign':
            print(new_prefix + "├── [Var] " + str(node[1]))
            print_tree(node[2], new_prefix, True, "[Expr] ")
        elif name == 'print':
            print(new_prefix + "└── [Var] " + str(node[1]))
        else:
            children = node[1:]
            for i, child in enumerate(children):
                print_tree(child, new_prefix, i == (len(children) - 1))
    elif isinstance(node, list):
        for i, child in enumerate(node):
            print_tree(child, prefix, i == (len(node) - 1))
    else:
        print(prefix + connector + label + str(node))
