from random import choice
from django import forms
from.models import User
class searchdetail(forms.ModelForm):
     modeselect = (('team','team'),('teammember','teammember'),('solo','solo'))
     modes = forms.ChoiceField(choices = modeselect,widget=forms.RadioSelect)
     class Meta: 
         model = User
         fields = ['sport','postcode']
     #     labels = {'sport':'sports','postcode':'postcode'}
    
     postcode = forms.CharField(label = "postcode ",max_length=10)
     sport = forms.ChoiceField(label="sport",choices=[('football','football'),('baseball','baseball'),('rugby','rugby'),('tennis','tennis'),('dance','dance'),('swimming','swimming')])
