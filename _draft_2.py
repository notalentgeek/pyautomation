from sys import platform as p
from unittest import TestCase as TC
import getpass
import unittest
import warnings

from dbg import print_ut as put
from difi import crt as cr
from difi import de as dele
from note import append_md as am
from note import chk_exst_m_md as cmm
from note import chk_exst_md as cm
from note import chk_md_b as cmb
from note import crt_md as crm
from note import crt_nm as cn
from note import crt_nm_fi as cnf
from note import get_lst_n_md as glnm
from note import get_md as gm
from note import init as i
from note import read_md as r
from note import write_b_md as wbm
from note import write_md as wm
from pth import chk_ext_img as cei
from pth import jo as j
from pth import ncnp as n
from exc import ExceptionExistMultipleMDFiles as EX_MMD
from exc import ExceptionExistsDirectory as EX_D
from exc import ExceptionListIsNotAllString as EX_LNAS
from exc import ExceptionNotAbsolutePath as EX_NAP
from exc import ExceptionNotExistsDirectory as EX_ND
from exc import ExceptionNotExistsFile as EX_NF
from exc import ExceptionNotExistsFileExtension as EX_NFE
from exc import ExceptionNotExistsMDFile as EX_NMD
import var

du = n("/home/{}".format(getpass.getuser()))
dw = n("C:\\{}\\Documents and Settings\\My Documents".format(getpass.getuser()))
d = du # Unix platform.
if p == "cygwin" or p == "win32": d = dw # Windows platform.

dm = j(d, "dm_test_note") # Main directory for this unit test.

dmdf = j(dm, "dmdf") # Direcotry with .md file exists and with several files exist.
dme = j(dm, "dme") # Directory with .md file exists.
dmef = j(dm, "dmef") # Directory with .md file exists and is filled with dummy text.
dmewcf = j(dm, "dmewcf") # Directory with .md file not exists but will be created and filled with dummy text.
dmewf = j(dm, "dmewf") # Directory with .md file exists and will be filled with dummy text.
dmme = j(dm, "dmme") # Directory with .md files exist.
dmne = j(dm, "dmne") # Directory with .md file not exists.
dnmd = j(dm, "dnmd") # Directory with non .md file exists.
dnmdf = j(dm, "dnmdf") # Directory with .md file not exists and with several files exist.

dmp = j(dm, "20000101-0000-dmp") # Directory with properly named .md file and folder.
dmpn = j(dm, "20000101-0000-dmpn") # Directory with proper name but different name between .md file and folder.

dmi = j(dm, "di") # Directory for initiating note.

dre = n("./md.md") # Relative directory.
f1md = j(dmdf, "f1md.fi") # Sample file located in a directory where there is .md file.
f1md_md = j(dmdf, "f1md_md.md") # Sample .md file located in a directory where there are multiple files.
f1nmd = j(dnmdf, "f1nmd.fi") # Sample file located in a directory where there is no .md file.
f2md = j(dmdf, "f2md.fi") # Sample file located in a directory where there is .md file.
f2nmd = j(dnmdf, "f2nmd.fi") # Sample file located in a directory where there is no .md file.
i1md = j(dnmdf, "i1md.bmp") # Sample image.
i2md = j(dnmdf, "i2md.jpg") # Sample image.
i3md = j(dnmdf, "i3md.png") # Sample image.
md = j(dme, "md.md") # Empty .md file.
md1 = j(dmme, "md1.md") # Empty first  .md file.
md2 = j(dmme, "md2.md") # Empty second .md file.
mdf = j(dmef, "mdf.md") # .md file that is filled with dummy text.
mdp = j(dmp, "20000101-0000-dmp.md") # .md file with prefix.
mdpn = j(dmpn, "md.md") # .md file without prefix in folder with proper name.
mdwf = j(dmewf, "mdwf.md") # .md file that will be filled with dummy text.
nmd = j(dnmd, "not_md.fi") # Non .md file that is exists.

""" Do not create this in `setUp()`! """
mdwcf = j(dmewcf, "dmewcf.md")      # .md file that is not exists but will be created and willed.
mdo = j(dm, "md.md")              # Creating .md file in the outermost of the directory.
nmdo = j(dm, "not_md.fi")          # Creating file that is not .md file.

e = [dm, dmdf, dme, dmef, dmewcf, dmewf, dmme, dmne, dnmd, dnmdf, dmp, dmpn, dmi, f1md, f1md_md, f1nmd, f2md, f2nmd, i1md, i2md, i3md, md, md1, md2, mdf, mdp, mdpn, mdwf, nmd]
ed = [dm, dmdf, dme, dmef, dmewcf, dmewf, dmme, dmne, dnmd, dnmdf, dmp, dmpn, dmi]
ef = [f1md, f1md_md, f1nmd, f2md, f2nmd, i1md, i2md, i3md, md, md1, md2, mdf, mdp, mdpn, mdwf, nmd]

