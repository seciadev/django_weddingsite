from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ConfirmForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user', 'conferma_pranzo', 'conferma_sera','conferma_inviata',)
		
	def __init__(self, *args, **kwargs):
		super(ConfirmForm, self).__init__(*args, **kwargs)
		self.fields['user'].required = False
		self.fields['conferma_inviata'].required = False
		
class SendConfirmForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('conferma_inviata',)
		
	def __init__(self, *args, **kwargs):
		super(SendConfirmForm, self).__init__(*args, **kwargs)
		self.fields['conferma_inviata'].required = False
		
class ContactForm(forms.Form):
	la_tua_email = forms.EmailField(required=True, error_messages={'required':"Indirizzo email mancante",'invalid':"Indirizzo email non valido"})
	messaggio = forms.CharField(widget=forms.Textarea, error_messages={'required':"Ti sei dimenticato il messaggio!"})
	
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['la_tua_email'].widget.attrs['style'] = 'width: 245px'