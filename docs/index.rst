djorm-ext-pgarray
=================

PostgreSQL array field for Django.


Introduction
------------

Django by default, has a large collection of possible types that can be used to define the
model. But sometimes we need to use some more complex types offered by PostgreSQL. In this
case, we will look the integrating of PostgreSQL array with Django.

Quickstart
----------

**djorm-ext-pgarray** exposes a simple django model field `djorm_pgarray.fields.ArrayField`.
This accepts two additional parameters: **dbtype** that represents a postgresql type, and
**dimension** that represents a dimension of array field.

This is a sample definition of model using a ArrayField:

.. code-block:: python

    from django.db import models
    from djorm_pgarray.fields import ArrayField
    from djorm_expressions.models import ExpressionManager

    class Register(models.Model):
        name = models.CharField(max_length=200)
        points = ArrayField(dbtype="int")
        objects = ExpressionManager()

    class Register2(models.Model):
        name = models.CharField(max_length=200)
        texts = ArrayField(dbtype="text", dimension=2) # this creates `points text[][]` postgresql field.
        objects = ExpressionManager()


Creating objects
~~~~~~~~~~~~~~~~

This is a sample example of creating objects with array fields.

.. code-block:: pycon

    >>> Register.objects.create(points = [1,2,3,4])
    <Register: Register object>
    >>> Register2.objects.create(texts = [['Hello', 'World'], ['Hola', 'Mundo']])
    <Register2: Register2 object>


How install it?
---------------

You can clone the repo from github and install with simple python setup.py install
command. Or use a pip, for install it from Python Package Index.

.. code-block:: console

    pip install djorm-ext-pgarray

Additionally, you can install djorm-ext-expressions, that can help with complex queries
using array fields.
