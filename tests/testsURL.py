from atexit import register
from urllib import request, response
from django.test import TestCase
from teammatcherapp.forms import RegisterForm

from teammatcherapp.models import User

# Create your tests here.
class URLTests(TestCase):
    def test_homepage(self):
        response1 = self.client.get('/')
        response2 = self.client.get('/home/')
        self.assertEquals(response1.status_code, 200)
        self.assertEquals(response1.status_code,response2.status_code)

    def test_search(self):
        response1 = self.client.get('/search/')
        response2 = self.client.get('/home/search/')
        self.assertEquals(response1.status_code,200)
        self.assertEquals(response1.status_code,response2.status_code)

    def test_register(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)
    
    def test_gdpr(self):
        response = self.client.get('/gdpr/')
        self.assertEquals(response.status_code,200)

    def test_leaderboard(self):
        response = self.client.get('/leaderboard/')
        self.assertEquals(response.status_code,200)

    def test_shop(self):
        response = self.client.get('/shop/')
        self.assertEquals(response.status_code,200)



    

    
        

    
