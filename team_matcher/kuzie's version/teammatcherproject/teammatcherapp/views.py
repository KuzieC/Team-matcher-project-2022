from textwrap import fill
from django.shortcuts import render
from.forms import searchdetail
from.models import User
# Create your views here.
def search (request):
    if request.method == 'POST':
        filled_form = searchdetail(request.POST)
        if filled_form.is_valid():
            sports = User.objects.filter(sport=filled_form.cleaned_data['sport'])
            mode = sports.filter(mode=filled_form.cleaned_data['mode'])
            note ='search results for %s near %s' %(filled_form.cleaned_data['sport'], filled_form.cleaned_data['postcode'],)
            new_form=searchdetail()
            return render(request,'searchresult.html',{'sports':sports ,'note':note,'mode':mode})
    sport = searchdetail(); 
    return render(request,'search.html',{'search':sport})

def home(request):
    return render(request,'home.html')

def gdpr(request):
    return render(request,'gdpr.html')

