"""
@Time    : 2019/11/5 下午2:30
@Author  : chenhui
@FileName: forms.py
@Software: PyCharm
"""
import re
from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    """
    表单提交
    """

    class Meta:
        model = UserAsk
        # 列表形式，传入表单字段
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码
        :return:
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')
