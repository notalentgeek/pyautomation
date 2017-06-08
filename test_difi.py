from   sys      import platform                 as p
from   unittest import TestCase                 as TC
import getpass
import unittest
import warnings

from   difi     import chk_exst                 as ce
from   difi     import chk_exst_di              as ced
from   difi     import chk_exst_fi              as cef
from   difi     import cpy                      as c
from   difi     import crt                      as cr
from   difi     import de                       as dele
from   difi     import mov                      as m
from   difi     import ren                      as r
from   pth      import jo                       as j
from   pth      import ncnp                     as n
from   exc      import ExceptionNotAbsolutePath as EXC_NAP
from   exc      import ExceptionSamePath        as EXC_SP
from   wrn      import WarningExists            as W_E
from   wrn      import WarningNotExists         as W_NE

du = n("/home/{}".format(getpass.getuser()))
dw = n("C:\\{}\\Documents and Settings\\My Documents".format(getpass.getuser()))
d  = du                                  # Unix    platform.
if p == "cygwin" or p == "win32": d = dw # Windows platform.

dm     = j(d, "dm_test_difi") # Main directory for this unit test.

dc     = j(dm, "dc")          # Copied test directory that is exists.
dd     = j(dm, "dd")          # Deleted test directory that is exists.
de     = j(dm, "de")          # Test directory that is exists.
dmv1   = j(dm, "dmv1")        # Moved test directory 1 that is exists.
dmv2   = j(dm, "dmv2")        # Moved test directory 2 that is exists.
dr1    = j(dm, "dr1")         # Renamed test directory 1 that is exists.
dr2    = j(dm, "dr2")         # Renamed test directory 2 that is exists.
fc     = j(dm, "fc.fi")       # Copied test file that is exists.
fd     = j(dm, "fd.fi")       # Deleted test file that is exists.
fe     = j(dm, "fe.fi")       # Test file that is exists.
fmv1   = j(dm, "fmv1.fi")     # Moved test file 1 that is exists.
fmv2   = j(dm, "fmv2.fi")     # Moved test file 2 that is exists.
fr1    = j(dm, "fr1.fi")      # Renamed test file 1 that is exists.
fr2    = j(dm, "fr2.fi")      # Renamed test file 2 that is exists.

e      = [dm, dc, dd, de, dmv1, dmv2, dr1, dr2, fc, fd, fe, fmv1, fmv2, fr1, fr2]
edf    = [dm, dc, dd, de, dmv1, dmv2, dr1, dr2]
ed     = [dc, dd, de, dmv1, dmv2, dr1, dr2]
ef     = [fc, fd, fe, fmv1, fmv2, fr1, fr2]

dne    = j(dm, "dne")         # Test directory that is not exists.
dni    = j(dm, "di\\")        # Illegal directory that is not exists.
dnr    = n("./")              # Relative directory that is not exists.
dren   = "dren"
fne    = j(dm, "fne.fi")      # Test file that is not exists.
fni    = j(dm, "fi.fi\\")     # Illegal file that is not exists.
fnr    = n("./fi.fi")         # Relative file that is not exists.
fren   = "fren"

ne     = [dne, dni, fne, fni]
ne_exc = [dnr, fnr]

def su():
    for i in edf: cr(i, True)
    for i in ef : cr(i, False)
def td(): dele(dm)

