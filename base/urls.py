"""urlconf for the base application"""

from django.conf.urls import url
from base.views import home


urlpatterns =[
    url(r'^$', home),
]
