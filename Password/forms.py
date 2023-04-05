from django import forms
from django.contrib.auth.forms import *


class RecuperarContraseñaForm(PasswordResetForm):
    email = forms.EmailField(label='' ,required=True, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Your Email'}))


 