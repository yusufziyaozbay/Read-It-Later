from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='auth_index'),
    path('login/', views.user_login, name='auth_user_login'),
    path('signup/', views.user_signup, name='auth_user_signup'),
    path('logout/', views.user_logout, name='auth_user_logout'),
]
