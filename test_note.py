from   sys      import platform                 as p
from   unittest import TestCase                 as TC
import getpass
import unittest
import warnings

from   difi     import crt                      as cr
from   difi     import de                       as dele
from   note     import chk_m_md                 as cmm
from   note     import chk_md                   as cm
from   note     import init                     as i
from   pth      import jo                       as j
from   pth      import ncnp                     as n
from   exc      import ExceptionNotAbsolutePath as EX_NAP

du = n("/home/{}".format(getpass.getuser()))
dw = n("C:\\{}\\Documents and Settings\\My Documents".format(getpass.getuser()))
d  = du                                  # Unix    platform.
if p == "cygwin" or p == "win32": d = dw # Windows platform.

dm   = j(d, "dm_test_md") # Main directory for this unit test.

dme  = j(dm, "dme")       # Directory with .md file      exists.
dmme = j(dm, "dmme")      # Directory with .md files     exist.
dmne = j(dm, "dmne")      # Directory with .md file  not exists.
dmi  = j(dm, "di")        # Directory for initiating note.
dre  = n("./md.md")       # Relative directory.
md   = j(dme, "md.md")    # .md file.
md1  = j(dmme, "md1.md")  # First  .md file.
md2  = j(dmme, "md2.md")  # Second .md file.

e    = [dm, dme, dmme, dmne, dmi, md, md1, md2]
ed   = [dm, dme, dmme, dmne, dmi]
ef   = [md, md1, md2]

def su():
    for i in ed: cr(i, True)
    for i in ef: cr(i, False)
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

    def test_chk_m_md(self):
        self.assertFalse(cmm(dmne))
        self.assertFalse(cmm(dme))
        self.assertTrue(cmm(dmme))
        with self.assertRaises(EX_NAP): cmm(dre)

    def test_chk_md(self):
        self.assertFalse(cm(dmne))
        self.assertTrue(cm(dme))
        self.assertTrue(cm(dmme))
        with self.assertRaises(EX_NAP): cm(dre)

    def test_init(self):
        i(dmi, "md.md")

if __name__ == "__main__": unittest.main()