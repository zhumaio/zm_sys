# -*- coding: utf-8 -*-
import datetime
from sqlalchemy.schema import Sequence
from sqlalchemy import MetaData, create_engine
from config import db, DB_URI

engine = create_engine(DB_URI)
metadata = MetaData()

# # 指定数据的起始id
# Sequence_list = ['sys_permissions_id_seq', 'org_role_permission_id_seq', 'admin_roles_id_seq',
#                  'admin_role_users_id_seq', 'admin_role_users_id_seq']
# for i in Sequence_list:
#     Sequence(i, metadata=metadata).create(bind=engine)
#
# # 主键从10001开始
# id = db.Column(db.Integer, Sequence('sys_permissions_id_seq', start=10001, increment=1),
#              primary_key=True,server_default=db.text("nextval('sys_permissions_id_seq'::regclass)"))

class SysPermission(db.Model):
    """权限表
    type: 9: 总项目权限, 1: 分项目超级管理员权限, 2: 普通管理员权限
    """
    __tablename__ = 'sys_permissions'
    id = db.Column(db.Integer, primary_key=True)
    abbr = db.Column(db.String(50), nullable=False, unique=True, comment="权限简称，建议英文")
    name = db.Column(db.String(50), nullable=False, comment="权限名称")
    pid = db.Column(db.Integer, nullable=False, server_default=db.text("'0'"), comment="权限父级id，没有为：0")
    order = db.Column(db.Integer, nullable=False, server_default=db.text("'0'"))
    type = db.Column(db.Integer, nullable=False,  comment="权限类别")
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)


class OrgRolePermission(db.Model):
    """角色权限表"""
    __tablename__ = 'org_role_permission'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, nullable=False, comment='关联角色id')
    sys_permission_id = db.Column(db.Integer, nullable=False, comment='关联权限id')
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)


class Roles(db.Model):
    """角色表"""
    __tablename__ = 'admin_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, comment='角色名称')
    is_manager = db.Column(db.Boolean(2), default=0, comment='是否是管理员，0: 否，1: 是')
    manager_level = db.Column(db.Integer, default=0, comment='管理员等级，9: 超级管理员, 1: 分项目超级管理员权限, 2: 普通管理员')
    is_default = db.Column(db.Boolean(2), default=0, comment='是否是系统默认值，0: 否, 1: 是，如果是系统值不可修改或删除')
    project_id = db.Column(db.Integer, comment='项目id')
    workflow_state = db.Column(db.String, default='active', comment='工作状态')
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)


class OrgRoleUsers(db.Model):
    """ 角色用户关系表 """
    """"""
    __tablename__ = 'admin_role_users'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, comment="角色id")
    user_id = db.Column(db.Integer, comment="用户id")
    is_default = db.Column(db.Boolean(2), default=0, comment="是否是系统默认值，0: 否, 1:是，如果是系统值不可修改或删除")
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)


# 实例项目，按具体情况修改
class PDCProject(db.Model):
    """"""
    __tablename__ = 'pdc_projects'
    """项目表"""
    id = db.Column(db.Integer, primary_key=True)
    comparison_count = db.Column(db.Integer, server_default=db.text("0"), comment="对比次数")
    name = db.Column(db.String(255), comment="项目名称")
    short_name = db.Column(db.String(255), comment="项目简称")
    code = db.Column(db.String(255), comment="项目编号")
    plan_number = db.Column(db.String(255), comment="方案编号：RBGR 1201,项目编号")
    sponsor_project_unit = db.Column(db.Integer, comment="申办方id")
    weight = db.Column(db.Integer, server_default=db.text("0"), comment="权重")
    status = db.Column(db.Integer, server_default=db.text("0"), comment="1：上线  2：下架")
    project_type = db.Column(db.Integer, server_default=db.text("0"), comment="1：总项  2：分项")
    cliniccal_trials_code = db.Column(db.String(255), comment="临床试验方案编号")
    start_time = db.Column(db.DateTime, comment="开始时间")
    effective_month = db.Column(db.Integer, comment="有效时间,有效月份")
    is_index = db.Column(db.Integer, server_default=db.text("0"), comment="默认为0，上线为1")
    research_field = db.Column(db.Text, comment="研究领域")
    is_web_domain = db.Column(db.Integer, default=0, comment='样本量')
    only_code = db.Column(db.String(255), comment='唯一标识项')
    location = db.Column(db.String(255), comment="项目所在地（省/市/县）")
    mail_address = db.Column(db.Text, comment="通信地址")
    legal_representative = db.Column(db.String(255), comment="法人代表")
    legal_phone = db.Column(db.String(255), comment="法人电话")
    contact_person = db.Column(db.String(255), comment="联系人")
    contact_phone = db.Column(db.String(255), comment="联系电话")
    email = db.Column(db.String(255), comment="电子邮箱")
    bank_name = db.Column(db.String(255), comment="开户行")
    bank_number = db.Column(db.String(255), comment="银行帐号")
    main_business = db.Column(db.Text, comment="主营业务")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)