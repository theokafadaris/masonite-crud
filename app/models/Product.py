""" Product Model """

from masoniteorm.models import Model


class Product(Model):
    __fillable__ = ['name', 'details']

    
