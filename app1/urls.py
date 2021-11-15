from django.urls import path
from django.urls.resolvers import URLPattern
from app1.views import *
app_name='app1'


urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('rohit/',rohit,name='rohit'),
]