""" Default urlconf for {{ project_name }} """

from django.conf.urls import include, url
from django.contrib import admin
from base.views import profile
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
    url(r'', include('base.urls')),
    #all-auth 
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile', profile),    
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    
    
]
