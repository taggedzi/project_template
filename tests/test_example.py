#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
import sys
from src.example.example import Example


def test_double_none():
    with pytest.raises(TypeError):
        ex = Example(None)
        assert ex.double == 5


def test_double_string():
    ex = Example("a")
    assert ex.double == "aa"


def test_double_float():
    ex = Example(7.2)
    assert ex.double == 14.4


def test_double_int():
    ex = Example(6)
    assert ex.double == 12

