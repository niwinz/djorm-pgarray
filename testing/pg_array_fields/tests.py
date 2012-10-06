# -*- coding: utf-8 -*-

from django.test import TestCase

from djorm_expressions.base import SqlExpression
from .models import IntModel, TextModel, DoubleModel

class ArrayFieldTests(TestCase):
    def setUp(self):
        IntModel.objects.all().delete()
        TextModel.objects.all().delete()
        DoubleModel.objects.all().delete()

    def test_empty_create(self):
        instance = IntModel.objects.create(lista=[])
        instance = IntModel.objects.get(pk=instance.pk)
        self.assertEqual(instance.lista, [])

    def test_overlap(self):
        obj1 = IntModel.objects.create(lista=[1,2,3])
        obj2 = IntModel.objects.create(lista=[2,4,5])
        obj3 = IntModel.objects.create(lista=[5,33,21])

        queryset = IntModel.objects.where(
            SqlExpression("lista", "&&", [1,2,3])
        )
        self.assertEqual(queryset.count(), 2)

        queryset = IntModel.objects.where(
            SqlExpression("lista", "&&", [1,2,3])
        )
        self.assertEqual(queryset.count(), 2)

    def test_contains_unicode(self):
        obj = TextModel.objects\
            .create(lista=[u"Fóö", u"Пример", u"test"])

        queryset = TextModel.objects.where(
            SqlExpression("lista", "@>", [u"Пример"])
        )
        self.assertEqual(queryset.count(), 1)
