from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MyNewpass1!'
app.config['MYSQL_DATABASE_DB'] = 'scms'
app.config['MYSQL_DATABASE_HOST'] = 'ec2-100-26-166-67.compute-1.amazonaws.com'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)