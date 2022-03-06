from textwrap import fill
from django.shortcuts import render, redirect
from.forms import searchdetail
from.models import User
from .forms import RegisterForm

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

def shop(request):
    return render(request,'shop.html')

def leaderboard(request):
    return render(request,'leaderboard.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})