def su():
    for i in ed: cr(i, True)
    for i in ef: cr(i, False)

    """ Create .md file that is filled with dummy text. """
    wm(mdf, var.smpl_txt)

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
        with self.assertRaises(EX_LNAS): am(mdwf, ["a", "b", "c", 1])
        with self.assertRaises(EX_NMD): am(nmd, var.smpl_txt)

    def test_write_md(self):
        self.assertTrue(wm(mdwf, var.smpl_txt))
        with self.assertRaises(EX_LNAS): wm(mdwf, ["a", "b", "c", 1])
        with self.assertRaises(EX_NMD): wm(nmd, var.smpl_txt)

    def test_write_b_md(self):
        self.assertTrue(wbm(md))
        self.assertTrue(wbm(md1))
        self.assertTrue(wbm(md2))
        with self.assertRaises(EX_NMD): wbm(nmd)

    def test_chk_exst_m_md(self):
        self.assertFalse(cmm(dmne))
        self.assertFalse(cmm(dme))
        self.assertTrue(cmm(dmme))
        with self.assertRaises(EX_NAP): cmm(dre)
        with self.assertRaises(EX_ND): cmm(md)

    def test_chk_md(self):
        self.assertFalse(cm(dmne))
        self.assertTrue(cm(dme))
        self.assertTrue(cm(dmme))
        with self.assertRaises(EX_NAP): cm(dre)
        with self.assertRaises(EX_ND): cm(md)

    def test_chk_md_b(self):
        self.assertTrue(cmb(md))
        self.assertTrue(cmb(md1))
        self.assertTrue(cmb(md2))

    def test_crt_md(self):
        self.assertTrue(crm(mdo))
        with self.assertRaises(EX_NAP): crm(dre)
        with self.assertRaises(EX_ND): gm(mdo)
        with self.assertRaises(EX_NMD): crm(nmdo)

    def test_crt_nm(self):
        put("cn(dme)"  , cn(dme)  , False)
        put("cn(dmef)" , cn(dmef) , False)
        put("cn(dmewcf)", cn(dmewcf), False)
        put("cn(dmewf)", cn(dmewf), False)
        put("cn(dmme)" , cn(dmme) , False)
        put("cn(dmne)" , cn(dmne) , False)
        put("cn(dnmd)" , cn(dnmd))

    def test_crt_nm_fi(self):
        put("cnf(\"fi.bmp\", cei(\"fi.bmp\"))", cnf("fi.bmp", cei("fi.bmp")))
        put("cnf(\"fi.fi\", cei(\"fi.fi\"))", cnf("fi.fi", cei("fi.fi")))
        put("cnf(\"fi.jpeg\", cei(\"fi.jpeg\"))", cnf("fi.jpeg", cei("fi.jpeg")))
        put("cnf(\"fi.jpg\", cei(\"fi.jpg\"))", cnf("fi.jpg", cei("fi.jpg")))
        put("cnf(\"fi.png\", cei(\"fi.png\"))", cnf("fi.png", cei("fi.png")))
        with self.assertRaises(EX_NFE): cnf("fi", cei("fi"))

    def test_get_lst_n_md(self):
        for i in ef:
            with self.assertRaises(EX_ND): glnm(i)
        self.assertEqual(len(glnm(dmdf)), 2)
        self.assertEqual(len(glnm(dnmdf)), 5)
        with self.assertRaises(EX_D): glnm(dm)
        with self.assertRaises(EX_MMD): glnm(dmme)
        with self.assertRaises(EX_NAP): glnm(dre)

    def test_get_md(self):
        self.assertEqual(gm(dme), md)
        self.assertEqual(gm(dmme), md1)
        self.assertNotEqual(gm(dmme), md2)
        self.assertFalse(bool(gm(dmne)))
        with self.assertRaises(EX_NAP): gm(dre)
        with self.assertRaises(EX_ND): gm(md)

    def test_init(self):
        print("\n{}".format("="*50)) # To make nicer the console output.
        #i(dmdf)
        #i(dme)
        #i(dmef)
        #i(dmne)
        #i(dmp)
        #i(dmpn)
        i(dnmdf)
        print("="*50)

    def test_read_md(self):
        put("read_md(mdf)", r(mdf))
        self.assertEqual(len(r(mdf)), 5)
        self.assertEqual(len(r(md)), 0)
        self.assertEqual(len(r(md1)), 0)
        self.assertEqual(len(r(md2)), 0)
        with self.assertRaises(EX_NAP): r(dre)
        with self.assertRaises(EX_NF): r(dm)
        with self.assertRaises(EX_NMD): r(nmd)

if __name__ == "__main__": unittest.main()