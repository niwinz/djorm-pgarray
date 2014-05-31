# -*- coding: utf-8 -*-

from django.db import models
from djorm_pgarray.fields import ArrayField
from djorm_pgarray.fields import TextArrayField
from djorm_pgarray.fields import FloatArrayField
from djorm_pgarray.fields import IntegerArrayField
from djorm_pgarray.fields import DateArrayField
from djorm_pgarray.fields import DateTimeArrayField
from djorm_pgarray.fields import SmallIntegerArrayField


class Item(models.Model):
    tags = TextArrayField(default=lambda: [])


class Item2(models.Model):
    tags = TextArrayField(default=[])


class IntModel(models.Model):
    lista = IntegerArrayField()


class TextModel(models.Model):
    lista = TextArrayField()


class MacAddrModel(models.Model):
    lista = ArrayField(dbtype="macaddr", type_cast=str)


class DoubleModel(models.Model):
    lista = FloatArrayField()


class MTextModel(models.Model):
    data = TextArrayField(dimension=2)


class MultiTypeModel(models.Model):
    smallints = SmallIntegerArrayField()
    varchars = ArrayField(dbtype="varchar(30)")


class DateModel(models.Model):
    dates = DateArrayField()


class DateTimeModel(models.Model):
    dates = DateTimeArrayField()


class ChoicesModel(models.Model):
    choices = TextArrayField(choices=[("A", "A"), ("B", "B")])
