"""
@Time    : 2019/11/5 下午2:36
@Author  : chenhui
@FileName: urls.py
@Software: PyCharm
"""

from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home')
]
