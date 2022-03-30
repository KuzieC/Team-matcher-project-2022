from atexit import register
from random import choices
from urllib import request, response
from django.test import TestCase
from teammatcherapp.forms import RegisterForm, searchdetail

from teammatcherapp.models import User

class Formtests(TestCase):
    def test_invalid_regform(self):
         #one = User(name = 'David Olaribigbe',postcode ='E9 B2S',gender = 'Female' ,phone = '07745863521',age = 17 ,sport ='football',experience = 'advanced',username = 'price',password='paword')
         #one = User.objects.get(name ='David Olaribigbe')
         #data = {'name': one.name, 'postcode': one.postcode, 'gender': one.gender, 'phone': one.phone, 'age': one.age,'sport':one.sport,'experience':one.experience,'username':one.username,'password':one.password,'mode':one.mode}
         response = self.client.post('/register/',data = {'name': 'David Olaribigbe', 'city': 'Birmingham', 'gender': 'Female', 'phone': '07745863521', 'age': 17,'sport': 'football','experience': 'advanced','username': 'price','password': 'paword','mode': 'team'})
         form = RegisterForm({'name': 'David', 'city': 'Birmingham', 'Gender': 'Female', 'phone': '07745863521', 'age': 17, 'Sport': 'football','Experience': 'advanced','username': 'price','password': 'paword','mode': 'team'})
         self.assertFalse(form.is_valid())

    def test_invalid_input(self):
        form = RegisterForm({ 'name':'Dave','city':'Birmingham','gender':'Female','phone':'0774586356765563','age':17,'sport':'football','experience':'advanced','username':'price','password':'paword','mode':'team'})
        self.assertFalse(form.is_valid())
    
    def test_valid_searchform(self):
       form = searchdetail({ 'sport':'football','city':'Birmingham','mode':'team'})
       self.assertTrue(form.is_valid())

    def test_invalid_searchform(self):
        form = searchdetail({ 'sport':'football','city':' ','mode':'team'})
        self.assertFalse(form.is_valid())

    def test_outofbounds_searchform(self):
        form = searchdetail({ 'sport':'football','city':'ABCD123456Q','mode':'team'})
        self.assertFalse(form.is_valid())
