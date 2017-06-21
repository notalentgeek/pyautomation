from sys import platform as p
from unittest import TestCase as TC
import getpass
import unittest
import warnings

from dbg import print_ut as put
from difi import crt as cr
from difi import de as dele
from note import apnd_md as am
from note import chk_exst_md as cm
from note import chk_md_b as cmb
from note import crt_md as crm
from note import crt_nm as cn
from note import crt_nm_img as cni
from note import crt_nm_md as cnm
from note import get_lst_n_md as glnm
from note import get_md as gm
from note import init as i
from note import rd_md as r
from note import wrt_md as wm
from note import wrt_md_b as wbm
from pth import chk_ext_img as cei
from pth import jo as j
from pth import ncnp as n
from exc import ExceptionExistMultipleMDFiles as EX_EMMD
from exc import ExceptionExistsDirectoryInDirectory as EX_DND
from exc import ExceptionListNotAllString as EX_LNAS
from exc import ExceptionNotAbsolutePath as EX_NAP
from exc import ExceptionNotAbsolutePath as EX_NAP
from exc import ExceptionNotExistsDirectory as EX_NED
from exc import ExceptionNotExistsFile as EX_NEF
from exc import ExceptionNotExistsFileExtension as EX_NFE
from exc import ExceptionNotExistsImageFile as EX_NIMG
from exc import ExceptionNotExistsMDFile as EX_NEMD
from exc import ExceptionNotExistsOpenMode as EX_NEOM
import var

""" It is important to have separate folder for each unit test Python file. """

