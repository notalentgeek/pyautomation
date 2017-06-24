from sys import platform as p
from unittest import TestCase as TC
import os
import unittest

from dbg import print_ut as put
from pth import chk_ap as ca
from pth import chk_ext_img as cei
from pth import chk_s_ap_1 as csp1
from pth import chk_s_ap_x as cspx
from pth import get_ap_1 as gp1
from pth import get_ap_innermst as gpi
from pth import get_ap_x as gpx
from pth import get_ext as ge
from pth import get_no_ext as gne
from pth import get_sp as gsp
from pth import rm_ext as re
from pth import rm_ext_bak as reb
from pth import rm_ext_md as rem
from pth import jo as j
from pth import ncnp as n
from pth import rm_sp_lst as rsl
from exc import ExceptionNotAbsolutePath as EX_NAP
from exc import ExceptionNotExistsFileExtension as EX_NFE

pa = n("/pth1/pth2/pth3/pth4/pth5") # Absolute path.
pa1 = n("/pth1/pth2/pth3") # Absolute path first part for unit testing join function.
pa2 = n("/pth4/pth5") # Absolute path second part for unit testing join function.
pafl = n("/pth1/pth2/pth3/pth4/pth5/fi.fi") # Longer absolute path to file.
pafs = n("fi.fi") # Shorter absolute path to file.
pas = n("/pth1/pth2/pth3/pth4/pth5/") # Absolute path with system separator as a latest character.
paw1 = n("/pth1/./pth2") # Absolute path with single dot to shorten URL for unit testing URL normalizer function.
paw2 = n("/pth1/../pth2") # Absolute path with double dots to shorten URL for unit testing URL normalizer function.
pi = n("/pth1/pth2/pth3/pth4/pth5\\") # Illegal path.
pr = n("pth1/pth2/pth3/pth4/pth5") # Relative path.
prd = n("./pth1/pth2/pth3/pth4/pth5") # Relative path with singe dot.

