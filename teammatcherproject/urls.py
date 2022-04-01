"""teammatcherproject URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from teammatcherapp import view
from rest_framework.authtoken import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home),
    path('search/',view.search),
    path('home/search/',view.search),
    path('home/',view.home),
    path('gdpr/',view.gdpr),
    path('shop/',view.shop),
    path('leaderboard/',view.leaderboard),
    path('register/',view.register, name="register"),
    path('api/v1/',include('api.urls')),
    path('api-token-auth/',views.obtain_auth_token,name = 'api-toekn-auth')
]
