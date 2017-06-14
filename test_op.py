""" Unit test for `op.py`. """

from unittest import TestCase as TC
import unittest

from dbg import print_ut as put
from op import add_0_x as a0
from op import chk_limit_strint as clsi
from op import sort_lst as srt

class unit_test(TC):
    def test_add_0_x(self): put("add_0_x(\"1\", 3)", a0("1", 3))
    def test_sort_lst(self): put("sort_lst([\"bravo\", \"alpha\", \"charlie\"])", srt(["bravo", "alpha", "charlie"]))

    def test_chk_limit_strint(self):
        self.assertFalse(clsi("!@#", 0, 1))
        self.assertTrue(clsi("01", 0, 1))
        self.assertTrue(clsi("1", 0, 1))
        self.assertTrue(clsi(1, 0, 1))

if __name__ == "__main__": unittest.main()