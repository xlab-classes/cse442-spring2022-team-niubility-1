from django import forms

#登录表单
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "user name", "required": "required","id":"user","name":"username"}),
                              max_length=100,error_messages={"required": "username cannot empty",})

    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "password", "required": "required","id":"password","name":"password"}),
                              max_length=200,error_messages={"required": "password cannot empty",})

