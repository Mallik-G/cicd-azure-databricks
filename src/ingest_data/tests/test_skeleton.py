#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from ingest_data.skeleton import fib

__author__ = "Lace Lofranco"
__copyright__ = "Lace Lofranco"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
