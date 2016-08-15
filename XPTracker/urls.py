"""XPTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from project import views

from users.views import show_index, new_developer
from user_stories import views as us_views
from iterations import views as iterations_views
from tasks import views as tasks_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^projects/(.+)/user_stories/new/', us_views.new_us, name='new_us'),
    url(r'^projects/(.+)/developers/new/', new_developer, name='new_developer'),
    url(
        r'^projects/(.+)/user_stories/',
        us_views.show_us_index,
        name='us_index'),
    url(r'^projects/(.+)/tasks/', tasks_views.show_index, name='show_tasks_index'),
    url(r'^projects/(.+)/iterations/new/', iterations_views.create_new, name='new_iteration'),
    url(r'^projects/(.+)/iterations/', iterations_views.show_index, name='show_iteration_index'),
    url(r'^projects/(.+)/developers/', show_index, name='show_users_index'),
    url(r'^projects/new/', views.new_project, name='new_project'),
    url(r'^projects/(.+)/', views.show_project, name='show_project'),
    url(r'^projects/', views.show_projects, name='show_projects'),
    url(r'^$', views.show_index, name='home'),

]
