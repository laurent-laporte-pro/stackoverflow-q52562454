# coding: utf-8
from unittest import TestCase

from package_1.module_1 import f


class TestF(TestCase):
    def test_f(self):
        assert f() == "I'm f()"
