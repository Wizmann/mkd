import ply.yacc as yacc

from lex import tokens

def p_content(p):
    ''' content : content expression
                | expression
    '''
    if len(p) == 2 and p[1]:
        if not p[0]:
            p[0] = [p[1]]
        else:
            p[0].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = []
        if p[2]:
            p[0].append(p[2])

def p_expression(p):
    ''' expression : headline
                   | LINE CR
                   | CR
    '''
    if isinstance(p[1], dict):
        p[0] = p[1]
    else:
        p[0] = {
            'type': 'LINE',
            'line': p[1],
        }

def p_expression_head(p):
    '''headline : HEAD LINE CR'''
    p[0] = {
        'type': 'HEADING',
        'level': len(p[1]),
        'line': p[2],
    }

def p_error(p):
    print "Syntax error in input"
    print p

parser = yacc.yacc()

