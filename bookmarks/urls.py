from django.urls import path
from . import views


app_name = 'bookmarks'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]