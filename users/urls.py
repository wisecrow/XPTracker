from django.conf.urls import url
from users.views import show_index

urlpatterns = [
    url(r'^developers', show_index, name='show_index')
]