from django.shortcuts import render
from django.http import  HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters=list('qazwsxedcrfvtgbyhnujmikolp')
    length=int(request.GET.get('length',10))
    is_uppercase=request.GET.get('uppercase')
    is_special=request.GET.get('special')
    is_numbers=request.GET.get('numbers')
    thepassword=""
    if is_uppercase:
        characters.extend(list('QAZWSXEDCRFVTGBYHNUJMIKOLP'))
    if is_numbers:
        characters.extend(list('1234567890'))
    if is_special:
        characters.extend(list('!@#$%^&*()_-+*'))
    for i in range (length):
        thepassword+=random.choice(characters)
    return render(request, 'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')