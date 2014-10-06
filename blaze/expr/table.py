""" An abstract Table

>>> accounts = TableSymbol('accounts', '{name: string, amount: int}')
>>> deadbeats = accounts['name'][accounts['amount'] < 0]
"""
from __future__ import absolute_import, division, print_function

from datashape import dshape, DataShape, Record, isdimension, Option
from datashape import coretypes as ct
import datashape
import toolz
from toolz import (concat, partial, first, compose, get, unique, second,
                   isdistinct, frequencies, memoize)
from datashape.predicates import isscalar, iscollection
import numpy as np
from .core import *
from .expressions import *
from .collections import *
from .reductions import *
from .split_apply_combine import *
from .broadcast import broadcast, Broadcast
from ..compatibility import _strtypes, builtins, unicode, basestring, map, zip
from ..dispatch import dispatch


from .broadcast import _expr_child

__all__ = '''TableSymbol Apply'''.split()


def TableSymbol(name, dshape):
    """ A Symbol for Tabular data

    This is a leaf in the expression tree

    Examples
    --------

    >>> accounts = TableSymbol('accounts',
    ...                        '{name: string, amount: int, id: int}')
    >>> accounts['amount'] + 1
    accounts['amount'] + 1

    We define a TableSymbol with a name like ``accounts`` and the datashape of
    a single row, called a schema.
    """
    if isinstance(dshape, _strtypes):
        dshape = datashape.dshape(dshape)
    if not iscollection(dshape):
        dshape = datashape.var * dshape
    return Symbol(name, dshape)


class Apply(Expr):
    """ Apply an arbitrary Python function onto a Table

    Examples
    --------

    >>> t = TableSymbol('t', '{name: string, amount: int}')
    >>> h = Apply(hash, t)  # Hash value of resultant table

    Optionally provide extra datashape information

    >>> h = Apply(hash, t, dshape='real')

    Apply brings a function within the expression tree.
    The following transformation is often valid

    Before ``compute(Apply(f, expr), ...)``
    After  ``f(compute(expr, ...)``

    See Also
    --------

    blaze.expr.expressions.Map
    """
    __slots__ = '_child', 'func', '_dshape'

    def __init__(self, func, child, dshape=None):
        self._child = child
        self.func = func
        self._dshape = dshape

    @property
    def schema(self):
        if iscollection(self.dshape):
            return self.dshape.subshape[0]
        else:
            raise TypeError("Non-tabular datashape, %s" % self.dshape)

    @property
    def dshape(self):
        if self._dshape:
            return dshape(self._dshape)
        else:
            raise NotImplementedError("Datashape of arbitrary Apply not defined")
