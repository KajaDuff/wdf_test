from cms.models.pluginmodel import CMSPlugin

from django.db import models

class Person(CMSPlugin):
    firstname = models.CharField(max_length=200, default='Name')
    surname = models.CharField(max_length=200, default = 'Surname')