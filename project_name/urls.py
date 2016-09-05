""" Default urlconf for {{ project_name }} """

from django.conf.urls import include, url
from django.contrib import admin
from layout.views import profile
from django.conf import settings
from django.contrib.auth.views import logout
from django.views.static import serve
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = [
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^bad/$', bad),
    url(r'', include('layout.urls')),
    #all-auth 
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile', profile),    
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]

    
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ url(r'^__debug__/', include(debug_toolbar.urls)),]
