from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Album, Song, Profile
from .forms import RegisterForm



from django.db.models import Q


def search_view(request):
    if request.method == 'POST':
        query = request.POST.GET('q', '')
        if query:
            albums = Album.objects.filter(title__icontains=query)
        else:
            albums = Album.objects.none()
    else:
        albums = Album.objects.none()

    return render(request, 'search_results.html', {'albums': albums, 'query': query})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    albums = Album.objects.all()  # Fetch all albums
    return render(request, 'home.html', {'albums': albums})  # Pass albums to the template


@login_required
def album_detail_view(request, pk):
    album = get_object_or_404(Album, pk=pk)
    songs = album.songs.all()  # Get all songs related to this album

    # Retrieve the currently playing song ID from the session, if available
    playing_song_id = request.session.get('playing_song_id', None)

    return render(request, 'album_detail.html', {
        'album': album,
        'songs': songs,
        'playing_song_id': playing_song_id  # Pass the playing song ID to the template
    })


@login_required
def play_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)

    # Store the currently playing song ID in the session
    request.session['playing_song_id'] = song.id

    # After setting the playing song, redirect back to the album detail view
    return redirect('album_detail', pk=song.album.id)



@login_required
def search_view(request):
    query = request.GET.get('q')
    albums = Album.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'albums': albums})


@login_required
def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    # Ensure the user has a Profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    if album in profile.favorites.all():
        # Remove album from favorites
        profile.favorites.remove(album)
    else:
        # Add album to favorites
        profile.favorites.add(album)

    # Redirect to the previous page or home
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def favorite_view(request):
    # Get the Profile for the logged-in user
    profile = Profile.objects.get(user=request.user)
    # Get the favorite albums from the profile
    favorite_albums = profile.favorites.all()

    return render(request, 'favorite_view.html', {'favorite_albums': favorite_albums})