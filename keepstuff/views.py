from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *

class CurrentStuff(ListView):
    model = Stuff

class Log(ListView):
    model = Entry
