""" Views for the base application """

from django.shortcuts import render, render_to_response, HttpResponseRedirect

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')
    
def profile(request):
    return  render(request, "user/profile.html" )    
