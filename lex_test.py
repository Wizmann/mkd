import lex

data = '''
# Head1
## Head2
### Head3

hello world!

bullshit ## fuck me

'''

lex.lexer.input(data)

while True:
    tok = lex.lexer.token()
    if not tok:
        break
    print tok
