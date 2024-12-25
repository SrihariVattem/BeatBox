from django.contrib import admin
from .models import Album, Song, Profile

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')  # Fields to display in the admin list view
    search_fields = ('title', 'artist')  # Add search functionality
    list_filter = ('artist',)  # Add filter options

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'duration')  # Display song details
    search_fields = ('title', 'album__title')  # Add search for song and album
    list_filter = ('album',)  # Filter by album

from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_favorites')  # Customize displayed columns

    def get_favorites(self, obj):
        # Corrected to use the 'favorites' field from the model
        return ", ".join([album.title for album in obj.favorites.all()])
    get_favorites.short_description = 'Favorite Albums'
