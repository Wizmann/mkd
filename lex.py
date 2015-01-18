import sys
import ply.lex as lex

tokens = (
        'HEAD',
        'LINE',
        'CR'
)

t_HEAD = r'(?m)^\#+'
t_LINE = r'.+'

def t_CR(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print >> sys.stderr, 'Illegal character "%s"' % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()
