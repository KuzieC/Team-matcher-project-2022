from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User as u
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from .forms import EditProfileForm, RegisterForm, ItemsForm
import imp
from textwrap import fill
from urllib import request
from django.shortcuts import render, redirect
from.forms import searchdetail
from.models import User, LeaderBoardPosition, shopInfo
from .forms import RegisterForm , EditProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as u
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.urls import reverse_lazy
#from django.views.generic.edit import UpdateView
#from django.views.generic import DetailView
#from teammatcherapp import view
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)



# Create your views here.
def search(request):
    if request.method == 'POST':
        filled_form = searchdetail(request.POST)
        if filled_form.is_valid():
            sports = User.objects.filter(
                sport=filled_form.cleaned_data['sport'])
            mode = sports.filter(mode=filled_form.cleaned_data['mode'])
            city = mode.filter(city=filled_form.cleaned_data['city'])
            note = 'Search results for %s in %s' % (
                filled_form.cleaned_data['sport'], filled_form.cleaned_data['city'],)
            new_form = searchdetail()
            return render(request, 'searchresult.html', {'sports': sports, 'note': note, 'city': city})
    sport = searchdetail()
    return render(request, 'search.html', {'search': sport})


def home(request):
    return render(request, 'home.html')


def gdpr(request):
    return render(request, 'gdpr.html')


def shop(request):
    teammatcherapp = shopInfo.objects.all()
    context = {"teammatcherapp":teammatcherapp}
    return render(request,'shop.html',context)


def shopItems(request):
    if request.method == "POST":
        items = ItemsForm(request.POST, request.FILES)
        if items.is_valid():
            items.save()
            return redirect("/home/")
    else:
        items = ItemsForm()
    return render(request, "shopSell.html", {"items": items})


def profile(request):
    return render(request, 'profile.html')


def leaderboard(request):
    position = LeaderBoardPosition.objects.all().order_by('-score')
    return render(request, 'leaderboard.html', {'pos': position})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        form2 = UserCreationForm(response.POST)
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
        user = User(name=name, city=city, gender=gender, phone=phone, age=age, sport=sport,
                    experience=experience, username=username, password=password, mode=mode)
        hashed_pwd = make_password(password)
        user2 = u(username=username, password=hashed_pwd)
        if form.is_valid():
            user.save()
            user2.save()
            login(response, user2)
            return redirect("/home/")

    else:
        form = RegisterForm()
        form2 = UserCreationForm()
    return render(response, "register.html", {"form": form})



#class UserView(LoginRequiredMixin,DetailView):
   # model = User
    #template_name = "view_profile.html"


class ProfileView(LoginRequiredMixin,UserPassesTestMixin):
       
   #    model = User
   #    fields = ['name','city','phone','sport','experience','mode']
   #    template_name_suffix = '_update_form'
    #   success_url = reverse_lazy(view.home)


    def detail_view(request,user):
        context={}
        context["user"] = get_object_or_404(User,username=user)
    

        return render(request , "view_profile.html",context)

    def update_view(request,user):
        context={}
        obj = get_object_or_404(User,username=user)
        form = EditProfileForm(request.POST or None, instance = obj)
        if form.is_valid():
         form.save()
         return HttpResponseRedirect("/profile/"+user+"/")
        context["form"] = form
        return render(request,"user_update_form.html",context)

    def test_func(request,user) :
        x = request.user
        y = user
        if x == y :
            return True
        else:
            if request.user.is_authenticated():
                raise Http404("This is not your account to edit")






# def register(response):
#    if response.method == "POST":
 #       form = UserForm(response.POST)
  #      if form.is_valid():
   #         form.save()
    #        return redirect("/home")
    # else:
    #   form = UserForm()

    # return render(response, 'register.html', {'form': form})
