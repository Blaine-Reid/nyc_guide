from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    """ View rendered for '/' url pattern"""

    def get(self, request):
        return render(
            request=request,
            # render "city.html"
            template_name='city.html',
            # send 'city.html' context to display or use 
            context={
                'boroughs': boroughs.keys()
                })


class BoroughView(View):
    """View rendered for '<str:borough>' url pattern"""

    def get(self, request, borough):
        return render(
            request=request,
            # render 'borough.html'
            template_name='borough.html',
            # send 'borough.html' context to display or use 
            context={
                'borough': borough, 
                'activities': boroughs[borough].keys()
                })


class ActivityView(View):
    """View rendered for '<str:borough>/<str:activity>' url pattern"""

    def get(self, request, borough, activity):
        return render( 
            request=request, 
            # render 'activity.html'
            template_name= 'activity.html',
            # send 'activity.html' context to display or use  
            context={
                'borough': borough, 
                'activity': activity,
                'venues': boroughs[borough][activity].keys()
                })
        
class VenueView(View):  
    """View rendered for '<str:borough>/<str:activity>/<str:venue>' url pattern"""

    def get(self, request, borough, activity, venue):
        return render(
        request=request,
        # render 'venues.html'
        template_name= 'venues.html',
        # send 'venue.html' context to display or use  
        context={
            'borough': borough,
            'venue': venue, 
            'description' : boroughs[borough][activity][venue]['description']
            })