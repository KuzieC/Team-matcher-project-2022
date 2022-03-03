from random import choice
from django import forms
from.models import User
class searchdetail(forms.Form):
    postcode = forms.CharField(label = "postcode ",max_length=6)
    sport = forms.ChoiceField(label="sport",choices=[('football','football'),('baseball','baseball'),('rugby','rugby')])

# class searchdetail(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['sport','postcode']
#         labels = {'sport','postcode'}