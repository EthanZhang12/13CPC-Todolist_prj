"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# modified：include added to import
from django.urls import include, path
# added
from django.views import generic

# root urlconf (set in todolist/settings.py), the url received in the http
# request will be matched with it at first; note that in a url such as
# "http://localhost:8000/events/", "/events/" is the path part (without query
# string), and only the part after root ("/") in the path will be matched
# (such as "events/"); and note that a url can also omit the host (domain) and
# port before the path part, and the default is the current server; and note
# that the browser uses "/" as the default path, for example, if
# "http://localhost:8000" entered in the address bar, the browser will add "/"
# at the end automatically (http://localhost:8000/)
urlpatterns = [
    # added: after the matched part (such as "events/") removed, the remaining
    # part will be processed by the specified urlconf (such as (urlpatterns in)
    # events/urls.py)
    path('events/', include('events.urls')),
    # - redirecting "/" to "events/todo/", which is referenced by its
    # - pattern_name "todoList" defined in events/urls.py
    path('', generic.RedirectView.as_view(pattern_name='todoList')),
    # using include() to use other urlconf, except admin.site.urls
    path('admin/', admin.site.urls),
]
