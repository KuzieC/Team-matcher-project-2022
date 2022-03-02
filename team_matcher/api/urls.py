from django.urls import path
from .views import PersonView #CreateSearchView

urlpatterns = [ #both functions and classes can be views
    path('person', PersonView.as_view()), #call the function (defined in views)
    #path('doSearch', CreateSearchView.as_view()),
    #path('', main)
]