class unit_test(TC):
    def test_chk_ap(self):
        self.assertFalse(ca(prd))
        self.assertTrue(ca(pa))
        self.assertTrue(ca(pa1))
        self.assertTrue(ca(pa2))
        self.assertTrue(ca(paw1))
        self.assertTrue(ca(paw2))

    def test_chk_ext_img(self):
        self.assertFalse(cei("fi.fi"))
        self.assertTrue(cei("fi.bmp"))
        self.assertTrue(cei("fi.jpeg"))
        self.assertTrue(cei("fi.jpg"))
        self.assertTrue(cei("fi.png"))

        with self.assertRaises(EX_NFE): cei("fi")

    def test_chk_s_ap_1(self):
        self.assertFalse(csp1(pa1, pa2))
        self.assertFalse(csp1(pa1, pi))
        self.assertFalse(csp1(pi, pa2))
        self.assertTrue(csp1(pa, pa))
        self.assertTrue(csp1(pi, pi))

        with self.assertRaises(EX_NAP): csp1(pa1, prd)
        with self.assertRaises(EX_NAP): csp1(prd, pa2)
        with self.assertRaises(EX_NAP): csp1(prd, pi)
        with self.assertRaises(EX_NAP): csp1(prd, prd)
        with self.assertRaises(EX_NAP): self.assertFalse(csp1(pi, prd))

    def test_chk_s_ap_x(self):
        self.assertFalse(cspx(pa1, pa2, 2))
        self.assertFalse(cspx(pa1, pi, 2))
        self.assertFalse(cspx(pi, pa2, 2))
        self.assertTrue(cspx(pa, pa, 2))
        self.assertTrue(cspx(pa1, pa2, 3))
        self.assertTrue(cspx(pi, pi, 2))

        with self.assertRaises(EX_NAP): cspx(pa1, prd, 2)
        with self.assertRaises(EX_NAP): cspx(prd, pa2, 2)
        with self.assertRaises(EX_NAP): cspx(prd, pi, 2)
        with self.assertRaises(EX_NAP): cspx(prd, prd, 2)
        with self.assertRaises(EX_NAP): self.assertFalse(cspx(pi, prd, 2))

    def test_get_ap_1(self):
        self.assertEqual(gp1(pa), n("/pth1/pth2/pth3/pth4"))
        self.assertEqual(gp1(pa1), n("/pth1/pth2"))
        self.assertEqual(gp1(pa2), n("/pth4"))
        self.assertEqual(gp1(paw1), n("/pth1"))
        self.assertEqual(gp1(paw1), n("/pth1/."))
        self.assertEqual(gp1(paw2), n("/pth1/.."))
        self.assertNotEqual(gp1(pa), n("/pth1/pth2/pth3"))
        self.assertNotEqual(gp1(pa1), n("/pth1"))
        self.assertNotEqual(gp1(pa2), n("/"))
        self.assertNotEqual(gp1(paw2), n("/pth1"))

        with self.assertRaises(EX_NAP): gp1(prd)

    def test_get_ap_x(self):
        """ Due to `ncnp()`. """
        self.assertEqual(gpx(pa, 10), n("/"))
        self.assertEqual(gpx(pa, 10), n("/"))
        self.assertEqual(gpx(pa1, 10), n("/"))
        self.assertEqual(gpx(pa1, 10), n("/"))
        self.assertEqual(gpx(pa2, 10), n("/"))
        self.assertEqual(gpx(pa2, 10), n("/"))
        self.assertEqual(gpx(paw1, 10), n("/"))
        self.assertEqual(gpx(paw1, 10), n("/"))
        self.assertEqual(gpx(paw2, 10), n("/"))
        self.assertEqual(gpx(paw2, 10), n("/"))

        self.assertEqual(gpx(pa, 2), n("/pth1/pth2/pth3"))
        self.assertEqual(gpx(pa1, 2), n("/pth1"))
        self.assertEqual(gpx(pa2, 2), n("/"))
        self.assertNotEqual(gpx(pa, 2), n("/pth1/pth2/pth3/pth4"))
        self.assertNotEqual(gpx(pa1, 2), n("/pth1/pth2"))
        self.assertNotEqual(gpx(pa2, 2), n("/pth4"))
        self.assertNotEqual(gpx(paw1, 2), n("/pth1"))
        self.assertNotEqual(gpx(paw1, 2), n("/pth1/"))
        self.assertNotEqual(gpx(paw2, 2), n("/pth1"))
        self.assertNotEqual(gpx(paw2, 2), n("/pth1/"))

        with self.assertRaises(EX_NAP): gpx(prd, 2)

    def test_get_ap_innermst(self):
        self.assertEqual(gpi(pa), "pth5")
        self.assertEqual(gpi(pa1), "pth3")
        self.assertEqual(gpi(pa2), "pth5")
        self.assertEqual(gpi(paw1), "pth2")
        self.assertNotEqual(gpi(pa), "pth6")
        self.assertNotEqual(gpi(pa1), "pth4")
        self.assertNotEqual(gpi(pa2), "pth6")
        self.assertNotEqual(gpi(paw1), "pth3")
        self.assertNotEqual(gpi(paw2), "pth3")
        self.assertNotEqual(gpi(paw2), "pth3")

        with self.assertRaises(EX_NAP): gpi(prd)

    def test_get_ext(self):
        self.assertEqual(ge(pa), "")
        self.assertEqual(ge(pafl), "fi")
        self.assertEqual(ge(pafs), "fi")

    def test_get_no_ext(self):
        self.assertEqual(gne(pafl), n("/pth1/pth2/pth3/pth4/pth5/fi"))
        self.assertEqual(gne(pafs), "fi")

    def test_get_sp(self):
        if p == "darwin" or p == "linux": self.assertEqual(gsp(), "/")
        elif p == "cygwin" or p == "win32": self.assertEqual(gsp(), "\\")

    def test_jo(self):
        self.assertEqual(j(pa1, pa2), pa)
        self.assertEqual(j(pa1, prd), j(pa1, prd)) # Just to show that this function only needs its first parameter to be an absolute path.
        self.assertNotEqual(j(pa1, pa2), gp1(pa))

        with self.assertRaises(EX_NAP): j(prd, pa2)
        with self.assertRaises(EX_NAP): j(prd, prd)

    def test_ncnp(self):
        if p == "darwin" or p == "linux":
            self.assertTrue(n(paw1), "/pth1/pth2")
            self.assertTrue(n(paw2), "/pth2")
        elif p == "cygwin" or p == "win32":
            self.assertTrue(n(paw1), "\\pth1\\pth2")
            self.assertTrue(n(paw2), "\\pth2")

    def test_rm_ext(self): put("re(...)", "PENDING: not yet unit tested")

    def test_rm_ext_md(self): put("reb(...)", "PENDING: not yet unit tested")

    def test_rm_ext_bak(self): put("rem(...)", "PENDING: not yet unit tested")


    def test_rm_sp_fst(self):
        self.assertTrue(pa, rsl(pr))

    def test_rm_sp_lst(self):
        self.assertTrue(rsl(pas), pa)

if __name__ == "__main__": unittest.main()