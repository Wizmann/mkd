#coding=utf-8
import logging
from jinja2 import Template

renderers = {}

class MetaRender(type):
    def __init__(cls, name, bases, attrs):
        parents = [b for b in bases if isinstance(b, MetaRender)]
        if not parents:
            return

        render_type = cls.render_type
        if render_type in renderers:
            logging.fatal("Dup render type: %s" % render_type)
            return
        renderers[render_type] = cls()


class BaseRender(object):
    __metaclass__ = MetaRender

    def render(self, exp):
        return self.render_tpl.render(exp)


class headingRender(BaseRender):
    render_type = 'HEADING'
    render_tpl  = Template(
            '<h{{ level }}>{{ line }}</h{{ level }}>')


class crRender(BaseRender):
    render_type = 'CR'
    render_tpl  =  Template('<p></p>')


class quoteRender(BaseRender):
    render_type = 'QUOTE'
    render_tpl  =  Template(
            '<blockquote>\n{% for l in line %}<p>{{ l }}</p>\n{% endfor %}</blockquote>')


class ulistRender(BaseRender):
    render_type = 'ULIST'
    render_tpl  = Template(
            '<ul>\n{% for l in line %}<li>{{ l }}</li>\n{% endfor %}</ul>')


class olistRender(BaseRender):
    render_type = 'OLIST'
    render_tpl  = Template(
            '<ol>\n{% for l in line %}<li>{{ l }}</li>\n{% endfor %}</ol>')


class lineRender(BaseRender):
    render_type = 'LINE'
    render_tpl  = Template(
            '<p>{% for l in line %}'
            '{% if l.type == "BOLD" %}'
            '<b> {{ l.line }} </b>'
            '{% elif l.type == "ITALIC" %}'
            '<i> {{ l.line }} </i>'
            '{% else %}'
            '{{ l.line }}'
            '{% endif %}'
            '{% endfor %}'
            '</p>')


class dftRender(BaseRender):
    render_type = ''
    render_tpl  = Template('<p>{{ line }}</p>')


def render(exps):
    res = ''
    for exp in exps:
        exp_type = exp.get('type', '')
        renderer = renderers[exp_type]
        res += renderer.render(exp)
        res += '\n'
    return res
