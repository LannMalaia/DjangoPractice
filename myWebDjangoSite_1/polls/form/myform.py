from django import forms


class LoginForm(forms.Form):
    userid = forms.CharField(label='USER ID: ', max_length=255)
    password = forms.CharField(label='PASSWORD: ', max_length=255)