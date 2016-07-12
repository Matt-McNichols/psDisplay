from django.conf.urls import url
from dispPoc import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    ]
