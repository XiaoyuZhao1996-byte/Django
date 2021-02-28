from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Question, Choice


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),min_length=4)
    # validate_password(password, user=None, password_validators=None)
    # password = forms.CharField(widget=forms.PasswordInput(attrs=form_attrs.password)
    # validate_password(password=password)
    # if password:
    #     if len(password) < 4:
    #        raise forms.ValidationError(_("Password must be at least 8 chars."))
    def clean(self):# 定义username的校验方法
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        if password.isdigit() == True:
            raise forms.ValidationError("用户名不能全为数字")
    class Meta():
        model = User
        fields = ('username','email','password')
    

class Questions(forms.ModelForm):
    class Meta():
        model = Question
        fields = ('question_text','status')

class Questions1(forms.ModelForm):
    # disabled_fields = ('question_text',)
    class Meta():
        model = Question
        fields = ('status',)
    # def __init__(self, *args, **kwargs):
    #     super(Questions1, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     for field in self.disabled_fields:
    #         self.fields[field].disabled = True

class Choices(forms.ModelForm):
    disabled_fields = ('voter','question')
    class Meta():
        model = Choice
        fields = ('question','voter','choice_text')

    def __init__(self, *args, **kwargs):
        super(Choices, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        for field in self.disabled_fields:
            self.fields[field].disabled = True
    