from sys       import platform            as p
from unittest  import TestCase            as TC
import getpass
import unittest
import warnings

from difi import chk_exst                 as ce
from difi import chk_exst_di              as ced
from difi import chk_exst_fi              as cef
from difi import cpy                      as c
from difi import crt                      as cr
from difi import de                       as d
from difi import mov                      as m
from difi import ren                      as r
from pth  import jo                       as j
from wrn  import wrn_exst                 as we
from wrn  import wrn_n_exst               as wne
from exc  import ExceptionNotAbsolutePath as EX_NAP
from exc  import ExceptionNotSamePath     as EX_NSP
from exc  import ExceptionSamePath        as EX_SP

DE         = "di_exst"                            # Directory that is exists.
DEC        = "di_exst_cpy"                        # Copy of directory that is exists.
DER        = "di_exst_ren"                        # Renamed directory that is exists.
DM         = "di_mov"                             # Moved directory.
DM         = "test_difi"                          # Main directory for this unit test.
DNE        = "di_n_exst"                          # Directory that is not exists.
DNEI       = "di_n_exst_ill/"                     # Directory that is not exists and is illegal.
DR         = "./"                                 # Relative directory.
DU         = "/home/{}".format(getpass.getuser()) # Unix home directory.
DW         = "C:\\"                               # Windows home directory.
FE         = "fi_exst.fi"                         # File that is exists.
FER        = "fi_exst_ren.fi"                     # Renamed file.
FNE        = "fi_n_exst.fi"                       # File that is not exists.
FNEI       = "fi_n_exst_ill/.fi"                  # File that is not exists and is illegal.

if   p == "darwin" or p == "linux":
    dudm       = j(DU, DM)       # Main test directory for this unit test.

    dudmdec    = j(dudm, DEC)    # Copy directory for Unix.

    dudmdecde  = j(dudmdec, DE)  # Copy directory for Unix directory exists.
    dudmdecdne = j(dudmdec, DNE) # Copy directory for Unix directory not exists.
    dudmdecfe  = j(dudmdec, FE)  # Copy directory for Unix file exists.
    dudmdecfne = j(dudmdec, FNE) # Copy directory for Unix file not exists.

    dudmde     = j(dudm, DE)     # Directory Unix exists.
    dudmdne    = j(dudm, DNE)    # Directory Unix not exists.
    dudmfe     = j(dudm, FE)     # File Unix exists.
    dudmfne    = j(dudm, FNE)    # File Unix not exists.
elif p == "cygwin" or p == "win32":
    dwdm       = j(DW, DM)       # Main test directory for this unit test.

    dwdmdec    = j(dwdm, DEC)    # Copy directory for Windows.

    dwdmdecde  = j(dwdmdec, DE)  # Copy directory for Windows directory exists.
    dwdmdecdne = j(dwdmdec, DNE) # Copy directory for Windows directory not exists.
    dwdmdecfe  = j(dwdmdec, FE)  # Copy directory for Windows file exists.
    dwdmdecfne = j(dwdmdec, FNE) # Copy directory for Windows file not exists.

    dwdmde     = j(dwdm, DE)     # Directory Windows exists.
    dwdmdne    = j(dwdm, DNE)    # Directory Windows not exists.
    dwdmfe     = j(dwdm, FE)     # File Windows exists.
    dwdmfne    = j(dwdm, FNE)    # File Windows not exists.

""" Create environment. """
def c_en():
    if   p == "darwin" or p == "linux":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cr(dudm); cr(dudmde); cr(dudmfe); cr(dudmdec);
    elif p == "cygwin" or p == "win32":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cr(dwdm); cr(dwdmde); cr(dwdmfe); cr(dwdmdec);

""" Delete environment. """
def d_en():
    if   p == "darwin" or p == "linux":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            d(dudm); d(dudmde); d(dudmfe); d(dudmdec);
    elif p == "cygwin" or p == "win32":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            d(dwdm); d(dwdmde); d(dwdmfe); d(dwdmdec);

