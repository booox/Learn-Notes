# from make_db_file import loadDbase2
import make_db_file

# make_db_file.loadDbase2()

db = make_db_file.loadDbase()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

make_db_file.storeDbase(db)

