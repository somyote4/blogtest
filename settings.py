import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

#SECRET_KEY=os.environ['SECRET_KEY']
#DB_USERNAME=os.environ['DB_USERNAME']
#DB_PASSWORD=os.environ['DB_PASSWORD']
#DB_HOST=os.environ['DB_HOST']
#DATABASE_NAME=os.environ['DATABASE_NAME']
#DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
#SQLALCHEMY_DATABASE_URI = DB_URI
#SQLALCHEMY_TRACK_MODIFICATIONS = True
#MYSQL_ROOT_PASSWORD=os.environ['MYSQL_ROOT_PASSWORD']
BLOG_NAME='Blog' #os.environ['BLOG_NAME']
#BLOG_POST_IMAGES_PATH=os.environ['BLOG_POST_IMAGES_PATH']
#SERVER_NAME='127.0.0.1'