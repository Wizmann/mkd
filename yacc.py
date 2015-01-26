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
                   | quotes
                   | ulists
                   | olists
                   | LINE CR
                   | cr
    '''
    if isinstance(p[1], dict):
        p[0] = p[1]
    else:
        p[0] = {
            'type': 'LINE',
            'line': p[1],
        }

def p_expression_cr(p):
    ''' cr : CR '''
    p[0] = {
        'type': 'CR',
    }

def p_expression_quotes(p):
    ''' quotes : quotes QUOTE LINE CR
               | QUOTE LINE CR
    '''
    if len(p) == 5 and p[3]:
        if not p[1]:
            p[1] = {
                'type': 'QUOTE',
                'line': []
            }
        p[1]['line'].append(p[3].strip())
        p[0] = p[1]
    elif len(p) == 4 and p[2]:
        p[0] = {
            'type': 'QUOTE',
            'line': [p[2].strip()],
        }

def p_expression_olists(p):
    ''' olists : olists OLIST LINE CR
               | OLIST LINE CR
    '''
    if len(p) == 5 and p[3]:
        if not p[1]:
            p[1] = {
                'type': 'OLIST',
                'line': []
            }
        p[1]['line'].append(p[3].strip())
        p[0] = p[1]
    elif len(p) == 4 and p[2]:
        p[0] = {
            'type': 'OLIST',
            'line': [p[2].strip()],
        }

def p_expression_ulists(p):
    ''' ulists : ulists ULIST LINE CR
               | ULIST LINE CR
    '''
    if len(p) == 5 and p[3]:
        if not p[1]:
            p[1] = {
                'type': 'ULIST',
                'line': []
            }
        p[1]['line'].append(p[3].strip())
        p[0] = p[1]
    elif len(p) == 4 and p[2]:
        p[0] = {
            'type': 'ULIST',
            'line': [p[2].strip()],
        }

def p_expression_head(p):
    '''headline : HEAD LINE CR'''
    p[0] = {
        'type': 'HEADING',
        'level': len(p[1]),
        'line': p[2].strip(),
    }

def p_error(p):
    print "Syntax error in input"
    print p

parser = yacc.yacc()

