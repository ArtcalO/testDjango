from django import forms
from .models import *

class SchoolForm(forms.ModelForm):
	class Meta:
		model = School
		fields = '__all__'


class ClasseForm(forms.ModelForm):

	class Meta:
		model = Classe
		fields = '__all__'
		


class RegisterStudentForm(forms.ModelForm):
	
	class Meta:
		model = RegisterStudent
		fields = '__all__'

class ProfileForm(forms.Form):

	#------------CAMPS POUR USER-----------------
	username = forms.CharField(
		label='Username',
		widget=forms.TextInput(
			attrs={
				'placeholder':'Username',
				'class':'form-control'
			}
		)

	)

	password = forms.CharField(
		label='Password',
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'Password',
				'type':'password',
				'class':'form-control'
			}
		)
	)
	password1 = forms.CharField(
		label='Password Confirm',
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'Password',
				'type':'Confirmer',
				'class':'form-control'
			}
		)
	)
	nom = forms.CharField(
		label='Nom',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'Nom',
    			'class':'form-control'
    		}
    	)
	)
	prenom = forms.CharField(
		label='Prenom',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'Prenom',
    			'class':'form-control'
    		}
    	)
    )

	#------------CHAMPS POUR PROFILS--------------------
	age = forms.IntegerField(
		label='Age',
		widget=forms.NumberInput(
    		attrs={
    			'placeholder':'Age',
    			'class':'form-control'
    		}
    	)
    )

	matricule = forms.CharField(
		label='matricule',
		widget=forms.Textarea(
    		attrs={
    			'placeholder':'Matricule',
    			'class':'form-control'
    		}
    	)
    )
	avatar = forms.ImageField(
		label='Image',
		widget=forms.FileInput(
    		attrs={
    			'placeholder':'Image',
    			'class':'form-control'
    		}
    	)
		)


class ConnexionForm(forms.Form):
    username = forms.CharField(
    	label='Username',
    	widget=forms.TextInput(
    		attrs={
    			'placeholder':'Username',
    			'class':'form-control'
    			}
    		)
    	)
    password = forms.CharField(
    	label='Password',
    	widget=forms.PasswordInput(
    		attrs={
    			'placeholder':'password',
    			'type':'password',
    			'class':'form-control'
    			}
    		)
    	)
