# -*- coding: utf-8 -*-

from django.db import models
from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager
from djorm_expressions.base import SqlExpression


class ArrayExpression(object):
    def __init__(self, field):
        self.field = field

    def contains(self, value):
        return SqlExpression(self.field, "@>", value)

    def overlap(self, value):
        return SqlExpression(self.field, "&&", value)


class Item(models.Model):
    tags = ArrayField(dbtype="text")
    objects = ExpressionManager()


class IntModel(models.Model):
    lista = ArrayField(dbtype='int')
    objects = ExpressionManager()


class TextModel(models.Model):
    lista = ArrayField(dbtype='text')
    objects = ExpressionManager()


class MacAddrModel(models.Model):
    lista = ArrayField(dbtype='macaddr', type_cast=str)
    objects = ExpressionManager()


class DoubleModel(models.Model):
    lista = ArrayField(dbtype='double precision')
    objects = ExpressionManager()


class MTextModel(models.Model):
    data = ArrayField(dbtype="text", dimension=2)
    objects = ExpressionManager()


class MultiTypeModel(models.Model):
    smallints = ArrayField(dbtype="smallint")
    varchars = ArrayField(dbtype="varchar(30)")
    objects = ExpressionManager()


class ChoicesModel(models.Model):
    choices = ArrayField(dbtype='text', choices=[('A', 'A'), ('B', 'B')])
