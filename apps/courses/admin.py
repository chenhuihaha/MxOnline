from django.contrib import admin
from . import models


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'add_time']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'name', 'add_time']


class CourseResourseAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'download', 'add_time']


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Lesson, LessonAdmin)
admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.CourseResourse, CourseResourseAdmin)
