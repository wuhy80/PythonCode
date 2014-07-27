#!/usr/bin/python
import markdown
import codecs
# Open input file in read, utf-8 mode
input_file = codecs.open("D:\\MyBlog\\octopress\\source\\_posts\\2012-07-23-first-test-blog.markdown", mode="r", encoding="utf8")
text = input_file.read()
html = markdown.markdown(text)
# print
print html