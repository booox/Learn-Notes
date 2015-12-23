
import pickle

dbfile = open('people-pickle', 'r')     # use `rb` binary mode in 3.x
db = pickle.load(dbfile)

for key in db:
    print key, '=>\n   ', db[key]
    
print db['sue']['name']
