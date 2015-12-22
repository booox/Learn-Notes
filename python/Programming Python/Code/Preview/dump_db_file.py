# from make_db_file import loadDbase2
import make_db_file

# make_db_file.loadDbase2()

db = make_db_file.loadDbase()
for key in db:
    print key, '=>\n  ', db[key]
print db['sue']['name']

