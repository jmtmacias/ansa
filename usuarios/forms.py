from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Login','label':'Username'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password',}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirmar Password',}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre','label':'Username'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos','label':'Username'}))
	email = forms.EmailField()


	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
	is_superuser = forms.BooleanField()

	class Meta:
		model = User
#		fields = ("username","first_name","last_name", "email", "password1", "password2","is_superuser")

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user