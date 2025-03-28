from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email','password1','password2', 'avatar']
        
class UserLoginForm(forms.Form):
    username = forms.CharField(label='username', required=True, max_length=254)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Неверные почта или пароль!')
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password'].widget.attrs['id'] = 'password-input'