class unit_test(TC):
    def setUp(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            su()
    def tearDown(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            td()

    def test_chk_exst(self):
        for i in e : self.assertTrue(ce(i))
        for i in ne: self.assertFalse(ce(i))
        with self.assertRaises(EXC_NAP):
            for i in ne_exc: ce(i)

    def test_chk_exst_di(self):
        for i in edf: self.assertTrue(ced(i))
        for i in ef: self.assertFalse(ced(i))
        for i in ne: self.assertFalse(ced(i))
        with self.assertRaises(EXC_NAP):
            for i in ne_exc: ced(i)

    def test_chk_exst_fi(self):
        for i in edf: self.assertFalse(cef(i))
        for i in ef: self.assertTrue(cef(i))
        for i in ne: self.assertFalse(cef(i))
        with self.assertRaises(EXC_NAP):
            for i in ne_exc: cef(i)

    def test_cpy(self):
        """ Delete the copy directory and file. """
        dele(dc); dele(fc);
        self.assertTrue(c(de, dc))
        self.assertTrue(c(de, dc)) # Old directory is replaced.
        self.assertTrue(c(fe, fc))
        self.assertTrue(c(fe, fc)) # Old file is replaced.
        with self.assertRaises(EXC_NAP): c(dne, dnr)
        with self.assertRaises(EXC_NAP): c(dnr, dne)
        with self.assertRaises(EXC_NAP): c(dnr, dnr)
        with self.assertRaises(EXC_NAP): c(fne, fnr)
        with self.assertRaises(EXC_NAP): c(fnr, fne)
        with self.assertRaises(EXC_NAP): c(fnr, fnr)
        with self.assertRaises(EXC_SP) : c(de, de)
        with self.assertWarns(W_E)     : self.assertFalse(c(de , dc, False)) # Old directory is not replaced.
        with self.assertWarns(W_E)     : self.assertFalse(c(fe , fc, False)) # Old file      is not replaced.
        with self.assertWarns(W_NE)    : self.assertFalse(c(dne, dc))

    def test_crt(self):
        td() # Need to tear down the environment because
             # this test meant to set up the environment.
        for i in edf: self.assertTrue(cr(i, True))
        for i in ef : self.assertTrue(cr(i, False))
        for i in edf:
            with self.assertWarns(W_E): self.assertFalse(cr(i, True))
        for i in ef :
            with self.assertWarns(W_E): self.assertFalse(cr(i, False))
        with self.assertRaises(EXC_NAP): cr(dnr, True)
        with self.assertRaises(EXC_NAP): cr(fnr, False)

    def test_de(self):
        for i in ed: self.assertTrue(dele(i))
        for i in ef: self.assertTrue(dele(i))
        for i in ed:
            with self.assertWarns(W_NE): self.assertFalse(dele(i))
        for i in ef:
            with self.assertWarns(W_NE): self.assertFalse(dele(i))
        self.assertTrue(dele(dm))
        with self.assertRaises(EXC_NAP): dele(dnr)
        with self.assertRaises(EXC_NAP): dele(fnr)

    def test_mov(self):
        dele(dmv2); dele(fmv2);                                                 # Delete the move directory 2 and
                                                                                # move file 2.
        self.assertTrue(m(dmv1, dmv2)); cr(dmv1, True);                         # Re - create move directory 1.
        self.assertTrue(m(dmv1, dmv2)); cr(dmv1, True);                         # Re - create move directory 1 and
                                                                                # move directory 1 is replaced.
        self.assertTrue(m(fmv1, fmv2)); cr(fmv1, False);                        # Re - create move file 1.
        self.assertTrue(m(fmv1, fmv2)); cr(fmv1, False);                        # Re - create move file 1 and
                                                                                # move file 1 is replaced.
        with self.assertRaises(EXC_NAP): m(dne, dnr)
        with self.assertRaises(EXC_NAP): m(dnr, dne)
        with self.assertRaises(EXC_NAP): m(fne, fnr)
        with self.assertRaises(EXC_NAP): m(fnr, fne)
        with self.assertRaises(EXC_SP) : m(de, de)
        with self.assertWarns(W_E)     : self.assertFalse(m(dmv1, dmv2, False)) # Old move directory 1 is not replaced.
        with self.assertWarns(W_E)     : self.assertFalse(m(fmv1, fmv2, False)) # Old move file      1 is not replaced.
        dele(dmv1); dele(fmv1);                                                 # Delete the move directory 1 and
                                                                                # move file 1
        with self.assertWarns(W_NE)    : self.assertFalse(m(dmv1, dmv2))
        with self.assertWarns(W_NE)    : self.assertFalse(m(fmv1, fmv2))

    def test_ren(self):
        self.assertTrue(r(de, dren))
        self.assertTrue(r(fe, fren))
        cr(de, True); cr(fe, False); # Re - create.
        self.assertTrue(r(de, dren)) # Replace.
        self.assertTrue(r(fe, fren)) # Replace.
        cr(de, True); cr(fe, False); # Re - create.
        with self.assertRaises(EXC_NAP): self.assertFalse(r(dnr, dren))
        with self.assertRaises(EXC_NAP): self.assertFalse(r(fnr, fren))
        with self.assertRaises(EXC_SP) : r(de, "de")
        with self.assertWarns(W_E)     : self.assertFalse(r(de, dren, False)) # Not replace.
        with self.assertWarns(W_E)     : self.assertFalse(r(fe, fren, False)) # Not replace.
        with self.assertWarns(W_NE)    : self.assertFalse(r(dne, dren))
        with self.assertWarns(W_NE)    : self.assertFalse(r(fne, fren))


if __name__ == "__main__": unittest.main()