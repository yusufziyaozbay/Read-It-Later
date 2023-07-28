from django.shortcuts import render, redirect #, get_object_or_404

from .models import *
from django.contrib import messages
# import django users:
from django.contrib.auth.models import User
# For link previews:
import requests
from bs4 import BeautifulSoup


# Create your views here.
def index(request):
    #bookmarks = get_object_or_404(Bookmarks, pk=request.user.pk)
    try:
        bookmarks = Bookmarks.objects.filter(user=request.user)
    except:
        return redirect('auth_index') # DIKKATT
    
    if not bookmarks:
        messages.info(request, 'There are no records yet :/')
    
    return render(request, 'bookmarks/index.html', {'bookmarks' : bookmarks})


def add(request):
    if request.method == 'POST':
        url = request.POST['url']
        og_data = get_og_data(url)
        if og_data == '':
            return redirect('index')

        # title = request.POST['title']
        # description = request.POST['description']
        
        title = og_data['title']
        description = og_data['description']
        image = og_data['image']
        user = request.user

        print(url, title, description, user, image)
        
        bookmark = Bookmarks(user=user, url=url, title=title, description=description, image=image)
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


def get_og_data(url):
    try:
        response = requests.get(url)
    except:
        print('an error has occurred :/')
        og_data = ''
        return og_data
    soup = BeautifulSoup(response.text, 'html.parser')
    og_data = {
        'title': get_og_meta(soup, 'og:title'),
        'description': get_og_meta(soup, 'og:description'),
        'image': get_og_meta(soup, 'og:image'),
        # 'url': get_og_meta(soup, 'og:url'),
    }
    return og_data


def get_og_meta(soup, property_name):
    meta_tag = soup.find('meta', property=property_name)
    return meta_tag['content'] if meta_tag else ''
