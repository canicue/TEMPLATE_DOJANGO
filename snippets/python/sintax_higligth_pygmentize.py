# -*- coding: utf-8 -*-

'''
Created on 21/04/2010,18:29:12

@author: canicue
'''
from django import template

from pygments import highlight
from pygments.lexers import guess_lexer, PythonLexer
from pygments.formatters import HtmlFormatter
from BeautifulSoup import BeautifulSoup

register = template.Library()

@register.filter
def pygmentize(value):
    try:
        soup = BeautifulSoup(value)
        code_blocks = soup.findAll('code')
        for code in code_blocks:
            try:
                lexer = guess_lexer(code.string)
            except ValueError:
                lexer = PythonLexer()
            code.replaceWith(highlight(code.string, lexer, HtmlFormatter()))
        return str(soup)
    except:
        return value
