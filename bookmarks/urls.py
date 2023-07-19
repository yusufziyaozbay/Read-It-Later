from django.urls import path
from . import views


#app_name = 'bookmarks'

urlpatterns = [
    path('home/', views.index, name='bookmarks_index'),
    path('add/', views.add, name='bookmarks_add'),
    path('edit/<int:id>', views.edit, name='bookmarks_edit')
]