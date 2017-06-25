from unittest import TestCase as TC
import unittest

from dbg import crt_img_dbg as cid
from dbg import print_lst as pl
from dbg import print_ut as put

class unit_test(TC):
    def crt_img_dbg(self): put("cid(...)", "PENDING: not yet unit tested")

    def print_lst(self): put("pl(...)", "PENDING: not yet unit tested")

    def print_ut(self): put("put(...)", "PENDING: not yet unit tested")