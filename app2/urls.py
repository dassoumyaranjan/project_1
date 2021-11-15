from django.urls import path
from django.urls.resolvers import URLPattern
from app2.views import *
app_name='app2'

urlpatterns=[
    path('kohli/',kohli,name='kohli'),
    path('soumya/',soumya,name='soumya'),
]