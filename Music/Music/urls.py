from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # Admin Panel URL
                  path('admin/', admin.site.urls),  # Django admin interface

                  # Include your app's URLs
                  # Example for the music app (adjust for your app name)
                  path('', include('app.urls')),  # You can also have other paths like this

                  # You can add other app URLs here similarly
                  # path('another-app/', include('another_app.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)