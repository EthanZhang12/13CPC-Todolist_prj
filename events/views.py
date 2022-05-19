# added
import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect#, HttpResponse, Http404
from django.urls import reverse
from django.views import generic
from django.conf import settings
from django.core.mail import send_mail
#from django.template import loader

# modified: shortcuts, get_object_or_404 added
from django.shortcuts import render, get_object_or_404

# added
from .models import Event

# Create your views here.
# added
#- handled by a function
#def listEvent(request):
#    unexpired_event_list = Event.objects.filter(
#        time__gte=timezone.now()).order_by('time')
##    # directly output the response
##    output = ', '.join([e.title for e in unexpired_event_list])
##    return HttpResponse(output)
##    # render the response from the template
##    template = loader.get_template('event_list.html')
##    context = {
##        'unexpired_event_list': unexpired_event_list, }
##    return HttpResponse(template.render(context, request))
#    # using the template rendering shortcut
#    return render(request, 'event_list.html', {
#        'unexpired_event_list': unexpired_event_list, })
#- handled by a list view
class EventListView(generic.ListView):
#    # model class
#    model = Event
    # template, <app>/<model>_list.html as default, such as
    # events/event_list.html
    template_name = 'event_list.html'
#    # context object, <model>_list as default, such as event_list
#    context_object_name = 'unexpired_event_list'

    # if defined, then model class is specified by this (even if model
    # specified)
    def get_queryset(self):
        return Event.objects.filter(
            time__gte=timezone.now()).order_by('time')

#-
#def eventDetail(request, event_id):
##    return HttpResponse("You're looking at event %s." % event_id)
##    # if the query failed then raising Http404 exception (return 404 response)
##    try:
##        event = Event.objects.get(pk=event_id)
##    except Event.DoesNotExist:
##        raise Http404("Event does not exist")
#    # using get_object_or_404 shortcut; get_list_or_404 uses the filter
#    # function instead of the get function
#    event = get_object_or_404(Event, pk=event_id)
#
#    return render(request, 'event_detail.html', { 'event': event, })
#- the detail view query the context object of the specified model class with
#- the primary key captured from the url
class EventDetailView(generic.DetailView):
    model = Event
    # <app>/<model>_detail.html as default, such as events/event_detail.html
    template_name = 'event_detail.html'
#    # <model> as default, such as event
#    context_object_name = 'event'

#-
def modEvent(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    action = request.POST['submit']

    # delete
    if action == 'Delete':
        event.delete()
        # always return a redirect response for a successful post request
        # redirecting to "events/todo/"
        return HttpResponseRedirect(reverse('todoList'))

    # modify
    event.title = request.POST['title']
    event.description = request.POST['description']
    event.time = request.POST['time']
    event.save()
    return HttpResponseRedirect(reverse('todoList'))

#-
def eventNew(request):
    return render(request, 'event_detail.html', { 'event': None, })

#-
def addEvent(request):
    event = Event(title=request.POST['title'],
        description=request.POST['description'], time=request.POST['time'])
    event.save()
    return HttpResponseRedirect(reverse('todoList'))
