from django.urls import path
from . import views


app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.user_signup, name='user_signup'),
    path('logout/', views.user_logout, name='user_logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]