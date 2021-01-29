# -*- coding: utf-8 -*-
from config import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import db, DB_URI
from sqlalchemy.schema import Sequence
from sqlalchemy import MetaData, create_engine

Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# @manager.command
# def create_se():
#     engine = create_engine(DB_URI)
#     metadata = MetaData()
#     Sequence_list = ['sys_permissions_id_seq', 'org_role_permission_id_seq', 'admin_roles_id_seq',
#                      'admin_role_users_id_seq', 'admin_role_users_id_seq']
#     for i in Sequence_list:
#         Sequence(i, metadata=metadata).create(bind=engine)


# 删除表
@manager.command
def drop():
    db.drop_all()


# 创建表
@manager.command
def create():
    db.create_all()


# 初始化project
@manager.command
def init_project():
    from init_data import init_project
    init_project()


# 初始化定义好的权限
@manager.command
def init_db():
    from init_data import init_db_data
    init_db_data()


if __name__ == '__main__':
    #### 初始化数据库
    # ```python
    # python manage.py db init
    # python manage.py db migrate
    # python manage.py db upgrade
    # ```
    manager.run()
