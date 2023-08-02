from django.shortcuts import render, redirect #, get_object_or_404

from .models import *
from django.contrib import messages
# import django users:
from django.contrib.auth.models import User
# For link previews:
import requests
from bs4 import BeautifulSoup
import re


# Create your views here.
def index(request):
    #bookmarks = get_object_or_404(Bookmarks, pk=request.user.pk)
    try:
        bookmarks = Bookmarks.objects.filter(user=request.user, readed=False)
    except:
        return redirect('/')
    
    # if not bookmarks:
    #     messages.info(request, 'There are no records yet :/')

    tags_count = bookmarks_tags_count(request)
    
    context = {
        'bookmarks' : bookmarks,
        'current_page' : 'index',
        'tags_count' : tags_count,
    }
    return render(request, 'bookmarks/index.html', context)


def add(request):
    if request.method == 'POST':
        url = request.POST['url']
        og_data = get_og_data(url)
        if og_data == '':
            return redirect('/')
        
        title = og_data['title']
        description = og_data['description']
        image = og_data['image']
        user = request.user
        
        bookmark = Bookmarks(user=user, url=url, title=title, description=description, image=image)
        bookmark.save()
        return redirect('/home/')
    
    return redirect('/home/')


def edit(request, id):
    if request.method == "POST":
        bookmark = Bookmarks.objects.get(id=id)
        bookmark.url = request.POST['edit_url']
        bookmark.title = request.POST['edit_title']
        bookmark.description = request.POST['edit_description']
        bookmark.save()
        print('mesaj calistii')
        messages.info(request, '"' + bookmark.title + '" edited.')
    
    return redirect('/home')


def delete(request, id):
    if request.method == "POST":
        bookmark = Bookmarks.objects.get(id=id)
        bookmark.delete()
        messages.info(request, '"' + bookmark.title + '" deleted.')

    return redirect('/home/')


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


def autoread(request, bookmark_id):
    if request.method == "POST":
        try:
            bookmark = Bookmarks.objects.get(id=bookmark_id)
        except:
            return redirect('/home/')

        if bookmark.readed == False:
            bookmark.readed = True
            bookmark.save()
            messages.info(request, '"' + bookmark.title + '" readed.')

    return redirect('/home/')


def read(request):
    # Get readed bookmarks
    try:
        bookmarks = Bookmarks.objects.filter(user=request.user, readed=True)
    except:
        return redirect('/')
    
    # if not bookmarks:
    #     messages.info(request, 'There are no read yet :/')

    tags_count = bookmarks_tags_count(request)

    context = {
        'bookmarks' : bookmarks,
        'current_page' : 'read',
        'tags_count' : tags_count,

    }
    return render(request, 'bookmarks/read.html', context)


def btnread(request, bookmark_id):
    if request.method == 'POST':
        try:
            bookmark = Bookmarks.objects.get(id=bookmark_id)
        except:
            return redirect('/home/')

        if bookmark.readed == False:
            bookmark.readed = True
            messages.info(request, '"' + bookmark.title + '" readed.')
        else:
            bookmark.readed = False

        bookmark.save()
    return redirect('/home/')


def archive(request):
    try:
        bookmarks = Bookmarks.objects.filter(user=request.user, archived=True)
    except:
        return redirect('/')
    
    # if not bookmarks:
    #     messages.info(request, 'There are no archive yet :/')
    
    tags_count = bookmarks_tags_count(request)

    context = {
        'bookmarks' : bookmarks,
        'current_page' : 'archive',
        'tags_count' : tags_count,

    }
    return render(request, 'bookmarks/archive.html', context)


def btnarchive(request, bookmark_id):
    if request.method == 'POST':
        try:
            bookmark = Bookmarks.objects.get(id=bookmark_id)
        except:
            return redirect('/home/')

        if bookmark.archived == False:
            bookmark.archived = True
            messages.info(request, '"' + bookmark.title + '" archived.')
        else:
            bookmark.archived = False

        bookmark.save()
    return redirect('/home/')


def favorite(request):
    try:
        bookmarks = Bookmarks.objects.filter(user=request.user, favorited=True)
    except:
        return redirect('/')
    
    # if not bookmarks:
    #     messages.info(request, 'There are no favorite yet :/')
    
    tags_count = bookmarks_tags_count(request)

    context = {
        'bookmarks' : bookmarks,
        'current_page' : 'favorite',
        'tags_count' : tags_count,

    }
    return render(request, 'bookmarks/favorite.html', context)


def btnfavorite(request, bookmark_id):
    if request.method == 'POST':
        try:
            bookmark = Bookmarks.objects.get(id=bookmark_id)
        except:
            return redirect('/home/')
        
        if bookmark.favorited == False:
            bookmark.favorited = True
            messages.info(request, '"' + bookmark.title + '" favorited.')
        else:
            bookmark.favorited = False

        bookmark.save()
    return redirect('/home/')


def bookmarks_tags_count(request):
    try:
        bookmarks_saves = Bookmarks.objects.filter(user=request.user, readed=False)
        bookmarks_archived = Bookmarks.objects.filter(user=request.user, archived=True)
        bookmarks_favorited = Bookmarks.objects.filter(user=request.user, favorited=True)
        bookmarks_readed = Bookmarks.objects.filter(user=request.user, readed=True)
    except:
        return ''
    
    tags_count = {
        'bookmarks_saves' : bookmarks_saves.count,
        'bookmarks_archived' : bookmarks_archived.count,
        'bookmarks_favorited' : bookmarks_favorited.count,
        'bookmarks_readed' : bookmarks_readed.count,
    }
    return tags_count


def search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        # bookmarks = Bookmarks.objects.filter(user=request.user, title=search_text)
        bookmarks = Bookmarks.objects.filter(user=request.user, title__icontains=search_text)
        tags_count = bookmarks_tags_count(request)

        context = {
            'bookmarks' : bookmarks,
            # 'current_page' : 'search',
            'tags_count' : tags_count,
            'searched_text' : search_text,
        }

        return render(request, 'bookmarks/index.html', context)

    return redirect('/home/')