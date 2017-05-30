from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from datetime import datetime
from .models import *

class CurrentStuff(ListView):
    model = Stuff

class Log(ListView):
    model = Entry

def recalc(request):
    """
    get the latest Entry for each Stuff that is absolute measurement, else 0.
    get the in/decrments that are younger than this.
    update the stock value.
    """
    for stuff in Stuff.objects.all():
        last_abs = Entry.objects.filter(stuff=stuff,isabs=True)
        if last_abs:
            last_abs = last_abs.order_by('-time')[0]
            stuff.quant = last_abs.quant
            time = last_abs.time
        else:
            stuff.quant = 0
            time = datetime.min

        for inc in Entry.objects.filter(stuff=stuff,isabs=False,time__gt=time):
            stuff.quant += inc.quant
        stuff.save()

    return HttpResponseRedirect('/')
