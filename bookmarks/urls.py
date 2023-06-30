from django.urls import path
from . import views


#app_name = 'bookmarks'

urlpatterns = [
    path('home/', views.index, name='bookmarks_index'),
]