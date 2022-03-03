from random import choice
from django import forms
from.models import User
class searchdetail(forms.Form):
    postcode = forms.CharField(label = "postcode ",max_length=10)
    sport = forms.ChoiceField(label="sport",choices=[('football','football'),('baseball','baseball'),('rugby','rugby'),('tennis','tennis'),('dance','dance'),('swimming','swimming')])

# class searchdetail(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['sport','postcode']
#         labels = {'sport','postcode'}