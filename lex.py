import sys
import ply.lex as lex

tokens = (
        'HEAD',
        'QUOTE',
        'OLIST',
        'ULIST',
        'BOLD',
        'ITALIC',
        'LINE',
        'CR'
)

def t_HEAD(t):
    r'(?m)^\#+'
    return t

def t_QUOTE(t):
    r'(?m)^\>'
    return t

def t_OLIST(t):
    r'(?m)^\d+\.\ '
    return t

def t_ULIST(t):
    r'(?m)^\*\ '
    return t

def t_BOLD(t):
    r'\*\*'
    return t

def t_ITALIC(t):
    r'\_\_'
    return t

def t_LINE(t): 
    r'[^\*\_\n]+'
    return t

def t_CR(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print >> sys.stderr, 'Illegal character "%s"' % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()
