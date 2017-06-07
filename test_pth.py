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
from   pth      import get_sp                   as gsp
from   pth      import jo                       as j
from   pth      import ncnp                     as n
from   pth      import rm_sp_lst                as rsl
from   exc      import ExceptionNotAbsolutePath as EX_NAP

P1   = n("/pth1/pth2/pth3")
P1D  = n("/pth1/./pth2")
P2   = n("/pth4/pth5")
P2D  = n("/pth3/../pth4")
PA   = n("/pth1/pth2/pth3/pth4/pth5")
PFSP = n("pth1/pth2/pth3/pth4/pth5/")
PI   = n("/pth1/pth2/pth3/pth4/pth5\\")
PLSP = n("/pth1/pth2/pth3/pth4/pth5/")
PR   = n("./pth1/pth2/pth3/pth4/pth5")

class unit_test(TC):
    def test_chk_abs(self):
        self.assertFalse(ca(PR))
        self.assertTrue(ca(P1))
        self.assertTrue(ca(P1D))
        self.assertTrue(ca(P2))
        self.assertTrue(ca(P2D))
        self.assertTrue(ca(PA))

    def test_chk_s_ap_1(self):
        self.assertFalse(csp1(P1, P2))
        self.assertFalse(csp1(P1, PI))
        self.assertFalse(csp1(PI, P2))
        self.assertTrue(csp1(PA, PA))
        self.assertTrue(csp1(PI, PI))
        with self.assertRaises(EX_NAP): csp1(P1, PR)
        with self.assertRaises(EX_NAP): csp1(PR, P2)
        with self.assertRaises(EX_NAP): csp1(PR, PI)
        with self.assertRaises(EX_NAP): csp1(PR, PR)
        with self.assertRaises(EX_NAP): self.assertFalse(csp1(PI, PR))


    def test_chk_s_ap_x(self):
        self.assertFalse(cspx(P1, P2, 2))
        self.assertFalse(cspx(P1, PI, 2))
        self.assertFalse(cspx(PI, P2, 2))
        self.assertTrue(cspx(P1, P2, 3))
        self.assertTrue(cspx(PA, PA, 2))
        self.assertTrue(cspx(PI, PI, 2))
        with self.assertRaises(EX_NAP): cspx(P1, PR, 2)
        with self.assertRaises(EX_NAP): cspx(PR, P2, 2)
        with self.assertRaises(EX_NAP): cspx(PR, PI, 2)
        with self.assertRaises(EX_NAP): cspx(PR, PR, 2)
        with self.assertRaises(EX_NAP): self.assertFalse(cspx(PI, PR, 2))

    def test_get_ap_1(self):
        self.assertEqual   (gp1(P1) , n("/pth1/pth2"))
        self.assertEqual   (gp1(P1D), n("/pth1"))
        self.assertEqual   (gp1(P1D), n("/pth1/."))
        self.assertEqual   (gp1(P2) , n("/pth4"))
        self.assertEqual   (gp1(P2D), n("/pth1/.."))
        self.assertEqual   (gp1(PA) , n("/pth1/pth2/pth3/pth4"))
        self.assertNotEqual(gp1(P1) , n("/pth1"))
        self.assertNotEqual(gp1(P2) , n("/"))
        self.assertNotEqual(gp1(P2D), n("/pth1"))
        self.assertNotEqual(gp1(PA) , n("/pth1/pth2/pth3"))
        with self.assertRaises(EX_NAP): gp1(PR)

    def test_get_ap_x(self):
        """ Due to `ncnp()`. """
        self.assertEqual   (gpx(P1 , 10), n("/"))
        self.assertEqual   (gpx(P2 , 10), n("/"))
        self.assertEqual   (gpx(P1 , 10), n("/"))
        self.assertEqual   (gpx(P1D, 10), n("/"))
        self.assertEqual   (gpx(P1D, 10), n("/"))
        self.assertEqual   (gpx(P2 , 10), n("/"))
        self.assertEqual   (gpx(P2D, 10), n("/"))
        self.assertEqual   (gpx(P2D, 10), n("/"))
        self.assertEqual   (gpx(PA , 10), n("/"))
        self.assertEqual   (gpx(PA , 10), n("/"))

        self.assertEqual   (gpx(P1 ,  2), n("/pth1"))
        self.assertEqual   (gpx(P2 ,  2), n("/"))
        self.assertEqual   (gpx(PA ,  2), n("/pth1/pth2/pth3"))
        self.assertNotEqual(gpx(P1 ,  2), n("/pth1/pth2"))
        self.assertNotEqual(gpx(P1D,  2), n("/pth1"))
        self.assertNotEqual(gpx(P1D,  2), n("/pth1/"))
        self.assertNotEqual(gpx(P2 ,  2), n("/pth4"))
        self.assertNotEqual(gpx(P2D,  2), n("/pth1"))
        self.assertNotEqual(gpx(P2D,  2), n("/pth1/"))
        self.assertNotEqual(gpx(PA ,  2), n("/pth1/pth2/pth3/pth4"))
        with self.assertRaises(EX_NAP): gpx(PR, 2)

    def test_get_ap_innermst(self):
        self.assertEqual   (gpi(P1) , "pth3")
        self.assertEqual   (gpi(P1D), "pth2")
        self.assertEqual   (gpi(P2) , "pth5")
        self.assertEqual   (gpi(PA) , "pth5")
        self.assertNotEqual(gpi(P1) , "pth4")
        self.assertNotEqual(gpi(P1D), "pth3")
        self.assertNotEqual(gpi(P2) , "pth6")
        self.assertNotEqual(gpi(P2D), "pth2")
        self.assertNotEqual(gpi(P2D), "pth3")
        self.assertNotEqual(gpi(PA) , "pth6")
        with self.assertRaises(EX_NAP): gpi(PR)

    def test_get_sp(self):
        if   p == "darwin" or p == "linux": self.assertEqual(gsp(), "/")
        elif p == "cygwin" or p == "win32": self.assertEqual(gsp(), "\\")

    def test_jo(self):
        self.assertEqual   (j(P1, P2), PA)
        self.assertEqual   (j(P1, PR), j(P1, PR)) # Just to show that this
                                                  # function only needs its
                                                  # first parameter to be an
                                                  # absolute path.
        self.assertNotEqual(j(P1, P2), gp1(PA))
        with self.assertRaises(EX_NAP): j(PR, P2)
        with self.assertRaises(EX_NAP): j(PR, PR)

    def test_ncnp(self):
        if   p == "darwin" or p == "linux":
            self.assertTrue(n(P1D), "/pth1/pth2")
            self.assertTrue(n(P2D), "/pth2")
        elif p == "cygwin" or p == "win32":
            self.assertTrue(n(P1D), "\\pth1\\pth2")
            self.assertTrue(n(P2D), "\\pth2")

    def test_rm_sp_fst(self):
        self.assertTrue(PA, rsl(PFSP))

    def test_rm_sp_lst(self):
        self.assertTrue(rsl(PLSP), PA)


if __name__ == "__main__":
    unittest.main()