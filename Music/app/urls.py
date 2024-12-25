from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('album/<int:pk>/', views.album_detail_view, name='album_detail'),
    path('search/', views.search_view, name='search'),
    path('favorite/<int:album_id>/', views.favorite, name='favorite'),
    path('favorite_view/', views.favorite_view, name='favorite_view'),
    path('play_song/<int:song_id>/', views.play_song, name='play_song'),

]
