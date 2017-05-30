from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CurrentStuff.as_view()),
    url(r'^recalc$', views.recalc),
]

