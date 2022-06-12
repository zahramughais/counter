from itertools import count
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")
        request.session['count'] = 0
    if 'visit' in request.session:
        request.session['visit'] += 1
        print('key exists!')
    else:
        print("key 'visit' does NOT exist")
        request.session['visit'] = 1
    
    return render(request, 'index.html')

def destroy(request):
    del request.session['count']
    return redirect ('/')

def add_2(request):
    request.session['count'] += 1
    return redirect ('/')

def add_by(request):
    num_from_form = request.POST['num']
    print(num_from_form)
    request.session['count'] += (int(num_from_form)-1)
    return redirect ('/')
