import pickle, glob

for filename in glob.glob('*.pkl'):     # for 'bob', 'sue', 'tom'
    recfile = open(filename, 'r')
    record = pickle.load(recfile)
    print filename, '=>\n   ', record
    
suefile = open('sue.pkl', 'r')
print pickle.load(suefile)['name']      # fetch sue's name