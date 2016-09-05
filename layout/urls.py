"""urlconf for the layout application"""

from django.conf.urls import url
from layout.views import home


urlpatterns =[
    url(r'^$', home),
]
