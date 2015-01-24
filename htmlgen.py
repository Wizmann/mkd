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
    render_tpl  =  Template('<br/>')


class quotaRender(BaseRender):
    render_type = 'QUOTE'
    render_tpl  =  Template(
            '<blockquote>\n{% for l in line %}<p>{{ l }}</p>{% endfor %}</blockquote>')


class dftRender(BaseRender):
    render_type = 'LINE'
    render_tpl  = Template('<p>{{ line }}</p>')

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
