from random import choice
from django import forms
from.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as u




class searchdetail(forms.ModelForm):
     #modeselect = (('team','team'),('teammember','teammember'),('compete','compete'))
     #mode = forms.ChoiceField(choices = modeselect,widget=forms.RadioSelect)
     class Meta: 
         model = User
         fields = ['sport','city']
     #     labels = {'sport':'sports','postcode':'postcode'}
    
     city = forms.ChoiceField(label = "City ",choices=[('Aberdeen','Aberdeen'),('Armagh','Armagh'),('Bangor','Bangor'),('Bath','Bath'),('Belfast','Belfast'),('Birmingham','Birmingham'),('Bradford','Bradford'),('Brighton&Hove','Brighton&Hove'),('Bristol','Bristol'),('Cambridge','Cambridge'),('Canterbury','Canterbury'),('Cardiff Wales','Cardiff Wales'),('Carlisle','Carlisle'),('Chelmsford','Chelmsford'),('Chester','Chester'),('Chichester','Chichester'),('Coventry','Coventry'),('Derby','Derby'),('Dundee','Dundee'),('Durham','Durham'),('Edinburgh','Edinburgh'),('Ely','Ely'),('Exeter','Exeter'),('Glasgow','Glasgow'),('Gloucester','Gloucester'),('Hereford','Hereford'),('Inverness','Inverness'),('KingstonUponHull','KingstonUponHull'),('Lancaster','Lancaster'),('Leeds','Leeds'),('Leicester','Leicester'),('Lichfield','Lichfield'),('Lincoln','Lincoln'),('Lisburn','Lisburn'),('Liverpool','Liverpool'),('London','London'),('Londonderry','Londonderry'),('Manchester','Manchester'),('Newcastle','Newcastle'),('Newport','Newport'),('Newry','Newry'),('Norwich','Norwich'),('Nottingham','Nottingham'),('Oxford','Oxford'),('Perth','Perth'),('Peterborough','Peterborough'),('Plymouth','Plymouth'),('Portsmouth','Portsmouth'),('Preston','Preston'),('Ripon','Ripon'),('Salford','Salford'),('Salisbury','Salisbury'),('Sheffield','Sheffield'),('Southampton','Southampton'),('St Albans','St Albans'),
     ('St Asaph','St Asaph'),('St Davids','St Davids'),('Stirling','Stirling'),('Stoke-on-Trent','Stoke-on-Trent'),('Sunderland','Sunderland'),('Swansea','Swansea'),('Truro','Truro'),('Wakefield','Wakefield'),('Wells','Wells'),('Westminster','Westminster'),('Winchester','Winchester'),('Wolverhampton','Wolverhampton'),('Worcester','Worcester'),('York','York')])
     sport = forms.ChoiceField(label="Sport",choices=[('football','football'),('baseball','baseball'),('rugby','rugby'),('tennis','tennis'),('dance','dance'),('swimming','swimming'),('running','running')])
     mode = forms.ChoiceField(label="Mode",choices=[('team','team'),('teammember','teammember'),('compete','compete')])

class RegisterForm(forms.ModelForm):
    #modeselect = (('team','team'),('teammember','teammember'),('compete','compete'))
    #mode = forms.ChoiceField(choices = modeselect,widget=forms.RadioSelect)
    class Meta: 
        model = User
        fields = ['name','city','gender','phone','age','sport','experience','username','password']
        
    city = forms.ChoiceField(label = "City ",choices=[('Aberdeen','Aberdeen'),('Armagh','Armagh'),('Bangor','Bangor'),('Bath','Bath'),('Belfast','Belfast'),('Birmingham','Birmingham'),('Bradford','Bradford'),('Brighton&Hove','Brighton&Hove'),('Bristol','Bristol'),('Cambridge','Cambridge'),('Canterbury','Canterbury'),('Cardiff Wales','Cardiff Wales'),('Carlisle','Carlisle'),('Chelmsford','Chelmsford'),('Chester','Chester'),('Chichester','Chichester'),('Coventry','Coventry'),('Derby','Derby'),('Dundee','Dundee'),('Durham','Durham'),('Edinburgh','Edinburgh'),('Ely','Ely'),('Exeter','Exeter'),('Glasgow','Glasgow'),('Gloucester','Gloucester'),('Hereford','Hereford'),('Inverness','Inverness'),('KingstonUponHull','KingstonUponHull'),('Lancaster','Lancaster'),('Leeds','Leeds'),('Leicester','Leicester'),('Lichfield','Lichfield'),('Lincoln','Lincoln'),('Lisburn','Lisburn'),('Liverpool','Liverpool'),('London','London'),('Londonderry','Londonderry'),('Manchester','Manchester'),('Newcastle','Newcastle'),('Newport','Newport'),('Newry','Newry'),('Norwich','Norwich'),('Nottingham','Nottingham'),('Oxford','Oxford'),('Perth','Perth'),('Peterborough','Peterborough'),('Plymouth','Plymouth'),('Portsmouth','Portsmouth'),('Preston','Preston'),('Ripon','Ripon'),('Salford','Salford'),('Salisbury','Salisbury'),('Sheffield','Sheffield'),('Southampton','Southampton'),('St Albans','St Albans'),
     ('St Asaph','St Asaph'),('St Davids','St Davids'),('Stirling','Stirling'),('Stoke-on-Trent','Stoke-on-Trent'),('Sunderland','Sunderland'),('Swansea','Swansea'),('Truro','Truro'),('Wakefield','Wakefield'),('Wells','Wells'),('Westminster','Westminster'),('Winchester','Winchester'),('Wolverhampton','Wolverhampton'),('Worcester','Worcester'),('York','York')])
    sport = forms.ChoiceField(label="Sport",choices=[('football','football'),('baseball','baseball'),('rugby','rugby'),('tennis','tennis'),('dance','dance'),('swimming','swimming'),('running','running')])
    experience = forms.ChoiceField(label="Experience",choices=[('beginner','beginner'),('intermediate','intermediate'),('advanced','advanced')])
    gender = forms.ChoiceField(label="Gender",choices=[('M','Male'),('F','Female')])
    mode = forms.ChoiceField(label="Mode",choices=[('team','team'),('teammember','teammember'),('compete','compete')])
    password = forms.CharField(widget=forms.PasswordInput())
    gdpr = forms.BooleanField(label = 'Accept GDPR')


