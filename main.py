#coding=utf-8
import sys

from lex import lexer
from yacc import parser
from htmlgen import render

reload(sys)
sys.setdefaultencoding('utf-8')

data = '''
# Head1
## Head2
### Head3

Hello World!

我们的口号是：#闷声发大财#

'''

result = parser.parse(data)

print render(result)
