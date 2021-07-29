from django.urls import path,include
from .views import QuizListView, quiz_view, quiz_data_view, save_quiz_view
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view

app_name = 'quizes'

urlpatterns = [ 
    path('', QuizListView.as_view(), name = 'main-view'),
    path('<int:pk>/', quiz_view, name='quiz-view'),
    path('<int:pk>/save', save_quiz_view, name='save_quiz-view'),
    path('<int:pk>/data/', quiz_data_view, name='quiz-data-view'),
    url(r'^new/question', views.create_quiz, name='new-question'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)