from django import forms
from django.contrib.auth.models import User

from production.models import ProductionOrder, Supplies


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control controls col-md-4 col-form-label text-md-end',
        'id': 'username',
        'placeholder': 'Nombre'
    }))
    last_name = forms.CharField(required=True, min_length=4, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control controls col-md-4 col-form-label text-md-end',
        'id': 'last_name',
        'placeholder': 'Apellido'
    }))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control controls col-md-4 col-form-label text-md-end',
        'id': 'email',
        'placeholder': 'Correo'
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control controls col-md-4 col-form-label text-md-end',
        'id': 'password',
        'placeholder': 'Contraseña'
    }))

    password2 = forms.CharField(label='Confirmar password', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control controls col-md-4 col-form-label text-md-end',
        'id': 'password-confirm',
        'placeholder': 'Confirmar contraseña'
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre ya se encuentra en uso")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya se encuentra en uso")
        return email
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La contraseña no coincide')

