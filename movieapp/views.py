from django.http import HttpResponse
from .models import Movie
from django.shortcuts import render, redirect
from .forms import movieform


# Create your views here.
def fun(request):
    
    movie=Movie.objects.all
    context={'movie_list':movie}
    return render (request,"index.html",context)

def details(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})

def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        Year = request.POST.get('Year',)
        price= request.POST.get('price',)
        img  = request.FILES['img']

        movie=Movie(name=name,Year=Year,price=price,img=img)
        movie.save(),
    return render(request,'add.html')

def update(request, id):
    movie = Movie.objects.get(id=id)
    form  = movieform(request.POST or None, request.FILES, instance =movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render (request ,'edit.html',{'form':form,'movie':movie})

def delet(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delet.html')