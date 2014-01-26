# -*- coding: utf-8 -*-

from django.db import models
from djorm_pgarray.fields import ArrayField

class Item(models.Model):
    tags = ArrayField(dbtype="text", default=lambda: [])

class Item2(models.Model):
    tags = ArrayField(dbtype="text", default=[])

class IntModel(models.Model):
    lista = ArrayField(dbtype='int')

class TextModel(models.Model):
    lista = ArrayField(dbtype='text')

class MacAddrModel(models.Model):
    lista = ArrayField(dbtype='macaddr', type_cast=str)

class DoubleModel(models.Model):
    lista = ArrayField(dbtype='double precision')

class MTextModel(models.Model):
    data = ArrayField(dbtype="text", dimension=2)

class MultiTypeModel(models.Model):
    smallints = ArrayField(dbtype="smallint")
    varchars = ArrayField(dbtype="varchar(30)")

class DateModel(models.Model):
    dates = ArrayField(dbtype="date")

class DateTimeModel(models.Model):
    dates = ArrayField(dbtype="timestamp")

class ChoicesModel(models.Model):
    choices = ArrayField(dbtype='text', choices=[('A', 'A'), ('B', 'B')])