class unit_test(TC):
    d_en()

    def test_chk_exst(self):
        d_en()
        c_en()

        du = n("/home/{}".format(getpass.getuser()))
        dw = n("C:\\{}\\Documents and Settings\\My Documents".format(getpass.getuser()))
        d = None
        if p == "cygwin" or p == "win32": d = du
        else                            : d = dw # Other than Windows refer any
                                                 # other operating system to Unix.
        dm   = j(d, "dm_{}".format(_nm_tst))     # Main directory for this unit test.

        dc   = j(dm, "dc")                       # Copied test directory that is exists.
        dd   = j(dm, "dd")                       # Deleted test directory that is exists.
        de   = j(dm, "de")                       # Test directory that is exists.
        dmv1 = j(dm, "dmv1")                     # Moved test directory 1 that is exists.
        dmv2 = j(dm, "dmv2")                     # Moved test directory 2 that is exists.
        dr1  = j(dm, "dr1")                      # Renamed test directory 1 that is exists.
        dr2  = j(dm, "dr2")                      # Renamed test directory 2 that is exists.
        dne  = j(dm, "dne")                      # Test directory that is not exists.
        dni  = j(dm, "di\\")                     # Illegal directory that is not exists.
        dnr  = n("./")                           # Relative directory that is not exists.

        dc   = j(dm, "fc.fi")                    # Copied test file that is exists.
        dd   = j(dm, "fd.fi")                    # Deleted test file that is exists.
        de   = j(dm, "fe.fi")                    # Test file that is exists.
        dmv1 = j(dm, "fmv1.fi")                  # Moved test file 1 that is exists.
        dmv2 = j(dm, "fmv2.fi")                  # Moved test file 2 that is exists.
        dr1  = j(dm, "fr1.fi")                   # Renamed test file 1 that is exists.
        dr2  = j(dm, "fr2.fi")                   # Renamed test file 2 that is exists.
        dne  = j(dm, "fne.fi")                   # Test file that is not exists.
        dni  = j(dm, "fi.fi\\")                  # Illegal file that is not exists.
        dnr  = n("./fi.fi")                      # Relative file that is not exists.

    def test_chk_exst(self):
        if   p == "darwin" or p == "linux":
            d_en()
            c_en()
            self.assertFalse(ce(dudmdne))
            self.assertFalse(ce(dudmfne))
            self.assertTrue(ce(dudmde))
            self.assertTrue(ce(dudmdec))
            self.assertTrue(ce(dudmfe))
            d_en()
        elif p == "cygwin" or p == "win32":
            d_en()
            c_en()
            self.assertFalse(ce(dwdmdne))
            self.assertFalse(ce(dwdmfne))
            self.assertTrue(ce(dwdmde))
            self.assertTrue(ce(dwdmdec))
            self.assertTrue(ce(dwdmfe))
            d_en()
    def test_chk_exst_di(self):
        if   p == "darwin" or p == "linux":
            d_en()
            c_en()
            self.assertFalse(ced(dudmdne))
            self.assertFalse(ced(dudmfe))
            self.assertFalse(ced(dudmfne))
            self.assertTrue(ced(dudmde))
            self.assertTrue(ced(dudmdec))
            d_en()
        elif p == "cygwin" or p == "win32":
            d_en()
            c_en()
            self.assertFalse(ced(dwdmdne))
            self.assertFalse(ced(dwdmfe))
            self.assertFalse(ced(dwdmfne))
            self.assertTrue(ced(dwdmde))
            self.assertTrue(ced(dwdmdec))
            d_en()
    def test_chk_exst_fi(self):
        if   p == "darwin" or p == "linux":
            d_en()
            c_en()
            self.assertFalse(cef(dudmde))
            self.assertFalse(cef(dudmdec))
            self.assertFalse(cef(dudmdne))
            self.assertFalse(cef(dudmfne))
            self.assertTrue(cef(dudmfe))
            d_en()
        elif p == "cygwin" or p == "win32":
            d_en()
            c_en()
            self.assertFalse(cef(dwdmde))
            self.assertFalse(cef(dwdmdec))
            self.assertFalse(cef(dwdmdne))
            self.assertFalse(cef(dwdmfne))
            self.assertTrue(cef(dwdmfe))
            d_en()
    def test_cpy(self):
        if   p == "darwin" or p == "linux":
            d_en()
            c_en()
            self.assertTrue(c(dudmde, dudmdecde))
            self.assertTrue(c(dudmde, dudmdecde)) # Automatically replace (not merge ) directory.
            self.assertTrue(c(dudmfe, dudmdecfe))
            self.assertTrue(c(dudmfe, dudmdecfe)) # Automatically replace (not merge ) file.
            with self.assertRaises(EX_SP): c(dudmde, dudmde)
            with self.assertWarns(we)    : self.assertFalse(c(dudmde, dudmdecde, False))
            with self.assertWarns(we)    : self.assertFalse(c(dudmfe, dudmdecfe, False))
            with self.assertWarns(wne)   : self.assertFalse(c(dudmdne, dudmdecdne))
            with self.assertWarns(wne)   : self.assertFalse(c(dudmfne, dudmdecfne))
            d_en()
        elif p == "cygwin" or p == "win32":
            d_en()
            c_en()
            self.assertTrue(c(dwdmde, dwdmdecde))
            self.assertTrue(c(dwdmde, dwdmdecde)) # Automatically replace (not merge ) directory.
            self.assertTrue(c(dwdmfe, dwdmdecfe))
            self.assertTrue(c(dwdmfe, dwdmdecfe)) # Automatically replace (not merge ) file.
            with self.assertRaises(EX_SP): c(dwdmde, dwdmde)
            with self.assertWarns(we)    : self.assertFalse(c(dwdmde, dwdmdecde, False))
            with self.assertWarns(we)    : self.assertFalse(c(dwdmfe, dwdmdecfe, False))
            with self.assertWarns(wne)   : self.assertFalse(c(dwdmdne, dwdmdecdne))
            with self.assertWarns(wne)   : self.assertFalse(c(dwdmfne, dwdmdecfne))
            d_en()

    def test_crt(self):
        if   p == "darwin" or p == "linux":
            d_en()
            self.assertTrue(cr(DU, DE, True))
            self.assertTrue(cr(DU, DEC, True))
            self.assertTrue(cr(DU, FE, False))
            with self.assertWarns(we): self.assertFalse(cr(DU, DE, True))
            with self.assertWarns(we): self.assertFalse(cr(DU, DEC, True))
            with self.assertWarns(we): self.assertFalse(cr(DU, FE, False))
            d_en()
        elif p == "cygwin" or p == "win32":
            d_en()
            self.assertTrue(cr(DW, DE, True))
            self.assertTrue(cr(DW, DEC, True))
            self.assertTrue(cr(DW, FE, False))
            with self.assertWarns(we): self.assertFalse(cr(DW, DE, True))
            with self.assertWarns(we): self.assertFalse(cr(DW, DEC, True))
            with self.assertWarns(we): self.assertFalse(cr(DW, FE, False))
            d_en()
        with self.assertRaises(EX_NAP): cr(DR, DNE)
        with self.assertRaises(EX_NAP): cr(DR, FNE)

    def test_de(self):
        if   p == "darwin" or p == "linux":
            d_en()
            c_en()
            self.assertTrue(d(dudmde))
            self.assertTrue(d(dudmfe))
            self.assertTrue(d(dudmdec))
            with self.assertWarns(wne): self.assertFalse(d(dudmde))
            with self.assertWarns(wne): self.assertFalse(d(dudmdec))
            with self.assertWarns(wne): self.assertFalse(d(dudmdne))
            with self.assertWarns(wne): self.assertFalse(d(dudmfe))
            with self.assertWarns(wne): self.assertFalse(d(dudmfne))
        elif p == "cygwin" or p == "win32":
            d_en()
            c_en()
            self.assertTrue(d(dwdmde))
            self.assertTrue(d(dwdmfe))
            self.assertTrue(d(dwdmdec))
            with self.assertWarns(wne): self.assertFalse(d(dwdmde))
            with self.assertWarns(wne): self.assertFalse(d(dwdmdec))
            with self.assertWarns(wne): self.assertFalse(d(dwdmdne))
            with self.assertWarns(wne): self.assertFalse(d(dwdmfe))
            with self.assertWarns(wne): self.assertFalse(d(dwdmfne))
    def test_mov(self):
        if   p == "darwin" or p == "linux":
            d_en()
            c_en()
            self.assertTrue(m(dudmde, dudmdecde)); cr(DU, DE, True);
            self.assertTrue(m(dudmde, dudmdecde)); cr(DU, DE, True);
            self.assertTrue(m(dudmfe, dudmdecfe)); cr(DU, FE, False);
            self.assertTrue(m(dudmfe, dudmdecfe)); cr(DU, FE, False);
            with self.assertRaises(EX_SP): m(dudmde, dudmde)
            with self.assertWarns(we)    : self.assertFalse(m(dudmde, dudmdecde, False))
            with self.assertWarns(we)    : self.assertFalse(m(dudmfe, dudmdecfe, False))
            with self.assertWarns(wne)   : self.assertFalse(m(dudmdne, dudmdecdne))
            with self.assertWarns(wne)   : self.assertFalse(m(dudmfne, dudmdecfne))
            d_en()
        elif p == "cygwin" or p == "win32":
            d_en()
            c_en()
            self.assertTrue(m(dwdmde, dwdmdecde)); cr(DU, DE, True);
            self.assertTrue(m(dmwude, dwdmdecde)); cr(DU, DE, True);
            self.assertTrue(m(dwdmfe, dwdmdecfe)); cr(DU, FE, False);
            self.assertTrue(m(dwdmfe, dwdmdecfe)); cr(DU, FE, False);
            with self.assertRaises(EX_SP): m(dmwude, dwdmde)
            with self.assertWarns(we)    : self.assertFalse(m(dmwude, dwdmdecde, False))
            with self.assertWarns(we)    : self.assertFalse(m(dwdmfe, dwdmdecfe, False))
            with self.assertWarns(wne)   : self.assertFalse(m(dwdmdne, dudmdecdne))
            with self.assertWarns(wne)   : self.assertFalse(m(dwdmfne, dwdmdecfne))
            d_en()

    def test_ren(self):
        if   p == "darwin" or p == "linux":
            d_en()
            c_en()
            self.assertTrue(r(dudmde, DER))
            self.assertTrue(r(dudmfe, FER))
            with self.assertWarns(wne)               : self.assertFalse(r(dudmdne, DER))
            with self.assertWarns(wne)               : self.assertFalse(r(dudmfne, FER))
            with self.assertRaises(FileNotFoundError): self.assertFalse(r(dudmde, DNEI))
            with self.assertRaises(FileNotFoundError): self.assertFalse(r(dudmfe, FNEI))
            d_en()
        elif p == "cygwin" or p == "win32":
            d_en()
            c_en()
            self.assertTrue(r(dudmde, DER))
            self.assertTrue(r(dudmfe, FER))
            with self.assertWarns(wne)               : self.assertFalse(r(dudmdne, DER))
            with self.assertWarns(wne)               : self.assertFalse(r(dudmfne, FER))
            with self.assertRaises(FileNotFoundError): self.assertFalse(r(dudmde, DNEI))
            with self.assertRaises(FileNotFoundError): self.assertFalse(r(dudmfe, FNEI))
            d_en()
if __name__ == "__main__":
    unittest.main()