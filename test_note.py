from sys import platform as p
from unittest import TestCase as TC
import getpass
import unittest

from dbg import crt_img_dbg as cid
from dbg import print_ut as put
from difi import crt as cr
from difi import de
from note import apnd_md as am
from note import aw_md_ as awd
from note import chk_exst_md as cm
from note import chk_md_b as cmb
from note import crt_apnm_attach as ca
from note import crt_apnm_embed as ce
from note import crt_apnm_note as cn
from note import crt_md as crm
from note import crt_s_md as csmd
from note import fix_su as fs
from note import get_lst_n_md as glnm
from note import get_md as gm
from note import init as i
from note import rd_md as rd
from note import repair as r
from note import wrt_md as wm
from note import wrt_md_b as wbm
from pth import chk_ext_img as cei
from pth import jo as j
from pth import ncnp as n
from exc import ExceptionExistMultipleMDFiles as EX_EMMD
from exc import ExceptionExistsDirectoryInDirectory as EX_DND
from exc import ExceptionListNotAllString as EX_LNAS
from exc import ExceptionMDFileContent as EX_MDC
from exc import ExceptionMDFileNoContent as EX_MDNC
from exc import ExceptionNotAbsolutePath as EX_NAP
from exc import ExceptionNotAbsolutePath as EX_NAP
from exc import ExceptionNotExistsDirectory as EX_NED
from exc import ExceptionNotExistsFile as EX_NEF
from exc import ExceptionNotExistsFileExtension as EX_NFE
from exc import ExceptionNotExistsMDFile as EX_NEMD
from exc import ExceptionNotExistsOpenMode as EX_NEOM
import var

""" It is important to have separate folder for each unit test Python file. """

# This unit test home directory.
du = n("/home/{}").format(getpass.getuser()) # Unix.
dw = "C:\\Users\\{}".format(getpass.getuser()) # Windows.

d = du # The used directory.
if p == "cygwin" or p == "win32": d = dw # Check if this program runs in Windows platform.
dm = j(d, "dm_test_note") # Main directory for this unit test.

""" The ideal case scenario is to only have one upper classification. This note
is not relevant anymore since I put everything locally into the test function
itself. But I can use this practice for future project.

Wrong and current example:
file_img_jpg = ["jpg1", "jpg2"]
file_img_png = ["png1", "png2"]
file_md = ["file1", "file2", "file3"]
file_img = file_img_jpg + file_img_png
file_all = file_img + file_md # Multiple classification from `file_img` to this `file_all`.

The proper example:
file_img_jpg = ["jpg1", "jpg2"]
file_img_png = ["png1", "png2"]
file_md = ["file1", "file2", "file3"]
file_img = file_img_jpg + file_img_png
file_all = file_img + file_img_jpg + file_img_png # Only one upper classification.
"""

