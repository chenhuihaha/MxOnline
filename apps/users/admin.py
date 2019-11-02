from django.contrib import admin

# Register your models here.
from .models import UserProfile, EmailVerifyRecord, Banner
from . import models

'''
django后台管理注册
'''


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['nike_name', 'birday', 'gender', 'address', 'mobile', 'image']


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'url', 'index', 'add_time']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(Banner, BannerAdmin)
