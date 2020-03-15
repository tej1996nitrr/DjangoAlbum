
from django.urls import path,include
from .views import home, about
urlpatterns = [
    
    path('', home,name='album-home' ),
    path('about/',about,name='album-about')
]
