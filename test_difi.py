from sys import platform as p
from unittest import TestCase as TC
import getpass
import unittest
import warnings

from dbg import print_ut as put
from difi import chk_exst as ce
from difi import chk_exst_di as ced
from difi import chk_exst_dnd as cd
from difi import chk_exst_fi as cef
from difi import cpy as c
from difi import crt as cr
from difi import de
from difi import frmt_mkdocs as fm
from difi import get_lst as gl
from difi import mov as m
from difi import ren as r
from difi import ren_recr as rr
from difi import wlk_get_note as wgn
from pth import get_ap_innermst as gpi
from pth import jo as j
from pth import ncnp as n
from exc import ExceptionExistsDirectoryOrFile as EX_DF
from exc import ExceptionNotAbsolutePath as EX_NAP
from exc import ExceptionNotExistsDirectory as EX_ND
from exc import ExceptionNotExistsDirectoryOrFile as EX_NDF
from exc import ExceptionSamePath as EX_SP

du = n("/home/{}".format(getpass.getuser()))
dw = n("C:\\{}\\Documents and Settings\\My Documents".format(getpass.getuser()))
d = du # Unix platform.
if p == "cygwin" or p == "win32": d = dw # Windows platform.

dm = j(d, "dm_test_difi") # Main directory for this unit test.

dc = j(dm, "dc") # Copied test directory that is exists.
dd = j(dm, "dd") # Deleted test directory that is exists.
dex = j(dm, "dex") # Test directory that is exists.
dmv1 = j(dm, "dmv1") # Moved test directory 1 that is exists.
dmv2 = j(dm, "dmv2") # Moved test directory 2 that is exists.
fc = j(dm, "fc.f") # Copied test file that is exists.
fd = j(dm, "fd.f") # Deleted test file that is exists.
fe = j(dm, "fe.f") # Test file that is exists.
fmv1 = j(dm, "fmv1.f") # Moved test file 1 that is exists.
fmv2 = j(dm, "fmv2.f") # Moved test file 2 that is exists.
fr1 = j(dm, "fr1.f") # Renamed test file 1 that is exists.
fr2 = j(dm, "fr2.f") # Renamed test file 2 that is exists.

e = [dm, dc, dd, dex, dmv1, dmv2, fc, fd, fe, fmv1, fmv2, fr1, fr2]
edf = [dm, dc, dd, dex, dmv1, dmv2]
ed = [dc, dd, dex, dmv1, dmv2]
ef = [fc, fd, fe, fmv1, fmv2, fr1, fr2]
edef = [dc, dd, dex, dmv1, dmv2, fc, fd, fe, fmv1, fmv2, fr1, fr2]

dne = j(dm, "dne") # Test directory that is not exists.
dni = j(dm, "di\\") # Illegal directory that is not exists.
dnr = n("./") # Relative directory that is not exists.
fne = j(dm, "fne.f") # Test file that is not exists.
fni = j(dm, "f.f\\") # Illegal file that is not exists.
fnr = n("./f.f") # Relative file that is not exists.

dren = "dren" # New name for directory (used in rename operation).
fren = "fren" # New name for file (used in rename operation).

ne = [dne, dni, fne, fni]
ne_exc = [dnr, fnr]

