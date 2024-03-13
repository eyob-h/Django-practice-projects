from django.contrib import admin
from django.urls import path, include

# Media static file configuration
from django.conf.urls.static import static
from django.conf import settings
from listing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.view_listings, name='view_listings'),
    path('listing/', include('listing.urls')),
    path('owners/', include('owners.urls')),
    # path('', include('listing.urls')),
    # path('/listing', include('listing.urls')) Didn't work
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)