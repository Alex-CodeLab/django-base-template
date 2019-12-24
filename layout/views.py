""" Views for the layout application """

from django.shortcuts import render, HttpResponseRedirect
import django

def home(request):
    """ Default view for the root """
    djangoversion = django.get_version()
    return render(request, 'layout/home.html',{'djangoversion':djangoversion })

def profile(request):
    return  render(request, "user/profile.html" )    
