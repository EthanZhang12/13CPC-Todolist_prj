# added file

from django.urls import path
# added
from django.views import generic

# to handle matching url patterns with views (functions)
from . import views

# a namespace can be specified for the patterns to distinguish them with the
# same name in different apps, such as "events:detail"; of course, the
# pattern name itself can also be used to distinguish the app it belongs to, for
# example, "eventDetail"
#app_name = 'events'
# app urlconf, processing the remaining part of url after the part matched in
# the root urlconf removed, such as "todo/" in "events/todo/", the matching url
# will be handled by the corresponding view (function)
urlpatterns = [
#    # - e.g.: /events/
#    path('', views.listEvent, name='todoList'),
#    # - e.g.: /events/5/
#    # - "int:" here is for matching an integer, naming it as "event_id"
#    # - parameter of the pattern; the integer matched (5 in this example) is
#    # - then the value of the event_id parameter passed to the handling
#    # - function (here is views.eventDetail); or the parameter of a pattern can
#    # - be specified in reverse function to generate the url of this pattern,
#    # - for example, "reverse('eventDetail', args=(5))"
#    # - ("url 'eventDetail' '5'" in a template) generating "/events/5/"
#    path('<int:event_id>/', views.eventDetail, name='eventDetail'),
    path('<int:event_id>/modify/', views.modEvent, name='modEvent'),
    path('new/', views.eventNew, name='eventNew'),
    path('add/', views.addEvent, name='addEvent'),
    # handled by views derived from generic views (list view, detail view)
    path('', views.EventListView.as_view(), name='todoList'),
    #- the detail view captures the primary key (pk) of the context object
    #- from the url
    path('<int:pk>/', views.EventDetailView.as_view(), name='eventDetail'),
]