class unit_test(TC):
    def setUp(self):
        cr(dm, True)

    def tearDown(self):
        de(dm)

    def test_apnd_md(self):
        f = j(dm, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        self.assertTrue(am(f, ls))
        de(f)

        f = j(dm, "f.md")
        cr(f, False)
        lns = [1, "2", "3"]
        with self.assertRaises(EX_LNAS): am(f, lns)
        de(f)

        f = n("./f.f")
        ls = ["1", "2", "3"]
        with self.assertRaises(EX_NAP): am(f, ls)

        f = j(dm, "f.md")
        ls = ["1", "2", "3"]
        with self.assertRaises(EX_NEF): am(f, ls)

        f = j(dm, "f.f")
        ls = ["1", "2", "3"]
        cr(f, False)
        with self.assertRaises(EX_NEMD): am(f, ls)
        de(f)

    def test_aw_md_(self): put("awd(...)", "PENDING: not yet unit tested")

    def test_chk_exst_md(self):
        self.assertFalse(cm(dm))

        f = j(dm, "f.f")
        cr(f, False)
        self.assertFalse(cm(dm))
        de(f)

        f = j(dm, "j.md")
        cr(f, False)
        self.assertTrue(cm(dm))
        de(f)

        d = n("./")
        with self.assertRaises(EX_NAP): cm(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED): cm(d)

    def test_chk_md_b(self):
        f = j(dm, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        am(f, ls)
        self.assertFalse(cmb(f))
        de(f)

        f = j(dm, "f.md")
        cr(f, False)
        self.assertTrue(cmb(f))
        de(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP): cmb(f)

        f = j(dm, "f.md")
        with self.assertRaises(EX_NEF): cmb(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NEMD): cmb(f)
        de(f)

    def test_crt_apnm_attach(self): put("ca(...)", "PENDING: not yet unit tested")

    def test_crt_apnm_embed(self): put("ce(...)", "PENDING: not yet unit tested")

    def test_crt_apnm_img(self): put("ci(...)", "PENDING: not yet unit tested")

    def test_crt_apnm_note(self):
        cn_ = cn(dm)
        put("cn(dm).ap_di", cn_.ap_di)
        put("cn(dm).ap_md", cn_.ap_md)
        put("cn(dm).nm_di", cn_.nm_di)
        put("cn(dm).nm_md", cn_.nm_md)

        d = j(dm, "d")
        cr(d, True)
        with self.assertRaises(EX_DND): cn(dm)
        de(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED): cn(d)

        d = n("./")
        with self.assertRaises(EX_NAP): cn(d)

    def test_crt_md(self):
        f = j(dm, "f.md")
        self.assertTrue(crm(f))
        de(f)

        f = n("./f.md")
        with self.assertRaises(EX_NAP): crm(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NEMD): crm(f)
        de(f)

    def test_crt_s_md(self):
        f = j(dm, "f.bmp")
        cid(f)
        put("csmd(f)", csmd(f, True))
        de(f)

        f = j(dm, "f.jpeg")
        cid(f)
        put("csmd(f)", csmd(f, True))
        de(f)

        f = j(dm, "f.jpg")
        cid(f)
        put("csmd(f)", csmd(f, True))
        de(f)

        f = j(dm, "f.png")
        cid(f)
        put("csmd(f)", csmd(f, True))
        de(f)

        f = j(dm, "f.f")
        cr(f, False)
        put("csmd(f)", csmd(f, False))
        de(f)

        f = j(dm, "f")
        cr(f, False)
        with self.assertRaises(EX_NFE): csmd(f, False)
        de(f)

    def test_fix_su(self): put("fs(...)", "PENDING: not yet unit tested")

    def test_get_lst_n_md(self): 
        f1 = j(dm, "f1.md")
        cr(f1, False)
        f2 = j(dm, "f2.f")
        cr(f2, False)
        f3 = j(dm, "f3.f")
        cr(f3, False)
        put("glnm(dm)", glnm(dm))
        de(f1)
        de(f2)
        de(f3)

        d = j(dm, "d")
        cr(d, True)
        with self.assertRaises(EX_DND): glnm(dm)
        de(d)

        f1 = j(dm, "f1.md")
        cr(f1, False)
        f2 = j(dm, "f2.md")
        cr(f2, False)
        with self.assertRaises(EX_EMMD): glnm(dm)
        de(f1)
        de(f2)

        d = n("./")
        with self.assertRaises(EX_NAP): glnm(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED): glnm(d)

    def test_get_md(self):
        f = j(dm, "f.md")
        cr(f, False)
        put("gm(dm)", gm(dm))
        de(f)

        f1 = j(dm, "f1.md")
        f2 = j(dm, "f2.md")
        cr(f1, False)
        cr(f2, False)
        with self.assertRaises(EX_EMMD): gm(dm)
        de(f1)
        de(f2)
       
        d = n("./")
        with self.assertRaises(EX_NAP): gm(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED): gm(d)

        with self.assertRaises(EX_NEMD): gm(dm)

    def test_init(self):
        d = j(dm, "d")
        cr(d, True)
        f1 = j(d, "f1.bmp")
        cid(f1)
        f2 = j(d, "f2.jpeg")
        cid(f2)
        f3 = j(d, "f3.jpg")
        cid(f3)
        f4 = j(d, "f4.png")
        cid(f4)
        f5 = j(d, "f5.fi")
        cr(f5, False)
        dn = i(d)
        self.assertNotEqual(d, dn)
        de(dn)

        d = j(dm, "20000101-0000-cet-d")
        cr(d, True)
        f1 = j(d, "f1.bmp")
        cid(f1)
        f2 = j(d, "f2.jpeg")
        cid(f2)
        f3 = j(d, "f3.jpg")
        cid(f3)
        f4 = j(d, "f4.png")
        cid(f4)
        f5 = j(d, "f5.fi")
        cr(f5, False)
        dn = i(d)
        self.assertEqual(d, dn)
        de(dn)

        f1 = j(dm, "f1.md")
        cr(f1, False)
        f2 = j(dm, "f2.md")
        cr(f2, False)
        with self.assertRaises(EX_EMMD): i(dm)
        de(f1)
        de(f2)

        d = j(dm, "d")
        cr(d, True)
        f = j(d, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        am(f, ls)
        with self.assertRaises(EX_MDC): i(d)
        de(d)

        d = j(dm, "20000101-0000-cet-d")
        cr(d, True)
        f = j(d, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        am(f, ls)
        with self.assertRaises(EX_MDC): i(d)
        de(d)

        d = n("./")
        with self.assertRaises(EX_NAP): i(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED): i(d)

    def test_rd_md(self):
        f = j(dm, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        am(f, ls)
        put("rd(f)", rd(f))
        de(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP): rd(f)

        f = j(dm, "f.f")
        with self.assertRaises(EX_NEF): rd(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NEMD): rd(f)
        de(f)

    def test_repair(self):
        d = j(dm, "d")
        cr(d, True)
        fm = j(d, "fm.md")
        cr(fm, False)
        am(fm, var.smpl_md)
        f1 = j(d, "f1.bmp")
        cid(f1)
        f2 = j(d, "f2.jpeg")
        cid(f2)
        f3 = j(d, "f3.jpg")
        cid(f3)
        f4 = j(d, "f4.png")
        cid(f4)
        f5 = j(d, "f5.fi")
        cr(f5, False)
        dn = r(d)
        put("r(d)", dn)
        # PENDING: Test.
        de(dn)

        d = j(dm, "20000101-0000-cet-d")
        cr(d, True)
        fm = j(d, "fm.md")
        cr(fm, False)
        am(fm, var.smpl_md)
        f1 = j(d, "f1.bmp")
        cid(f1)
        f2 = j(d, "f2.jpeg")
        cid(f2)
        f3 = j(d, "f3.jpg")
        cid(f3)
        f4 = j(d, "f4.png")
        cid(f4)
        f5 = j(d, "f5.fi")
        cr(f5, False)
        dn = r(d)
        put("r(d)", dn)
        # PENDING: Test.
        de(dn)

        f1 = j(dm, "f1.md")
        cr(f1, False)
        f2 = j(dm, "f2.md")
        cr(f2, False)
        with self.assertRaises(EX_EMMD): r(dm)
        de(f1)
        de(f2)

        d = j(dm, "d")
        cr(d, True)
        f = j(d, "f.md")
        cr(f, False)
        with self.assertRaises(EX_MDNC): r(d)
        de(d)

        d = j(dm, "20000101-0000-cet-d")
        cr(d, True)
        f = j(d, "f.md")
        cr(f, False)
        with self.assertRaises(EX_MDNC): r(d)
        de(d)

        d = n("./")
        with self.assertRaises(EX_NAP): r(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED): r(d)

        d = j(dm, "d")
        cr(d, True)
        with self.assertRaises(EX_NEMD): r(d)
        de(d)

    def test_wrt_md(self):
        f = j(dm, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        self.assertTrue(wm(f, ls))
        de(f)

        f = j(dm, "f.md")
        cr(f, False)
        lns = [1, "2", "3"]
        with self.assertRaises(EX_LNAS): wm(f, lns)
        de(f)

        f = n("./f.f")
        ls = ["1", "2", "3"]
        with self.assertRaises(EX_NAP): wm(f, ls)

        f = j(dm, "f.md")
        ls = ["1", "2", "3"]
        with self.assertRaises(EX_NEF): wm(f, ls)

        f = j(dm, "f.f")
        ls = ["1", "2", "3"]
        cr(f, False)
        with self.assertRaises(EX_NEMD): wm(f, ls)
        de(f)

    def test_wrt_md_b(self):
        f = j(dm, "f.md")
        cr(f, False)
        self.assertTrue(wbm(f))
        de(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP): wbm(f)

        f = j(dm, "f.md")
        with self.assertRaises(EX_NEF): wbm(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NEMD): wbm(f)
        de(f)

if __name__ == "__main__": unittest.main()