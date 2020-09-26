# -*- coding: utf-8 -*-
"""
@Author    : parzulpan

@Email     : parzulpan@gmail.com

@Summary   : 请输入该文件所实现的功能描述

@Attention :
"""
from markdown_it import MarkdownIt
from markdown_it.extensions.front_matter import front_matter_plugin
from markdown_it.extensions.footnote import footnote_plugin


md = (
    MarkdownIt()
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .disable('image')
    .enable('table')
)
text = ("""
---
a: 1
---

a | b
- | -
1 | 2

A footnote [^1]

[^1]: some details
""")
print(text)

tokens = md.parse(text)
print(tokens)

html_text = md.render(text)
print(html_text)
