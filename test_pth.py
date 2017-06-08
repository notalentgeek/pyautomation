from   sys      import platform                 as p
from   unittest import TestCase                 as TC
import os
import unittest

from   pth      import chk_abs                  as ca
from   pth      import chk_s_ap_1               as csp1
from   pth      import chk_s_ap_x               as cspx
from   pth      import get_ap_1                 as gp1
from   pth      import get_ap_innermst          as gpi
from   pth      import get_ap_x                 as gpx
from   pth      import get_ext                  as ge
from   pth      import get_sp                   as gsp
from   pth      import jo                       as j
from   pth      import ncnp                     as n
from   pth      import rm_sp_lst                as rsl
from   exc      import ExceptionNotAbsolutePath as EX_NAP

ext  = "fi"

p1   = n("/pth1/pth2/pth3")
p1d  = n("/pth1/./pth2")
p2   = n("/pth4/pth5")
p2d  = n("/pth3/../pth4")
pa   = n("/pth1/pth2/pth3/pth4/pth5")
pf   = n("/pth1/pth2/pth3/pth4/pth5/fi.{}".format(ext))
pfsp = n("pth1/pth2/pth3/pth4/pth5/")
pi   = n("/pth1/pth2/pth3/pth4/pth5\\")
pjf  = n("fi.{}".format(ext))
plsp = n("/pth1/pth2/pth3/pth4/pth5/")
pr   = n("./pth1/pth2/pth3/pth4/pth5")

