#coding=utf-8
from jinja2 import Template

tpl_heading = Template('<h{{ level }}>{{ line }}</h{{ level }}>')
tpl_dft     = Template('<p>{{ line }}</p>')

def render(exps):
    res = ''
    for exp in exps:
        if exp['type'] == 'HEADING':
            res += tpl_heading.render(exp)
        else:
            res += tpl_dft.render(exp)

        res += '\n'
    return res

