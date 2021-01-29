# -*- coding: utf-8 -*-
import datetime
from config import db, XM_PERMISSIONS, DE_PERMISSIONS
from .models import PDCProject, SysPermission, Roles, OrgRoleUsers, OrgRolePermission


# 初始化PDCProject
def init_project():
    ppj = db.session.query(PDCProject).filter_by(id=1).first()
    if not ppj:
        data = {

        }
        c = PDCProject(**data)
        db.session.add(c)
        db.session.commit()
        db.session.close()


# 每次调用初始化权限表
def init_sys_permission(status=False):
    init_dict = [
        (1, 'users', '用户管理', 0, 1, 2),
        (101, 'user', '用户列表', 1, 101, 2),
        (102, 'role', '权限管理', 1, 102, 1),
        (103, 'institutionalManage', '部门管理', 1, 103, 1),
    ]

    def run_():
        db.session.query(SysPermission).delete(synchronize_session=False)
        db.session.flush()
        db.session.commit()

        for i in init_dict:
            db.session.add(SysPermission(id=i[0],abbr=i[1], name=i[2], pid=i[3], order=i[4], type=i[5]))
        db.session.commit()
        db.session.close()

    run_()


# 创建默认管理员
def init_admin_roles(status=False):
    init_dict = [(1, '超级管理员', 1, 9, 1, 1), (2, '项目管理员', 1, 1, 1, 0)]
    def run_():
        for i in init_dict:
            db.session.query(Roles).filter_by(id=i[0]).delete(synchronize_session=False)
            db.session.add(Roles(id=i[0], name=i[1], is_manager=i[2], manager_level=i[3], is_default=i[4], college_id=i[5]))
        db.session.commit()
        db.session.close()
    run_()


# 绑定默认权限与用户的关系
def init_admin_role_users(status=False):
    init_dict = [(1, 1, 1, 1),(2, 1, 2, 1),]
    def run_():
        for i in init_dict:
            db.session.query(OrgRoleUsers).filter_by(id=i[0]).delete(synchronize_session=False)
            db.session.add(OrgRoleUsers(id=i[0],role_id=i[1], user_id=i[2], is_default=i[3]))
        db.session.commit()
        db.session.close()
    run_()


# 初始化系统管理员所拥有的权限
def init_xm_permission(status=False):
    bm_permission_list = XM_PERMISSIONS
    def run_():
        db.session.query(OrgRolePermission).filter_by(role_id=2).delete(synchronize_session=False)
        for i in bm_permission_list:
            db.session.add(OrgRolePermission(role_id=2, sys_permission_id=i))
        db.session.commit()
        db.session.close()
    run_()


# 删除指定
def init_delete_de(status=False):
    def run_():
        for i in DE_PERMISSIONS:
            db.session.query(SysPermission).filter_by(id=i).delete(synchronize_session=False)
        db.session.commit()
        db.session.close()
    run_()


def init_db_data():
    print("==初始化第一项目===")
    init_project()
    print("==初始化权限===")
    init_sys_permission()
    print("==初始化角色===")
    init_admin_roles()
    print("==初始化用户权限关系===")
    init_admin_role_users()
    print("==初始化项目权限列表===")
    init_xm_permission()
    # print("==删除权限===")
    # init_delete_de()
