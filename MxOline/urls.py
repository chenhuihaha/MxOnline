"""MxOline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve  # 处理静态文件
from django.views.generic import TemplateView
from users import views
from organization.views import OrgView
from MxOline.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.user_register, name='register'),
    url(r'^forgetpwd/$', views.user_forgetpwd, name='forgetpwd'),

    # 课程机构url的分布式路由
    url(r'org/', include('organization.urls', namespace='org')),

    # 课程相关url的分布式路由
    url(r'course/', include('courses.urls', namespace='course')),

    # 配置上传文件的访问处理函数
    url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
