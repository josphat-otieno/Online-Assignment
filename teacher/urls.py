from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'teacher'
urlpatterns = [ 
    path('', views.index, name='index'),
]