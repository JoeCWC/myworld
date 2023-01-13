from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class PostForm(forms.Form):
	cName = forms.CharField(max_length=20,initial='')
	cSex = forms.CharField(max_length=2,initial='M')
	cBirthday = forms.DateField()
	cEmail = forms.EmailField(max_length=100,initial='',required=False)
	cPhone = forms.CharField(max_length=50,initial='',required=False)








