#coding=utf-8
from pprint import pprint

from lex import lexer
from yacc import parser

data = '''
# Head1
## Head2
### Head3

Hello World!

我们的口号是：#闷声发大财#

'''

result = parser.parse(data)
pprint(result)
