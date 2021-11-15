from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('hai this app1 dhoni')

def rohit(request):
    return HttpResponse('Rohit the Hitman')