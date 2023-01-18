from django.shortcuts import render,HttpResponse
import random

# Create your views here.

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters=list('abcdefghijklmnopqresuvwxyz')
    generate_password=""

    lenght=int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!"·$%&/()#-=+-*/'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    for i in range(lenght):
        generate_password+= random.choice(characters)


    return render(request, 'generator/password.html',{'password': generate_password})