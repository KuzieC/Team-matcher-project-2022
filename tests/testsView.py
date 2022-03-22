from atexit import register
from urllib import request, response
from django.test import TestCase
from teammatcherapp.forms import RegisterForm

from teammatcherapp.models import User

class ViewTest(TestCase):
    def setUp(self):
        user1 = User(name = 'Toyosi Olaribigbe',postcode ='E9 6LG',gender = 'male',phone = '07709863521',age = 7,sport ='football',experience = 'beginner',username = 'prince',password='password',mode = 'team')
        user2 = User(name = 'David Olaribigbe',postcode ='E9 B2S',gender = 'female',phone = '07745863521',age = 17,sport ='basketball',experience = 'profess',username = 'price',password='paword',mode = 'team')
        user3 = User(name = 'Tom smith',postcode ='SW17 42',gender = 'female',phone = '07746763521',age = 27,sport ='volleyball',experience = 'intermediate',username = 'pri',password='applejuice',mode = 'compete')
        user4 = User(name = 'Tommy bile',postcode ='SW17 62',gender = 'male',phone = '07746763532',age = 56,sport ='football',experience = 'intermediate',username = 'pro',password='appluice',mode = 'compete')
        user1.save()
        user2.save()
        user3.save()
        user4.save()

    def test_if_exists_and_all_stored(self):
        count = User.objects.all().count()
        self.assertEqual(count,4)
    
    def test_same_info(self):
        user5 = User(name = 'Toyosi Olaribigbe',postcode ='SW17 62',gender = 'male',phone = '07746763532',age = 56,sport ='football',experience =           'intermediate',username = 'prime',password='appluice',mode = 'compete')
        user5.save()
        one = User.objects.get(username ='prime')
        two = User.objects.get(username ='pro')
        self.assertEquals(one.age,two.age)
        self.assertEquals(one.phone,two.phone)
        self.assertNotEquals(one.name,two.name)
   
    def info_retained(self):
        one = User.objects.get(name ='David Olaribigbe')
        two = User.objects.get(name ='Toyosi Olaribigbe')
        three = User.objects.get(name = 'Tom smith')
        self.assertEquals(two.name,'Toyosi Olaribigbe')
        self.assertEquals(one.postcode,'E9 B2S')
        self.assertNotEquals(one.name,two.name)
        self.assertEquals(two.postcode,'E9 6LG')
        self.assertEquals(three.sport,'volleyball')
        self.assertEquals(three.phone,'07746763521')
