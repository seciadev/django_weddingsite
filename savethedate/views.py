from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from savethedate.forms import ConfirmForm, SendConfirmForm, ContactForm
from django.shortcuts import redirect
from .models import Profile
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.core.mail import send_mail, BadHeaderError
import sendgrid
import os
from sendgrid.helpers.mail import *


@login_required
def welcome(request):
    return render(request, 'savethedate/index.html', {})

@login_required	
def villa(request):
	return render(request, 'savethedate/villa.html', {})
	
@login_required	
def contatti(request):
	return render(request, 'savethedate/contatti.html', {})

@login_required
def chiesa(request):
	return render(request, 'savethedate/chiesa.html', {})
	
@login_required
def riepilogo(request):
	ProfileFormSet = modelformset_factory(Profile, form=ConfirmForm, extra=0)
	formset = ProfileFormSet(queryset=Profile.objects.filter())
	return render(request, 'savethedate/riepilogo.html', {'formset':formset})

@login_required
def regalo(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
			mUser = request.user.username
			subject = 'Auguri da ' + mUser
			from_email = Email(form.cleaned_data['la_tua_email'])
			to_email = Email('info@miriamgianluca.it')
			content = Content("text/plain", form.cleaned_data['messaggio'])
			mail = Mail(from_email, subject, to_email, content)
			try:
				response = sg.client.mail.send.post(request_body=mail.get())
				#send_mail(subject, message, from_email, ['info@miriamgianluca.it'])
			except BadHeaderError:
				return HttpResponse('Qualcosa è andato storto')
			return redirect('grazie')
	return render(request, "savethedate/regalo.html", {'form': form})
	
@login_required
def grazie(request):
	return render(request, 'savethedate/grazie.html', {})
	
	
@login_required
def conferma(request):
	mFamily = request.user.profile.family
	mConfirmed = request.user.profile.conferma_inviata
	if(mConfirmed==False):
		#ProfileFormSet = modelformset_factory(Profile, fields = ('user', 'conferma_pranzo', 'conferma_sera',), extra=0)
		ProfileFormSet = modelformset_factory(Profile, form=ConfirmForm, extra=0)
		if request.method == 'POST':
			formset = ProfileFormSet(request.POST, queryset=Profile.objects.filter(family=mFamily))
			if formset.is_valid():
				for form in formset:
					f = form.save(commit=False)
					f.conferma_inviata = True
					f.save()
				
				sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
				mUser = request.user.first_name + " " + request.user.last_name
				subject = 'Conferma da ' + mUser
				from_email = Email('info@miriamgianluca.it')
				to_email = Email('info@miriamgianluca.it')
				message = "Hai ricevuto una conferma da "  + mUser
				content = Content("text/plain", message)
				mail = Mail(from_email, subject, to_email, content)
				try:
					response = sg.client.mail.send.post(request_body=mail.get())
				except BadHeaderError:
					return HttpResponse('Qualcosa è andato storto')
					
				return redirect('conferma')
				
			else:
				return HttpResponse(formset.errors, request.POST)
		else:
			formset = ProfileFormSet(queryset=Profile.objects.filter(family=mFamily))
			#form = ConfirmForm(instance=request.user.profile)
		return render(request, 'savethedate/conferma.html', {'confermato': mConfirmed, 'formset':formset, 'mFamily':mFamily})
	
	else:
		EditFormSet = modelformset_factory(Profile, form=SendConfirmForm, extra=0)
		if request.method == 'POST':
			formset = EditFormSet(request.POST, queryset=Profile.objects.filter(family=mFamily))
			if formset.is_valid():
				for form in formset:
					f = form.save(commit=False)
					f.conferma_inviata = False
					f.save()
				
				return redirect('conferma')
			else:
				return HttpResponse(formset.errors, request.POST)
		else:
			formset = EditFormSet(queryset=Profile.objects.filter(family=mFamily))
		return render(request, 'savethedate/conferma.html', {'confermato': mConfirmed, 'formset':formset, 'mFamily':mFamily})