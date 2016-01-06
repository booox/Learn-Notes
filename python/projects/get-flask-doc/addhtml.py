import re

fname = 'index.html'
with open(fname, 'r') as f:
    data = f.read()
    

'''
regex:

    Find:   href="([^#][^":.]*?)/
    Replace: href="\1.html

'''