class unit_test(TC):
    def setUp(self):
        for i in edf: cr(i, True)
        for i in ef: cr(i, False)

    def tearDown(self): de(dm)

    def test_chk_exst(self):
        for i in e: self.assertTrue(ce(i))
        for i in ne: self.assertFalse(ce(i))
        with self.assertRaises(EX_NAP):
            for i in ne_exc: ce(i)

    def test_chk_exst_di(self):
        for i in edf: self.assertTrue(ced(i))
        for i in ef: self.assertFalse(ced(i))
        for i in ne: self.assertFalse(ced(i))
        with self.assertRaises(EX_NAP):
            for i in ne_exc: ced(i)

    def test_chk_exst_dnd(self):
        for i in ed: self.assertFalse(cd(i))
        for i in ef:
            with self.assertRaises(EX_ND): cd(i)
        self.assertTrue(cd(dm))
        with self.assertRaises(EX_NAP): cd(dnr)

    def test_chk_exst_fi(self):
        for i in edf: self.assertFalse(cef(i))
        for i in ef: self.assertTrue(cef(i))
        for i in ne: self.assertFalse(cef(i))
        with self.assertRaises(EX_NAP):
            for i in ne_exc: cef(i)

    def test_cpy(self):
        """ Delete the copy directory and file. """
        de(dc); de(fc);
        self.assertTrue(c(dex, dc))
        self.assertTrue(c(dex, dc)) # Old directory is replaced.
        self.assertTrue(c(fe, fc))
        self.assertTrue(c(fe, fc)) # Old file is replaced.
        self.assertFalse(c(dex, dc, False)) # Old directory is not replaced.
        self.assertFalse(c(fe, fc, False)) # Old file is not replaced.
        with self.assertRaises(EX_NAP): c(dne, dnr)
        with self.assertRaises(EX_NAP): c(dnr, dne)
        with self.assertRaises(EX_NAP): c(dnr, dnr)
        with self.assertRaises(EX_NAP): c(fne, fnr)
        with self.assertRaises(EX_NAP): c(fnr, fne)
        with self.assertRaises(EX_NAP): c(fnr, fnr)
        with self.assertRaises(EX_NDF): c(dne, dc)
        with self.assertRaises(EX_SP): c(dex, dex)

    def test_crt(self):
        de(dm) # Need to tear down the environment because this test meant to set up the environment.
        for i in edf: self.assertTrue(cr(i, True))
        for i in ef: self.assertTrue(cr(i, False))
        for i in edf:
            self.assertFalse(cr(i, True))
        for i in ef:
            self.assertFalse(cr(i, False))
        with self.assertRaises(EX_NAP): cr(dnr, True)
        with self.assertRaises(EX_NAP): cr(fnr, False)

    def test_de(self):
        for i in ed: self.assertTrue(de(i))
        for i in ef: self.assertTrue(de(i))
        for i in ed: self.assertFalse(de(i))
        for i in ef: self.assertFalse(de(i))
        self.assertTrue(de(dm))
        with self.assertRaises(EX_NAP): de(dnr)
        with self.assertRaises(EX_NAP): de(fnr)

    def test_frmt_mkdocs(self): put("fm(...)", "PENDING: not yet unit tested")

    def test_get_lst(self):
        for i in edef: self.assertTrue(gpi(i) in gl(dm))
        with self.assertRaises(EX_NAP): gl(dnr)

    def test_mov(self):
        de(dmv2); de(fmv2); # Delete the move directory 2 and move file 2.
        self.assertTrue(m(dmv1, dmv2)); cr(dmv1, True); # Re - create move directory 1.
        self.assertTrue(m(dmv1, dmv2)); cr(dmv1, True); # Re - create move directory 1 and move directory 1 is replaced.
        self.assertTrue(m(fmv1, fmv2)); cr(fmv1, False); # Re - create move file 1.
        self.assertTrue(m(fmv1, fmv2)); cr(fmv1, False); # Re - create move file 1 and move file 1 is replaced.
        self.assertFalse(m(dmv1, dmv2, False)) # Old move directory 1 is not replaced.
        self.assertFalse(m(fmv1, fmv2, False)) # Old move file 1 is not replaced.
        with self.assertRaises(EX_NAP): m(dne, dnr)
        with self.assertRaises(EX_NAP): m(dnr, dne)
        with self.assertRaises(EX_NAP): m(fne, fnr)
        with self.assertRaises(EX_NAP): m(fnr, fne)
        with self.assertRaises(EX_SP): m(dex, dex)
        de(dmv1); de(fmv1); # Delete the move directory 1 and move file 1
        with self.assertRaises(EX_NDF): m(dmv1, dmv2)
        with self.assertRaises(EX_NDF): m(fmv1, fmv2)

    def test_ren(self):
        self.assertTrue(r(dex, dren))
        self.assertTrue(r(fe, fren))
        cr(dex, True); cr(fe, False); # Re - create.
        self.assertTrue(r(dex, dren)) # Replace.
        self.assertTrue(r(fe, fren)) # Replace.
        cr(dex, True); cr(fe, False); # Re - create.
        with self.assertRaises(EX_NAP): r(dnr, dren)
        with self.assertRaises(EX_NAP): r(fnr, fren)
        with self.assertRaises(EX_NDF): r(dne, dren)
        with self.assertRaises(EX_NDF): r(fne, fren)

    def test_ren_recr(self): put("rr(...)", "PENDING: not yet unit tested")

    def test_wlk_get_note(self):
        dw = j(dm, "dw"); cr(dw, True);
        d1 = j(dw, "d1"); cr(d1, True);
        d2 = j(dw, "d2"); cr(d2, True);
        d3 = j(dw, "d3"); cr(d3, True);
        d4 = j(dw, "d4"); cr(d4, True);
        d5 = j(dw, "d5"); cr(d5, True);
        f1_1 = j(d1, "f1_1.f"); cr(f1_1, False);
        f1_2 = j(d1, "f1_2.f"); cr(f1_2, False);
        f2_1 = j(d2, "f2_1.f"); cr(f2_1, False);
        f2_2 = j(d2, "f2_2.f"); cr(f2_2, False);
        f3_1 = j(d3, "f3_1.f"); cr(f3_1, False);
        f3_2 = j(d3, "f3_2.f"); cr(f3_2, False);
        f4_1 = j(d4, "f4_1.f"); cr(f4_1, False);
        f4_2 = j(d4, "f4_2.f"); cr(f4_2, False);
        f5_1 = j(d5, "f5_1.f"); cr(f5_1, False);
        f5_2 = j(d5, "f5_2.f"); cr(f5_2, False);
        #put("wgn(\"C:\\Users\\mikael\\Downloads\\notalentgeek-wiki\")", wgn("C:\\Users\\mikael\\Downloads\\notalentgeek-wiki"))

if __name__ == "__main__": unittest.main()