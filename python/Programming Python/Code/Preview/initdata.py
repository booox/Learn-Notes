#coding=utf-8
# Initialize data to be stored in files, pickles, shelves

# records
bob = {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
sue = {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
tom = {'pay': 0, 'job': None, 'age': 50, 'name': 'Tom'}

#database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':          # When run as a script
    for key in db:
        print key, '=>\n    ', db[key]
    input()         # pause the cmd