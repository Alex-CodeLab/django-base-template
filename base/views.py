""" Views for the base application """

from django.shortcuts import render, render_to_response, HttpResponseRedirect
import django

def home(request):
    """ Default view for the root """
    djangoversion = django.get_version()
    return render(request, 'base/home.html',{'djangoversion':djangoversion })


return render(request, 'base/home.html')
    
def profile(request):
    return  render(request, "user/profile.html" )    
