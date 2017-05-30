from django.db.models import *

class Category(Model):
    name = CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Stuff(Model):
    name = CharField(max_length=200)
    unit = CharField(max_length=10)
    quant = IntegerField(default=0)
    catg = ForeignKey(Category)
    lastmod = DateTimeField('last modified', auto_now=True)
    def __str__(self):
        return self.name

class Stock(Model):
    stuff = ForeignKey(Stuff)
    quant = IntegerField(default=0)
    time = DateTimeField('entry timestamp', auto_now_add=True)

class Diff(Model):
    stuff = ForeignKey(Stuff)
    quant = IntegerField(default=0)
    time = DateTimeField('entry timestamp', auto_now_add=True)
