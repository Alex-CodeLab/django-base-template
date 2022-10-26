""" Default urlconf for {{ project_name }} """

from django.conf.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from layout.views import profile
from django.conf import settings
from django.contrib.auth import logout
from django.views.static import serve
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = [

    path('admin/', admin.site.urls),
    path('bad/', bad),
    path('', include('layout.urls')),
    #all-auth 
    path('accounts/', include('allauth.urls')),
    path('accounts/profile', profile),    
    path('accounts/logout/', logout, {'next_page': '/'}),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ path('__debug__/', include('debug_toolbar.urls')),]
