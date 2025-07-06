from django import forms

class LoginForm(forms.Form):
    """
    Form for user login.
    """
    username = forms.CharField(max_length=150, required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')
