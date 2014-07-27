#   Programmer:     limodou
#   E-mail:         limodou@gmail.com
#  
#   Copyleft 2006 limodou
#  
#   Distributed under the terms of the GPL (GNU Public License)
#  
#   UliPad is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   $Id$

from mixins.NCustomLexer import *
    
class DjangoTmpLexer(CustomLexer):

    metaname = 'djangotmp'
    casesensitive = True

    def loadDefaultKeywords(self):
        keys = ['extends', 'block', 'include', 'comment', 'load', 'firstof', 
            'now', 'for', 'regroup', 'ifequal', 'ifnotequal', 'widthratio', 
            'templatetag', 'ifchanged', 'filter', 'ssi', 'debug', 'if', 
            'spaceless', 'cycle', 'else', 'expr', 'catch', 'call', 'pyif', 'pycall']
        end_keys = ['end' + x for x in keys]
        return keys + end_keys

    preview_code = """{% load i18n config %}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
<head>
    <title>{% block title %}Woodlog{% endblock %}</title>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    {% block js %}{% endblock %}
    {% block css %}
    <link href="{% theme_media_path "home" "woodlog.css" %}" rel="stylesheet" type="text/css" />
    {% endblock %}
</head>
"""

    syl_tag = STYLE_CUSTOM + 1
    syl_attrname = STYLE_CUSTOM + 2
    syl_attrvalue = STYLE_CUSTOM + 3
    syl_variable = STYLE_CUSTOM + 4
    syl_symbol = STYLE_CUSTOM + 5
    syl_filter = STYLE_CUSTOM + 6
    syl_tagtext = STYLE_CUSTOM + 7
    syl_djangotag = STYLE_CUSTOM + 8
    syl_script_text = STYLE_CUSTOM + 9
    syl_style_text = STYLE_CUSTOM + 10
    syl_cdatatag = STYLE_CUSTOM + 11

#        self.filters = ['truncatewords', 'removetags', 'linebreaksbr', 'yesno', 
#            'get_digit', 'timesince', 'random', 'striptags', 'filesizeformat', 
#            'escape', 'linebreaks', 'length_is', 'ljust', 'rjust', 'cut', 
#            'urlize', 'fix_ampersands', 'title', 'floatformat', 'capfirst', 
#            'pprint', 'divisibleby', 'add', 'make_list', 'unordered_list', 
#            'urlencode', 'timeuntil', 'urlizetrunc', 'wordcount', 'stringformat', 
#            'linenumbers', 'slice', 'date', 'dictsort', 'dictsortreversed', 
#            'default_if_none', 'pluralize', 'lower', 'join', 'center', 'default', 
#            'upper', 'length', 'phone2numeric', 'wordwrap', 'time', 'addslashes', 
#            'slugify', 'first']
    
    def initSyntaxItems(self):
        self.addSyntaxItem('r_default',         'Default',              STYLE_DEFAULT,              self.STC_STYLE_TEXT)
        self.addSyntaxItem('keyword',           'Keyword',              STYLE_KEYWORD,              self.STC_STYLE_KEYWORD1)
        self.addSyntaxItem('tag',               'Tag',                  self.syl_tag,               self.STC_STYLE_TAG)
        self.addSyntaxItem('attribute',         'Attribute Name',       self.syl_attrname,          self.STC_STYLE_ATTRNAME)
        self.addSyntaxItem('attrvalue',         'Attribute Value',      self.syl_attrvalue,         self.STC_STYLE_ATTRVALUE)
        self.addSyntaxItem('comment',           'Comment',              STYLE_COMMENT,              self.STC_STYLE_COMMENT)
        self.addSyntaxItem('variable',          'Variable',             self.syl_variable,          'italic,back:#FFDCFF')
        self.addSyntaxItem('symbol',            'Symbol',               self.syl_symbol,            self.STC_STYLE_TAG1)
        self.addSyntaxItem('filter',            'Filter',               self.syl_filter,            'fore:#7f7047')
        self.addSyntaxItem('tagtext',           'Tag Text',             self.syl_tagtext,           self.STC_STYLE_TEXT)
        self.addSyntaxItem('djangotag',         'Django Tag',           self.syl_djangotag,         self.STC_STYLE_KEYWORD2)
        self.addSyntaxItem('script_text',       'Script Text',          self.syl_script_text,       self.STC_STYLE_COMMENT)
        self.addSyntaxItem('style_text',        'Style Text',           self.syl_style_text,        self.STC_STYLE_COMMENT)
        self.addSyntaxItem('cdatatag',          'CDATA Tag',            self.syl_cdatatag,          'fore:#FF833F')
        
    def loadToken(self):
        token_tag = TokenList([
            (r'([\w\-:_.]+)\s*=\s*(%s|%s|\S+)' % (PATTERN_DOUBLE_STRING, PATTERN_SINGLE_STRING),
                    [(1, self.syl_attrname), (2, self.syl_attrvalue)]),
            (r'([\w\-:_.]+)\b(?!=)', self.syl_attrname),
        ])
            
        return TokenList([
            (r'<!--.*?-->|\{#.*?#\}|\{%\s*comment\s*%\}.*\{%\s*endcomment\s*%\}', 
                STYLE_COMMENT),
            (r'(<!\[CDATA\[)(.*?)(\]\]>)', 
                [(1, self.syl_cdatatag), (3, self.syl_cdatatag)]),
            (r'(<)(script)(.*?)(>)(.*?)(</)(script)(>)', 
                [(1, self.syl_tag), (2, STYLE_KEYWORD), (3, token_tag),
                (4, self.syl_tag), (5, self.syl_script_text), (6, self.syl_tag), 
                (7, STYLE_KEYWORD), (8, self.syl_tag),
                ]),
            (r'(<)(style)(.*?)(>)(.*?)(</)(style)(>)', 
                [(1, self.syl_tag), (2, STYLE_KEYWORD), (3, token_tag),
                (4, self.syl_tag), (5, self.syl_style_text), (6, self.syl_tag), 
                (7, STYLE_KEYWORD), (8, self.syl_tag),
                ]),
            (r'(\{%)\s*(\w+)\s*(.*?)\s*(%\})', 
                [(1, self.syl_symbol), (2, self.syl_djangotag),
                (3, self.syl_tagtext), (4, self.syl_symbol),
                ]),
            (r'(\{\{)\s*(.*?)\s*(\}\})',
                [(1, self.syl_symbol), (2, self.syl_variable),
                (3, self.syl_symbol),
                ]),
            (r'(<!|<\?|</?)\s*([\w\-:_.]+)\s*(.*?)\s*(\?>|/?>)', 
                [(1, self.syl_tag), (2, STYLE_KEYWORD), 
                (3, token_tag), (4, self.syl_tag)
                ]),
        ])

    backstyles = [(STYLE_COMMENT, '<!--'),
        (syl_cdatatag, '<![CDATA['),
        (syl_tag, '<script'),
        (syl_tag, '<style'),
        (syl_tag, '<'),
    ]
    