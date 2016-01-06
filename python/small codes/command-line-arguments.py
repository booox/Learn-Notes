import sys

print sys.argv
for arg in sys.argv:
    print arg
    
fname = sys.argv[1]
fh = open(fname, 'r')
text = fh.read()
print fname, len(text)