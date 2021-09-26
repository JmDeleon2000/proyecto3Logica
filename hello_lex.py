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
    'COMA'
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
t_COMA = R'\,'

def t_error(t):
    print("Caracter invalido: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("~^~")



while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)