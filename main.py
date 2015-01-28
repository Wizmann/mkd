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

我们的口号是：#闷声发大财#

> 美国记者华莱士，北大教授王铁崖
> 比你们高到不知道哪里去啦！

> Naive!

1. 准备好
2. 滚蛋

3. 没准备好就别想太多

* 为什么人要上床？
* 因为床不会自己来找人啊！

你们这些**螳臂当车**的歹徒！

All you need is __love__, **love** is all you need.

'''

result = parser.parse(data)

print render(result)