# This unit test home directory.
du = n("/home/{}").format(getpass.getuser()) # Unix.
dw = "C:\\Users\\{}\\Documents".format(getpass.getuser()) # Windows.

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
        dele(dm)

    def test_apnd_md(self):
        f = j(dm, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        self.assertTrue(am(f, ls))
        dele(f)

        f = j(dm, "f.md")
        cr(f, False)
        lns = [1, "2", "3"]
        with self.assertRaises(EX_LNAS):
            am(f, lns)
        dele(f)

        f = n("./f.f")
        ls = ["1", "2", "3"]
        with self.assertRaises(EX_NAP):
            am(f, ls)

        f = j(dm, "f.md")
        ls = ["1", "2", "3"]
        with self.assertRaises(EX_NEF):
            am(f, ls)

        f = j(dm, "f.f")
        ls = ["1", "2", "3"]
        cr(f, False)
        with self.assertRaises(EX_NEMD):
            am(f, ls)
        dele(f)

    def test_chk_exst_md(self):
        self.assertFalse(cm(dm))

        f = j(dm, "f.f")
        cr(f, False)
        self.assertFalse(cm(dm))
        dele(f)

        f = j(dm, "j.md")
        cr(f, False)
        self.assertTrue(cm(dm))
        dele(f)

        d = n("./")
        with self.assertRaises(EX_NAP):
            cm(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED):
            cm(d)

    def test_chk_md_b(self):
        f = j(dm, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        am(f, ls)
        self.assertFalse(cmb(f))
        dele(f)

        f = j(dm, "f.md")
        cr(f, False)
        self.assertTrue(cmb(f))
        dele(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP):
            cmb(f)

        f = j(dm, "f.md")
        with self.assertRaises(EX_NEF):
            cmb(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NEMD):
            cmb(f)
        dele(f)

    def test_crt_md(self):
        f = j(dm, "f.md")
        self.assertTrue(crm(f))
        dele(f)

        f = n("./f.md")
        with self.assertRaises(EX_NAP):
            crm(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NEMD):
            crm(f)
        dele(f)

    def test_crt_nm(self):
        cn_ = cn(dm)
        put("cn(dm).di", cn_.di)
        put("cn(dm).fi", cn_.fi)
        put("cn(dm).nm", cn_.nm)

        d = j(dm, "d")
        cr(d, True)
        with self.assertRaises(EX_DND):
            cn(dm)
        dele(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED):
            cn(d)

        d = n("./")
        with self.assertRaises(EX_NAP):
            cn(d)

    def test_crt_nm_img(self):
        f = j(dm, "f.bmp")
        cr(f, False)
        cni_ = cni(f)
        put("cni(f).ap_bak", cni_.ap_bak)
        put("cni(f).ap_cn", cni_.ap_cn)
        put("cni(f).nm_bak", cni_.nm_bak)
        put("cni(f).nm_cn", cni_.nm_cn)
        dele(f)

        f = j(dm, "f.jpeg")
        cr(f, False)
        cni_ = cni(f)
        put("cni(f).ap_bak", cni_.ap_bak)
        put("cni(f).ap_cn", cni_.ap_cn)
        put("cni(f).nm_bak", cni_.nm_bak)
        put("cni(f).nm_cn", cni_.nm_cn)
        dele(f)

        f = j(dm, "f.jpg")
        cr(f, False)
        cni_ = cni(f)
        put("cni(f).ap_bak", cni_.ap_bak)
        put("cni(f).ap_cn", cni_.ap_cn)
        put("cni(f).nm_bak", cni_.nm_bak)
        put("cni(f).nm_cn", cni_.nm_cn)
        dele(f)

        f = j(dm, "f.png")
        cr(f, False)
        cni_ = cni(f)
        put("cni(f).ap_bak", cni_.ap_bak)
        put("cni(f).ap_cn", cni_.ap_cn)
        put("cni(f).nm_bak", cni_.nm_bak)
        put("cni(f).nm_cn", cni_.nm_cn)
        dele(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP):
            cni(f)

        f = j(dm, "f.bmp")
        with self.assertRaises(EX_NEF):
            cni(f)

        f = j(dm, "f.jpeg")
        with self.assertRaises(EX_NEF):
            cni(f)

        f = j(dm, "f.jpg")
        with self.assertRaises(EX_NEF):
            cni(f)

        f = j(dm, "f.png")
        with self.assertRaises(EX_NEF):
            cni(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NIMG):
            cni(f)
        dele(f)

    def test_crt_nm_md(self):
        f = j(dm, "f.bmp")
        cr(f, False)
        put("cnm(f)", cnm(f, True))
        dele(f)

        f = j(dm, "f.f")
        cr(f, False)
        put("cnm(f)", cnm(f, False))
        dele(f)

        f = j(dm, "f.jpeg")
        cr(f, False)
        put("cnm(f)", cnm(f, True))
        dele(f)

        f = j(dm, "f.jpg")
        cr(f, False)
        put("cnm(f)", cnm(f, True))
        dele(f)

        f = j(dm, "f.png")
        cr(f, False)
        put("cnm(f)", cnm(f, True))
        dele(f)


        f = j(dm, "f")
        cr(f, False)
        with self.assertRaises(EX_NFE):
            cnm(f, False)
        dele(f)

    def test_get_lst_n_md(self):
        f1 = j(dm, "f1.md")
        cr(f1, False)
        f2 = j(dm, "f2.f")
        cr(f2, False)
        f3 = j(dm, "f3.f")
        cr(f3, False)
        put("glnm(dm)", glnm(dm))
        dele(f1)
        dele(f2)
        dele(f3)

        d = j(dm, "d")
        cr(d, True)
        with self.assertRaises(EX_DND):
            glnm(dm)
        dele(d)

        f1 = j(dm, "f1.md")
        cr(f1, False)
        f2 = j(dm, "f2.md")
        cr(f2, False)
        with self.assertRaises(EX_EMMD):
            glnm(dm)
        dele(f1)
        dele(f2)

        d = n("./")
        with self.assertRaises(EX_NAP):
            glnm(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED):
            glnm(d)

    def test_get_md(self):
        f = j(dm, "f.md")
        cr(f, False)
        put("gm(dm)", gm(dm))
        dele(f)

        f1 = j(dm, "f1.md")
        f2 = j(dm, "f2.md")
        cr(f1, False)
        cr(f2, False)
        with self.assertRaises(EX_EMMD):
            gm(dm)
        dele(f1)
        dele(f2)
       
        d = n("./")
        with self.assertRaises(EX_NAP):
            gm(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED):
            gm(d)

        with self.assertRaises(EX_NEMD):
            gm(dm)
    
    def test_init(self):
        d = j(dm, "d")
        cr(d, True)
        f1 = j(d, "f1.bmp")
        cr(f1, False)
        f2 = j(d, "f2.jpeg")
        cr(f2, False)
        f3 = j(d, "f3.jpg")
        cr(f3, False)
        f4 = j(d, "f4.png")
        cr(f4, False)
        f5 = j(d, "f5.fi")
        cr(f5, False)
        dn = i(d)
        self.assertNotEqual(d, dn)
        dele(dn)

        f1 = j(dm, "f1.md")
        cr(f1, False)
        f2 = j(dm, "f2.md")
        cr(f2, False)
        with self.assertRaises(EX_EMMD):
            i(dm)
        dele(f1)
        dele(f2)

        d = n("./")
        with self.assertRaises(EX_NAP):
            i(d)

        d = j(dm, "d")
        with self.assertRaises(EX_NED):
            i(d)
    
    def test_rd_md(self):
        f = j(dm, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        am(f, ls)
        put("r(f)", r(f))
        dele(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP):
            r(f)

        f = j(dm, "f.f")
        with self.assertRaises(EX_NEF):
            r(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NEMD):
            r(f)
        dele(f)

    def test_wrt_md(self):
        f = j(dm, "f.md")
        cr(f, False)
        ls = ["1", "2", "3"]
        self.assertTrue(wm(f, ls))
        dele(f)

        f = j(dm, "f.md")
        cr(f, False)
        lns = [1, "2", "3"]
        with self.assertRaises(EX_LNAS):
            wm(f, lns)
        dele(f)

        f = n("./f.f")
        ls = ["1", "2", "3"]
        with self.assertRaises(EX_NAP):
            wm(f, ls)

        f = j(dm, "f.md")
        ls = ["1", "2", "3"]
        with self.assertRaises(EX_NEF):
            wm(f, ls)

        f = j(dm, "f.f")
        ls = ["1", "2", "3"]
        cr(f, False)
        with self.assertRaises(EX_NEMD):
            wm(f, ls)
        dele(f)
    
    def test_wrt_md_b(self):
        f = j(dm, "f.md")
        cr(f, False)
        self.assertTrue(wbm(f))
        dele(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP):
            wbm(f)

        f = j(dm, "f.md")
        with self.assertRaises(EX_NEF):
            wbm(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NEMD):
            wbm(f)
        dele(f)

if __name__ == "__main__": unittest.main()