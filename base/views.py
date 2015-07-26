""" Views for the base application """

from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')
    
def profile(request):
    return  render_to_response("user/profile.html",
                               locals(),
                               context_instance  = RequestContext(request))    
