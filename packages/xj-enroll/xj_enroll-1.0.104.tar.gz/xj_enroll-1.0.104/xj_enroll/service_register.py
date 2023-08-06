# encoding: utf-8
"""
@project: djangoModel->service_register
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 对外开放服务调用注册白名单
@created_time: 2023/1/12 14:29
"""

import xj_enroll
from .service import enroll_services

# 对外服务白名单
register_list = [
    {
        "service_name": "check_can_add",
        "pointer": enroll_services.EnrollRecordServices.check_can_add
    },
    {
        "service_name": "record_add",
        "pointer": enroll_services.EnrollRecordServices.record_add
    },
    {
        "service_name": "test",
        "pointer": enroll_services.EnrollRecordServices.test
    },
]


# 遍历注册
def register():
    for i in register_list:
        setattr(xj_enroll, i["service_name"], i["pointer"])


if __name__ == '__main__':
    register()