class unit_test(TC):
    def test_chk_abs(self):
        self.assertFalse(ca(pr))
        self.assertTrue(ca(p1))
        self.assertTrue(ca(p1d))
        self.assertTrue(ca(p2))
        self.assertTrue(ca(p2d))
        self.assertTrue(ca(pa))

    def test_chk_s_ap_1(self):
        self.assertFalse(csp1(p1, p2))
        self.assertFalse(csp1(p1, pi))
        self.assertFalse(csp1(pi, p2))
        self.assertTrue(csp1(pa, pa))
        self.assertTrue(csp1(pi, pi))
        with self.assertRaises(EX_NAP): csp1(p1, pr)
        with self.assertRaises(EX_NAP): csp1(pr, p2)
        with self.assertRaises(EX_NAP): csp1(pr, pi)
        with self.assertRaises(EX_NAP): csp1(pr, pr)
        with self.assertRaises(EX_NAP): self.assertFalse(csp1(pi, pr))


    def test_chk_s_ap_x(self):
        self.assertFalse(cspx(p1, p2, 2))
        self.assertFalse(cspx(p1, pi, 2))
        self.assertFalse(cspx(pi, p2, 2))
        self.assertTrue(cspx(p1, p2, 3))
        self.assertTrue(cspx(pa, pa, 2))
        self.assertTrue(cspx(pi, pi, 2))
        with self.assertRaises(EX_NAP): cspx(p1, pr, 2)
        with self.assertRaises(EX_NAP): cspx(pr, p2, 2)
        with self.assertRaises(EX_NAP): cspx(pr, pi, 2)
        with self.assertRaises(EX_NAP): cspx(pr, pr, 2)
        with self.assertRaises(EX_NAP): self.assertFalse(cspx(pi, pr, 2))

    def test_get_ap_1(self):
        self.assertEqual   (gp1(p1) , n("/pth1/pth2"))
        self.assertEqual   (gp1(p1d), n("/pth1"))
        self.assertEqual   (gp1(p1d), n("/pth1/."))
        self.assertEqual   (gp1(p2) , n("/pth4"))
        self.assertEqual   (gp1(p2d), n("/pth1/.."))
        self.assertEqual   (gp1(pa) , n("/pth1/pth2/pth3/pth4"))
        self.assertNotEqual(gp1(p1) , n("/pth1"))
        self.assertNotEqual(gp1(p2) , n("/"))
        self.assertNotEqual(gp1(p2d), n("/pth1"))
        self.assertNotEqual(gp1(pa) , n("/pth1/pth2/pth3"))
        with self.assertRaises(EX_NAP): gp1(pr)

    def test_get_ap_x(self):
        """ Due to `ncnp()`. """
        self.assertEqual   (gpx(p1 , 10), n("/"))
        self.assertEqual   (gpx(p2 , 10), n("/"))
        self.assertEqual   (gpx(p1 , 10), n("/"))
        self.assertEqual   (gpx(p1d, 10), n("/"))
        self.assertEqual   (gpx(p1d, 10), n("/"))
        self.assertEqual   (gpx(p2 , 10), n("/"))
        self.assertEqual   (gpx(p2d, 10), n("/"))
        self.assertEqual   (gpx(p2d, 10), n("/"))
        self.assertEqual   (gpx(pa , 10), n("/"))
        self.assertEqual   (gpx(pa , 10), n("/"))

        self.assertEqual   (gpx(p1 ,  2), n("/pth1"))
        self.assertEqual   (gpx(p2 ,  2), n("/"))
        self.assertEqual   (gpx(pa ,  2), n("/pth1/pth2/pth3"))
        self.assertNotEqual(gpx(p1 ,  2), n("/pth1/pth2"))
        self.assertNotEqual(gpx(p1d,  2), n("/pth1"))
        self.assertNotEqual(gpx(p1d,  2), n("/pth1/"))
        self.assertNotEqual(gpx(p2 ,  2), n("/pth4"))
        self.assertNotEqual(gpx(p2d,  2), n("/pth1"))
        self.assertNotEqual(gpx(p2d,  2), n("/pth1/"))
        self.assertNotEqual(gpx(pa ,  2), n("/pth1/pth2/pth3/pth4"))
        with self.assertRaises(EX_NAP): gpx(pr, 2)

    def test_get_ap_innermst(self):
        self.assertEqual   (gpi(p1) , "pth3")
        self.assertEqual   (gpi(p1d), "pth2")
        self.assertEqual   (gpi(p2) , "pth5")
        self.assertEqual   (gpi(pa) , "pth5")
        self.assertNotEqual(gpi(p1) , "pth4")
        self.assertNotEqual(gpi(p1d), "pth3")
        self.assertNotEqual(gpi(p2) , "pth6")
        self.assertNotEqual(gpi(p2d), "pth2")
        self.assertNotEqual(gpi(p2d), "pth3")
        self.assertNotEqual(gpi(pa) , "pth6")
        with self.assertRaises(EX_NAP): gpi(pr)

    def test_get_ext(self):
        self.assertEqual(ge(pa), "")
        self.assertEqual(ge(pf), ext)
        self.assertEqual(ge(pjf), ext)

    def test_get_sp(self):
        if   p == "darwin" or p == "linux": self.assertEqual(gsp(), "/")
        elif p == "cygwin" or p == "win32": self.assertEqual(gsp(), "\\")

    def test_jo(self):
        self.assertEqual   (j(p1, p2), pa)
        self.assertEqual   (j(p1, pr), j(p1, pr)) # Just to show that this
                                                  # function only needs its
                                                  # first parameter to be an
                                                  # absolute path.
        self.assertNotEqual(j(p1, p2), gp1(pa))
        with self.assertRaises(EX_NAP): j(pr, p2)
        with self.assertRaises(EX_NAP): j(pr, pr)

    def test_ncnp(self):
        if   p == "darwin" or p == "linux":
            self.assertTrue(n(p1d), "/pth1/pth2")
            self.assertTrue(n(p2d), "/pth2")
        elif p == "cygwin" or p == "win32":
            self.assertTrue(n(p1d), "\\pth1\\pth2")
            self.assertTrue(n(p2d), "\\pth2")

    def test_rm_sp_fst(self):
        self.assertTrue(pa, rsl(pfsp))

    def test_rm_sp_lst(self):
        self.assertTrue(rsl(plsp), pa)

if __name__ == "__main__": unittest.main()