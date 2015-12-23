from initdata import db
import pickle

dbfile = open('people-pickle', 'w')     # use `wb` binary mode in 3.x
pickle.dump(db, dbfile)
dbfile.close()
