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
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Event

# Create your views here.
# added
#- handled by a function
#def listEvents(request):
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
#- login required, the view should inherit from LoginRequiredMixin (as the
#- leftmost parent class)
class EventListView(LoginRequiredMixin, generic.ListView):
#    # if not logged in, this view will be redirected to its login_url
#    # (/accounts/login/ as default) with this path as a query string named
#    # "next" (<login_url>?next=<request.path>), and then redirecting back here
#    # after the successful login (according to the next=<request.path>)
#    # using reverse to generate the url to prevent hard coding
#    login_url = reverse('login')
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
        # showing only the current user's event
        # the implementation of the user depends on the session, which in turn 
        # depends on cookie; http supports server using the "set-cookie" header
        # in the response (in addition to the request/response line and body,
        # there can also be headers in the request/response) to instruct the
        # browser to save specified data (called cookies) to its local storage;
        # a cookie is a named value, such as:
        # <name>=<value>;domain=<domain>;path=<path>;expires=<date>
        # once there are matching (domain and path) and unexpired cookies for a
        # requested URL, the browser will send its name-value pair to the server
        # with the "cookie" header in the request. cookies are used to associate
        # multiple different http interactions; an http interaction includes the
        # client establishing a connection with the server, and then the client
        # sending a request, and the server returning a response, then the
        # connection being disconnected. multiple interactions use different
        # connections, and each interaction neither can get any information
        # about the previous interaction; in short, the server doesn't know what
        # the client has done before; through the cookie, the server can write
        # some information to the client as its id, and the request sent by the
        # client then contains its id, and then the server can identify
        # different clients, and records the interaction history with the
        # specified client; the multiple interactions associated with each other
        # are called sessions; in django, for security, only a sessionid is
        # saved in the cookie, the session data is saved in the django_session
        # table on the server, the value of sessionid is the primary key of this
        # table, and the server can get the session data (request.session)
        # according to the sessionid of the client; the user is also a kind of
        # session data, after a successful login, the user id will be saved in
        # the session, and request.user can be used directly to get the current
        # (logged in) user (it is AnnonymousUser if no user logged in)
        # showing the undue tasks if matching "todolist" pattern (/events/todo/)
        if self.request.resolver_match.url_name == 'todoList':
            return Event.objects.filter(
                user=self.request.user,
                time__gte=timezone.now()).order_by('time')
        # showing the events of selected date if matching "eventList" pattern
        return Event.objects.filter(
            user=self.request.user,
            time__year=self.request.resolver_match.kwargs['year'],
            time__month=self.request.resolver_match.kwargs['month'],
            time__day=self.request.resolver_match.kwargs['day']).order_by(
                'time')

    # add context
    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)

        # to display the current username
        if self.request.user.first_name or self.request.user.last_name:
            context['username'] = \
                self.request.user.first_name + ' ' + self.request.user.last_name
        else:
            context['username'] = self.request.user.username

        # to display the date for the query result of the specified date
        if self.request.resolver_match.url_name == 'eventList':
            context['date'] = '%s-%s-%s' % (
                self.request.resolver_match.kwargs['year'],
                self.request.resolver_match.kwargs['month'],
                self.request.resolver_match.kwargs['day'])

        return context

#- login required, using the decorator, with the same logic as the
#- LoginRequiredMixin above (login_url is available as the decorator parameter,
#- such as "@login_required(login_url=reverse('login')))
@login_required
def eventDetail(request, event_id):
#    return HttpResponse("You're looking at event %s." % event_id)
#    # if the query failed then raising Http404 exception (return 404 response)
#    try:
#        event = Event.objects.get(pk=event_id)
#    except Event.DoesNotExist:
#        raise Http404("Event does not exist")
    # using get_object_or_404 shortcut; get_list_or_404 uses the filter function
    # instead of the get function
    event = get_object_or_404(Event, pk=event_id)
    # only showing the events of current user, otherwise redirect to login
    if event.user.id != request.user.id:
        return HttpResponseRedirect(
            '%s?next=%s' % (reverse('login'), request.path))

    return render(request, 'event_detail.html', { 'event': event, })
#- the detail view query the context object of the specified model class with
#- the primary key captured from the url
#- if using the detail view, events of other users will result in 404 due to
#- query failure instead of redirecting to login, so still using the function
#class EventDetailView(LoginRequiredMixin, generic.DetailView):
##    model = Event
#    # <app>/<model>_detail.html as default, such as events/event_detail.html
#    template_name = 'event_detail.html'
##    # <model> as default, such as event
##    context_object_name = 'event'
#
#    # showing only the current user's event
#    def get_queryset(self):
#        return Event.objects.filter(user=self.request.user)

#-
@login_required
def modEvent(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    # modifying only the current user's events
    if event.user.id != request.user.id:
        return HttpResponseRedirect(
            '%s?next=%s' % (reverse('login'), request.path))

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
@login_required
def eventNew(request):
    return render(request, 'event_detail.html', { 'event': None, })

#-
@login_required
def addEvent(request):
    request.user.event_set.create(title=request.POST['title'],
        description=request.POST['description'], time=request.POST['time'])
    return HttpResponseRedirect(reverse('todoList'))

#-
@login_required
def calendar(request):
    return render(request, 'calendar.html')

#-
@login_required
def search(request):
    lst=request.POST['date'].split('-')
    return HttpResponseRedirect(reverse('eventList',
        args=(lst[0], lst[1], lst[2])))

#- email reminder, as a scheduled task
def remind():
    # reminding 10 mins before the due time
    todolist = Event.objects.filter(
        time__gte=timezone.now(),
        time__lte=timezone.now()+datetime.timedelta(minutes=10))

    subject = 'Event Reminder'
    email_from = settings.EMAIL_HOST_USER
    for event in todolist:
        # - NZST conversion, since it is the UTC time in the database
        message = '%s --- %s\n%s' % (
            event.title,
            event.time.astimezone(
                datetime.timezone(datetime.timedelta(hours=12))),
            event.description)
        recipient_list = [ event.user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        event.save()
