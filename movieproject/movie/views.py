from urllib import response
from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = '64892459019c27d851fbdfb055507f94'

def home(request):
    if request.method =='POST':
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
    
        if form.is_valid():
            url = "https://api.themoviedb.org/3/search/movie?api_key=" + my_id + '&query='+searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            
            return render(request, 'search.html',{'obj':obj})
        
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj = obj['results']
    return render(request, 'index.html', {'obj':obj})

def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key='+my_id
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html',{"resdata":resdata})