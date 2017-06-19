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
from note import crt_nm_fi as cnf
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

# This unit test home directory.
du = n("/home/{}").format(getpass.getuser()) # Unix.
dw = "C:\\Users\\{}\\Documents".format(getpass.getuser()) # Windows.

d = du # The used directory.
if p == "cygwin" or p == "win32": d = dw # Check if this program runs in Windows platform.
dm = j(d, "dm_test_note") # Main directory for this unit test.

deme = j(dm, "deme") # Directory exists with an .md file.
deme_m = j(deme, "deme_m.md")
dememie = j(dm, "dememie") # Directory exists with an .md file and with multiple images.
dememie_i1 = j(dememie, "dememie_i1.bmp")
dememie_i2 = j(dememie, "dememie_i2.jpeg")
dememie_i3 = j(dememie, "dememie_i3.jpg")
dememie_i4 = j(dememie, "dememie_i4.png")
dememie_m = j(dememie, "dememie_m.md")
demie = j(dm, "demie") # Directory exists with multiple images.
demie_i1 = j(demie, "demie_i1.bmp")
demie_i2 = j(demie, "demie_i2.jpeg")
demie_i3 = j(demie, "demie_i3.jpg")
demie_i4 = j(demie, "demie_i4.png")
demme = j(dm, "demme") # Directory exists with multiple .md files.
demme_m1 = j(demme, "demme_m1.md")
demme_m2 = j(demme, "demme_m2.md")
den = j(dm, "den") # Directory without any .md file.
den_m = j(den, "den_m.md")
denme = j(dm, "denme") # Directory exists but with non - .md file.
denme_nm = j(denme, "denme_nm.fi")
dne = j(dm, "dne") # A directory that is not exists.

lns = [1, "two", "three"]
ls = ["one", "two", "three"]

fim = [dememie_i1, dememie_i2, dememie_i3, dememie_i4, demie_i1, demie_i2, demie_i3, demie_i4]
fmd = [deme_m, dememie_m, demme_m1, demme_m2]
fo = [denme_nm]

dmd = [deme, dememie, demme]
dnmd = [demie, den, denme]

d = dmd + dnmd # All directories that should be created.
f = fim + fmd + fo # All files that should be created.
a = d + f # Both directories and files that should be created.

dn = [dne] # Not exists.
fn = [den_m] # Not exists.
dner = n("./") # Relative directory.

class unit_test(TC):
    def setUp(self):
        for i in d: cr(i, True)
        for i in f: cr(i, False)

    def tearDown(self):
        dele(dm)

    def test_apnd_md(self):
        for i in fmd: self.assertTrue(am(i, ls))
        for i in d:
            with self.assertRaises(EX_NEF): am(i, ls)
        for i in fim:
            with self.assertRaises(EX_NEMD): am(i, ls)
        for i in fmd:
            with self.assertRaises(EX_LNAS): am(i, lns)
        for i in fn:
            with self.assertRaises(EX_NEF): am(i, ls)
        with self.assertRaises(EX_NAP): am(dner, ls)

    def test_chk_exst_md(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsDirectory

        for i in f:
            with self.assertRaises(EX_NED): cm(i)
        for i in d

        cm

    """
    def test_chk_md_b(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsFile
        ExceptionNotExistsImageFile

        cmb
    def test_crt_md(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsMDFile
        ExceptionNotExistsDirectory

        crm
    def test_crt_nm(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsDirectory
        ExceptionExistsDirectoryInDirectory

        cn
    def test_crt_nm_fi(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsFile

        cnf
    def test_crt_nm_md(self):
        ExceptionNotExistsFileExtension

        cnm
    def test_get_lst_n_md(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsDirectory
        ExceptionExistMultipleMDFiles
        ExceptionExistsDirectoryInDirectory

        glnm
    def test_get_md(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsDirectory
        ExceptionNotExistsMDFile
        ExceptionExistMultipleMDFiles

        gm
    def test_init(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsDirectory

        i
    def test_rd_md(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsFile
        ExceptionNotExistsMDFile

        r
    def test_wrt_md(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsFile
        ExceptionNotExistsMDFile
        ExceptionListNotAllString
        ExceptionNotExistsOpenMode

        wm
    def test_wrt_md_b(self):
        ExceptionNotAbsolutePath
        ExceptionNotExistsFile
        ExceptionNotExistsMDFile
        ExceptionListNotAllString
        ExceptionNotExistsOpenMode

        wbm
    """

if __name__ == "__main__": unittest.main()