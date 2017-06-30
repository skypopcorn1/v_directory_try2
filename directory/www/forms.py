from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		bio = forms.CharField(widget=forms.Textarea)
		fields = [ 'name', 'email', 'title', 'phone', 'image', 'bio', 'hobbies', 'birthday', 'github']
		