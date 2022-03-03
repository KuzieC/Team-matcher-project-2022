from textwrap import fill
from django.shortcuts import render
from.forms import searchdetail
from.models import User
# Create your views here.
def home (request):
    if request.method == 'POST':
        filled_form = searchdetail(request.POST)
        if filled_form.is_valid():
            sports = User.objects.filter(sport=filled_form.cleaned_data['sport'])
            note ='search for %s at %s area is successful' %(filled_form.cleaned_data['sport'], filled_form.cleaned_data['postcode'],)
            new_form=searchdetail()
            return render(request,'search.html',{'sports':sports ,'note':note})
    sport = searchdetail(); 
    return render(request,'home.html',{'search':sport})

