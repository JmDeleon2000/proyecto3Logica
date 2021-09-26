import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'VARIABLE',
    'CONSTANT',
    'NEGATION',
    'DOUBLEARROW',
    'ARROW',
    'HAT',
    'OR',
    'LPAREN',
    'RPAREN',
)

t_VARIABLE = R'[p-zA-Z_]' #acepta ppp se arregla con YACC
t_CONSTANT = R'[0-1]' #acepta 01101 se arregla con YACC
t_NEGATION = R'\~'
t_ARROW = R"\=\>"
t_DOUBLEARROW = R'\<\=\>'
t_HAT = R'\^'
t_OR = R'o'
t_LPAREN = R'\('
t_RPAREN = R'\)'


def t_error(t):
    print("Caracter invalido: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("~ ^ ~")



while True:
    break
    tok = lexer.token()
    if not tok:
        break
    print(tok)




def p_parentheses(p):
    'S : LPAREN S RPAREN'
    p[0] = p[2]

def p_VAR(p):
    'S : VARIABLE'
    p[0] = p[1]

def p_CONS(p):
    'S : CONSTANT'
    p[0] = p[1]

def p_NEG(p):
    'S : NEGATION S'
    p[0] = str(p[1]) + str(p[2])

def p_DOUBLEARROW(p):
    'S : S DOUBLEARROW S'
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) 

def p_ARROW(p):
    'S : S ARROW S'
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) 

def p_HAT(p):
    'S : S HAT S'
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) 

def p_OR(p):
    'S : S OR S'
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) 


def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc(start='S')



print(parser.parse('p'))
print(parser.parse('~~~q'))
print(parser.parse('(p^q)'))
print(parser.parse('~(p^q)'))
print(parser.parse('(p<=>~p)'))
print(parser.parse('((p=>q)^p)'))
print(parser.parse('(~(p^(qor))os)'))

