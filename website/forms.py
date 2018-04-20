from django import forms
from .models import UsersForm


class FeedbackForm(forms.ModelForm):	
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name','autocomplete':'off'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email','autocomplete':'off'}))
	mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile','autocomplete':'off'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message','autocomplete':'off'}))

	class Meta:
		model = UsersForm
		fields = ['name','email','mobile','message']
