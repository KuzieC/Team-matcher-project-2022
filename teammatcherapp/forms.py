from random import choice
from django import forms
from.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as u


class searchdetail(forms.ModelForm):
     modeselect = (('team','team'),('teammember','teammember'),('compete','compete'))
     mode = forms.ChoiceField(choices = modeselect,widget=forms.RadioSelect)
     class Meta: 
         model = User
         fields = ['sport','postcode']
     #     labels = {'sport':'sports','postcode':'postcode'}
    
     postcode = forms.CharField(label = "postcode ",max_length=10)
     sport = forms.ChoiceField(label="sport",choices=[('football','football'),('baseball','baseball'),('rugby','rugby'),('tennis','tennis'),('dance','dance'),('swimming','swimming'),('running','running')])

class RegisterForm(forms.ModelForm):
    modeselect = (('team','team'),('teammember','teammember'),('compete','compete'))
    mode = forms.ChoiceField(choices = modeselect,widget=forms.RadioSelect)
    class Meta: 
        model = User
        fields = ['name','postcode','gender','phone','age','sport','experience','username','password']
        
    sport = forms.ChoiceField(label="Sport",choices=[('football','football'),('baseball','baseball'),('rugby','rugby'),('tennis','tennis'),('dance','dance'),('swimming','swimming'),('running','running')])
    experience = forms.ChoiceField(label="Experience",choices=[('beginner','beginner'),('intermediate','intermediate'),('advanced','advanced')])
    gender = forms.ChoiceField(label="Gender",choices=[('M','Male'),('F','Female')])

# class RegisterForm(UserCreationForm):

#     class Meta:
#         model = u
#         fields = ["username", "password1", "password2"]


