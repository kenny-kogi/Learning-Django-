from django.urls import path
from . import views
urlpatterns = [
    path('', views.myfunctioncall,name='index'),
    path('math', views.math1,name='math'),
    path('subtract/<int:a>/<int:b>', views.subtract,name='subtract'),
    path('year/<str:name>/<int:yob>', views.year, name ='year'),
    path('myfirstapp', views.app, name ='myfirstapp'),
    path('mysecondapp', views.app2, name ='mysecondapp'),
    path('mythirdapp', views.app3, name ='mythirdapp'),
    path('imageapp', views.app4, name ='imageapp'),
    path('imageapp2', views.app5, name ='imageapp2'),
    path('imageapp3/<str:name>', views.app6, name ='imageapp3')


]