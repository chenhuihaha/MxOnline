from django.contrib import admin
from . import models


# Register your models here.
class UserAskAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'add_time']


admin.site.register(models.UserAsk, UserAskAdmin)
admin.site.register(models.CourseComments, CourseCommentsAdmin)
admin.site.register(models.UserFavorite, UserFavoriteAdmin)
admin.site.register(models.UserMessage, UserMessageAdmin)
admin.site.register(models.UserCourse, UserCourseAdmin)
