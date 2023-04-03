from builtins import property
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, Form, Select
from .models import *
from django.forms import DateInput, ModelForm, ModelChoiceField, Form, Select, TextInput 
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()


class QuestionForm(ModelForm):

    class Meta:
        model = QuestionModel
        fields = ('__all__')
        widgets = { 
            'text': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
 

class ChooseQuestionForm(ModelForm):

    class Meta:
        model = ChooseQuestionModel
        fields = ('__all__')
        widgets = { 
            'text': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
 


class ElegirInlineFormset(forms.BaseInlineFormSet):
	def clean(self):
		super(ElegirInlineFormset, self).clean()

		respuesta_correcta = 0
		for formulario in self.forms:
			if not formulario.is_valid():
				return

			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta += 1

		try:
			assert respuesta_correcta == QuestionModel.NUMER_DE_RESPUESTAS_PERMITIDAS
		except AssertionError:
			raise forms.ValidationError('Exactamente una sola respuesta es permitida')

  
class UsuarioLoginFormulario(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

class RegistroFormulario(UserCreationForm):
	username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
	password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}))

	class Meta:
		model = User 

		fields = [

			'first_name',
			'last_name',
			'username',
			'email',
			'password1',
			'password2'

		]