"""
@Time    : 2019/11/6 下午3:54
@Author  : chenhui
@FileName: urls.py
@Software: PyCharm
"""

from django.conf.urls import url
from .views import CourseListView, CourseDetailView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail')
]
