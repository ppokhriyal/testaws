from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#App Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '878436c0a462c4145fa59eec2c43a66a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin123@terraform-20220223105941158300000001.cbcqn9vb4mbs.us-east-1.rds.amazonaws.com/mysqldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from test.home.route import blue

app.register_blueprint(home.route.blue)
