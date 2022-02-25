from sqlalchemy import null
from test import app,db

#User Database
class Users(db.Model):
    __tablename__ = 'usertab'
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(5),nullable=False)
    lastname = db.Column(db.String(10),nullable=False)