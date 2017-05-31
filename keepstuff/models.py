from django.db.models import *
import django_tables2 as tables

class Category(Model):
    name = CharField(max_length=200)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name


class Stuff(Model):
    name = CharField(max_length=200)
    unit = CharField(max_length=10, blank=True)
    quant = IntegerField(default=0)
    catg = ForeignKey(Category)
    lastmod = DateTimeField('last modified', auto_now=True)
    @property
    def howmuch(self):
        return '{} {}'.format(self.quant, self.unit)
    class Meta:
        ordering = ["catg", "-quant"]
    def __str__(self):
        return self.name

class Entry(Model):
    stuff = ForeignKey(Stuff)
    quant = IntegerField(default=0)
    isabs = BooleanField(default=False)
    time = DateTimeField('entry timestamp', auto_now_add=True)

    class Meta:
        ordering = ["-time"]
    def __str__(self):
        return "%s, %s %s, %s"%(self.stuff.name, self.quant, 'abs' if self.isabs else '', self.time)


class StuffTable(tables.Table):
    howmuch = tables.Column(order_by=('quant',))
    class Meta:
        model = Stuff
        fields = ('catg','name','howmuch')
        sequence = ('catg','name','howmuch')
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}


