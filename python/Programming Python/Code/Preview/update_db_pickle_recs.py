import pickle

suefile = open('sue.pkl', 'r')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.10

suefile = open('sue.pkl', 'w')
pickle.dump(sue, suefile)
suefile.close()