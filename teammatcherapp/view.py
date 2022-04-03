from textwrap import fill
from urllib import request
from django.shortcuts import render, redirect
from.forms import searchdetail
from.models import User, LeaderBoardPosition
from .forms import RegisterForm

# Create your views here.
def search (request):
    if request.method == 'POST':
        filled_form = searchdetail(request.POST)
        if filled_form.is_valid():
            sports = User.objects.filter(sport=filled_form.cleaned_data['sport'])
            mode = sports.filter(mode=filled_form.cleaned_data['mode'])
            city = mode.filter(city=filled_form.cleaned_data['city'])
            note ='Search results for %s in %s' %(filled_form.cleaned_data['sport'], filled_form.cleaned_data['city'],)
            new_form=searchdetail()
            return render(request,'searchresult.html',{'sports':sports ,'note':note,'city':city})
    sport = searchdetail(); 
    return render(request,'search.html',{'search':sport})

def home(request):
    return render(request,'home.html')

def gdpr(request):
    return render(request,'gdpr.html')

def shop(request):
    return render(request,'shop.html')

def leaderboard(request):
    position = LeaderBoardPosition.objects.all().order_by('-score')
    return render(request,'leaderboard.html', {'pos':position})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        name = response.POST['name']
        city = response.POST['city']
        gender = response.POST['gender']
        phone = response.POST['phone']
        age = response.POST['age']
        sport = response.POST['sport']
        experience = response.POST['experience']
        username = response.POST['username']
        password = response.POST['password']
        mode = response.POST['mode']
        user = User(name = name ,city = city,gender = gender,phone = phone,age = age , sport = sport,experience = experience,username = username,password= password,mode = mode)
        if form.is_valid():
            user.save()
            return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})



