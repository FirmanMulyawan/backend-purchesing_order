from flask import Flask, jsonify
from model import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

POSTGRES = {
    'user': 'postgres',
    'pw': '3210151201900081KTp',
    'db': 'purchase_order_database',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
# app.config['JSON_SORT_KEYS'] = False

db.init_app(app)


from employee import get_all_employee
# from option import get_all_Options
# from question import get_all_Questions
# from quizzes import get_all_Quizzes
# from users import tesUser
# from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def main():
    return 'Test'


# if __name__=='__main__':
#     app.run()