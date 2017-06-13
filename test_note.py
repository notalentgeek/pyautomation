from   sys      import platform                 as p
from   unittest import TestCase                 as TC
import getpass
import unittest
import warnings

from   dbg      import print_ut                 as put
from   difi     import crt                      as cr
from   difi     import de                       as dele
from   note     import append_md                as am
from   note     import chk_exst_m_md            as cmm
from   note     import chk_exst_md              as cm
from   note     import chk_md_b                 as cmb
from   note     import crt_md                   as crm
from   note     import get_md                   as gm
from   note     import init                     as i
from   note     import read_md                  as r
from   note     import write_b_md               as wbm
from   note     import write_md                 as wm
from   pth      import jo                       as j
from   pth      import ncnp                     as n
from   exc      import ExceptionNotAbsolutePath as EX_NAP
from   exc      import ExceptionNotDirectory    as EX_ND
from   exc      import ExceptionNotFile         as EX_NF
from   wrn      import WarningMultipleMDFiles   as W_MMD
from   wrn      import WarningNotAllString      as W_NT_A_S
from   wrn      import WarningNotMDFile         as W_NT_MD
import var

du = n("/home/{}".format(getpass.getuser()))
dw = n("C:\\{}\\Documents and Settings\\My Documents".format(getpass.getuser()))
d  = du                                  # Unix    platform.
if p == "cygwin" or p == "win32": d = dw # Windows platform.

dm     = j(d, "dm_test_note")   # Main directory for this unit test.

dme    = j(dm, "dme")           # Directory with     .md file      exists.
dmef   = j(dm, "dmef")          # Directory with     .md file      exists and is      filled with dummy text.
dmewcf = j(dm, "dmewcf")        # Directory with     .md file  not exists but will be created and filled with dummy text.
dmewf  = j(dm, "dmewf")         # Directory with     .md file      exists and will be filled with dummy text.
dmme   = j(dm, "dmme")          # Directory with     .md files     exist.
dmne   = j(dm, "dmne")          # Directory with     .md file  not exists.
dnmd   = j(dm, "dnmd")          # Directory with non .md file exists.

dmi    = j(dm, "di")            # Directory for initiating note.
dre    = n("./md.md")           # Relative directory.
md     = j(dme, "md.md")        # Empty .md file.
md1    = j(dmme, "md1.md")      # Empty first  .md file.
md2    = j(dmme, "md2.md")      # Empty second .md file.
mdf    = j(dmef, "mdf.md")      # .md file that is filled with dummy text.
mdwf   = j(dmewf, "mdwf.md")    # .md file that will be filled with dummy text.
nmd    = j(dnmd, "not_md.fi")   # Non .md file that is exists.

""" Do not create this in `setUp()`! """
mdwcf  = j(dmewcf, "dmewcf.md") # .md file that is not exists but will be created and willed.
mdo    = j(dm, "md.md")         # Creating .md file in the outermost of the directory.
nmdo   = j(dm, "not_md.fi")     # Creating file that is not .md file.

e      = [dm, dme, dmef, dmewcf, dmewf, dmme, dmne, dnmd, dmi, md, md1, md2, mdf, mdwf, nmd]
ed     = [dm, dme, dmef, dmewcf, dmewf, dmme, dmne, dnmd, dmi]
ef     = [md, md1, md2, mdf, mdwf, nmd]

def su():
    for i in ed: cr(i, True)
    for i in ef: cr(i, False)
    wm(mdf, var.smpl_txt)      # Create .md file that is filled with dummy text.
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

    def test_append_md(self):
        self.assertTrue(am(mdwf, var.smpl_txt))
        with self.assertWarns(W_NT_A_S): self.assertFalse(am(mdwf, ["a", "b", "c", 1]))
        with self.assertWarns(W_NT_MD) : self.assertFalse(am(nmd, var.smpl_txt))

    def test_write_md(self):
        self.assertTrue(wm(mdwf, var.smpl_txt))
        with self.assertWarns(W_NT_A_S): self.assertFalse(wm(mdwf, ["a", "b", "c", 1]))
        with self.assertWarns(W_NT_MD) : self.assertFalse(wm(nmd, var.smpl_txt))

    def test_write_b_md(self):
        self.assertTrue(wbm(md))
        self.assertTrue(wbm(md1))
        self.assertTrue(wbm(md2))
        with self.assertWarns(W_NT_MD): self.assertFalse(wbm(nmd))

    def test_chk_exst_m_md(self):
        self.assertFalse(cmm(dmne))
        self.assertFalse(cmm(dme))
        self.assertTrue(cmm(dmme))
        with self.assertRaises(EX_NAP): cmm(dre)
        with self.assertRaises(EX_ND) : cmm(md)

    def test_chk_md(self):
        self.assertFalse(cm(dmne))
        self.assertTrue(cm(dme))
        self.assertTrue(cm(dmme))
        with self.assertRaises(EX_NAP): cm(dre)
        with self.assertRaises(EX_ND) : cm(md)

    def test_chk_md_b(self):
        self.assertTrue(cmb(md))
        self.assertTrue(cmb(md1))
        self.assertTrue(cmb(md2))

    def test_crt_md(self):
        self.assertTrue(crm(mdo))
        with self.assertRaises(EX_NAP): crm(dre)
        with self.assertRaises(EX_ND) : gm(mdo)
        with self.assertWarns(W_NT_MD): self.assertFalse(crm(nmdo))

    def test_get_md(self):
        self.assertEqual(gm(dme), md)
        self.assertEqual(gm(dmme), md1)
        self.assertNotEqual(gm(dmme), md2)
        self.assertFalse(bool(gm(dmne)))
        with self.assertRaises(EX_NAP): gm(dre)
        with self.assertRaises(EX_ND) : gm(md)

    def test_init(self):
        i(dme)
        i(dmef)
        i(dmne)

    def test_read_md(self):
        put("read_md(mdf)", r(mdf))
        self.assertEqual(len(r(mdf)), 5)
        self.assertEqual(len(r(md)) , 0)
        self.assertEqual(len(r(md1)), 0)
        self.assertEqual(len(r(md2)), 0)
        with self.assertRaises(EX_NAP): r(dre)
        with self.assertRaises(EX_NF) : r(dm)
        with self.assertWarns(W_NT_MD): self.assertFalse(r(nmd))

if __name__ == "__main__": unittest.main()