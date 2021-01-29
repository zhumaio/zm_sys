# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


DB_HOST = '192.168.0.84'
DB_PORT = '5432'
DB_USERNAME = 'zm_test'
DB_PASSWORD = '123456'
DB_DATABASE = 'admin_development'
DB_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)

# 项目链接postgresql
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 初始化一项权限
XM_PERMISSIONS = []
# 删除权限
DE_PERMISSIONS = []
