from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users, name='users'),
    path('users/list', views.listUsers, name='listUsers'),
    path('users/<str:ID>', views.userID, name='userID'),
    path('unknown', views.resource, name='resource'),
    path('unknown/list', views.listunknown, name='listunknown'),
    path('unknown/<str:ID>', views.unknownID, name='unknownID'),
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('sendResource', views.sendResource, name='sendResource'),
    path('sendPeople', views.sendPeople, name='sendPeople'),

]