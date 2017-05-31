# BrewInventory
A quite basic Django app for keeping my homebrewing inventory.

It keeps track of "stuff" through absolute or relative "entries"
that it uses to update the stock.

Views are the log of entries and a sortable table with the help
of django_tables2. Data entry is done with Django's admin interface
only.

(Yes, the database is included in this respository, containing log-in
information. Don't bother trying to use it, this app is not hosted
publicly.)
