from django.shortcuts import render, redirect #, get_object_or_404

from .models import *
# import django users:
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    #bookmarks = get_object_or_404(Bookmarks, pk=request.user.pk)
    try:
        bookmarks = Bookmarks.objects.filter(user=request.user)
    except:
        return redirect('auth_index')
    
    return render(request, 'bookmarks/index.html', {"bookmarks":bookmarks})


def add(request):
    if request.method == 'POST':
        url = request.POST['url']
        title = request.POST['title']
        description = request.POST['description']
        user = request.user

        print(url, title, description, user)
        
        bookmark = Bookmarks(user=user, url=url, title=title, description=description)
        bookmark.save()
        return redirect('/home')
    
    return redirect('/home')


def edit(request, id):
    if request.method == "POST":
        bookmark = Bookmarks.objects.get(id=id)
        bookmark.url = request.POST['edit_url']
        bookmark.title = request.POST['edit_title']
        bookmark.description = request.POST['edit_description']
        bookmark.save()
        return redirect('/home')
    
    return redirect('/home')


def delete(request, id):
    if request.method == "POST":
        bookmark = Bookmarks.objects.get(id=id)
        bookmark.delete()
    return redirect('/home')