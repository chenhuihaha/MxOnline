from django.contrib import admin
from . import models


# Register your models here.
class CityDictAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'add_time']


class CourseOrgAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']


admin.site.register(models.CityDict, CityDictAdmin)
admin.site.register(models.CourseOrg, CourseOrgAdmin)
admin.site.register(models.Teacher, TeacherAdmin)
