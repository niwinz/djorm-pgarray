# -*- coding: utf-8 -*-

from django.db import models
from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager


class IntModel(models.Model):
     lista = ArrayField(dbtype='int')
     objects = ExpressionManager()


class TextModel(models.Model):
    lista = ArrayField(dbtype='text')
    objects = ExpressionManager()


class DoubleModel(models.Model):
    lista = ArrayField(dbtype='double precision')
    objects = ExpressionManager()
