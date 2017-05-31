from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.stuff),
    url(r'^list$', views.CurrentStuff.as_view()),
    url(r'^recalc$', views.recalc),
    url(r'^log$', views.Log.as_view()),
]

