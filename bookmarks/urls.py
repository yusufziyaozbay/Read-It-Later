from django.urls import path
from . import views


app_name = 'bookmarks'

urlpatterns = [
    path('home/', views.index, name='index'),
    # Link operations
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    # Link tags
    path('autoread/<int:bookmark_id>', views.autoread, name='autoread'),
    path('read/', views.read, name='read'),
    path('btnread/<int:bookmark_id>', views.btnread, name='btnread'),
    path('archive/', views.archive, name='archive'),
    path('btnarchive/<int:bookmark_id>', views.btnarchive, name='btnarchive'),
    path('favorite/', views.favorite, name='favorite'),
    path('btnfavorite/<int:bookmark_id>', views.btnfavorite, name='btnfavorite'),
    path('search/', views.search, name='search')
]