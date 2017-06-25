from sys import platform as p
from unittest import TestCase as TC
import getpass
import unittest

from dbg import crt_img_dbg as cid
from dbg import print_ut as put
from difi import crt as cr
from difi import de
from img import cnvrt_img_ip as cni
from img import cnvrt_img_ip_600 as cn6
from img import crt_apnm_img_cnvrt as cc
from img import get_img_dim as gid
from img import get_img_dim_h as gidw
from img import get_img_dim_w as gidh
from pth import jo as j
from pth import ncnp as n
from exc import ExceptionNotAbsolutePath as EX_NAP
from exc import ExceptionNotExistsFile as EX_NEF
from exc import ExceptionNotExistsImageFile as EX_NIMG

""" It is important to have separate folder for each unit test Python file. """

# This unit test home directory.
du = n("/home/{}").format(getpass.getuser()) # Unix.
dw = "C:\\Users\\{}".format(getpass.getuser()) # Windows.

d = du # The used directory.
if p == "cygwin" or p == "win32": d = dw # Check if this program runs in Windows platform.
dm = j(d, "dm_test_img") # Main directory for this unit test.

class unit_test(TC):
    def setUp(self):
        cr(dm, True)

    def tearDown(self):
        de(dm)

    def test_cnvrt_img_ip(self):  put("cni(...)", "PENDING: not yet unit tested")

    def test_cnvrt_img_ip_600(self):  put("cn6(...)", "PENDING: not yet unit tested")

    def test_crt_apnm_img_cnvrt(self):
        f = j(dm, "f.bmp")
        cid(f)
        cni_ = cc(f)
        put("cc(f).ap_bak", cni_.ap_bak)
        put("cc(f).ap_cn", cni_.ap_cn)
        put("cc(f).nm_bak", cni_.nm_bak)
        put("cc(f).nm_cn", cni_.nm_cn)
        de(f)

        f = j(dm, "f.jpeg")
        cid(f)
        cni_ = cc(f)
        put("cc(f).ap_bak", cni_.ap_bak)
        put("cc(f).ap_cn", cni_.ap_cn)
        put("cc(f).nm_bak", cni_.nm_bak)
        put("cc(f).nm_cn", cni_.nm_cn)
        de(f)

        f = j(dm, "f.jpg")
        cid(f)
        cni_ = cc(f)
        put("cc(f).ap_bak", cni_.ap_bak)
        put("cc(f).ap_cn", cni_.ap_cn)
        put("cc(f).nm_bak", cni_.nm_bak)
        put("cc(f).nm_cn", cni_.nm_cn)
        de(f)

        f = j(dm, "f.png")
        cid(f)
        cni_ = cc(f)
        put("cc(f).ap_bak", cni_.ap_bak)
        put("cc(f).ap_cn", cni_.ap_cn)
        put("cc(f).nm_bak", cni_.nm_bak)
        put("cc(f).nm_cn", cni_.nm_cn)
        de(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP): cc(f)

        f = j(dm, "f.bmp")
        with self.assertRaises(EX_NEF): cc(f)

        f = j(dm, "f.jpeg")
        with self.assertRaises(EX_NEF): cc(f)

        f = j(dm, "f.jpg")
        with self.assertRaises(EX_NEF): cc(f)

        f = j(dm, "f.png")
        with self.assertRaises(EX_NEF): cc(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NIMG): cc(f)
        de(f)

    def test_get_img_dim(self):
        f = j(dm, "f.bmp")
        cid(f)
        put("gid(f)", gid(f))
        de(f)

        f = j(dm, "f.jpeg")
        cid(f)
        put("gid(f)", gid(f))
        de(f)

        f = j(dm, "f.jpg")
        cid(f)
        put("gid(f)", gid(f))
        de(f)

        f = j(dm, "f.png")
        cid(f)
        put("gid(f)", gid(f))
        de(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP): gid(f)

        f = j(dm, "f.bmp")
        with self.assertRaises(EX_NEF): gid(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NIMG): gid(f)
        de(f)

    def test_get_img_dim_h(self):
        f = j(dm, "f.bmp")
        cid(f)
        put("gidh(f)", gidh(f))
        de(f)

        f = j(dm, "f.jpeg")
        cid(f)
        put("gidh(f)", gidh(f))
        de(f)

        f = j(dm, "f.jpg")
        cid(f)
        put("gidh(f)", gidh(f))
        de(f)

        f = j(dm, "f.png")
        cid(f)
        put("gidh(f)", gidh(f))
        de(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP): gidh(f)

        f = j(dm, "f.bmp")
        with self.assertRaises(EX_NEF): gidh(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NIMG): gidh(f)
        de(f)

    def test_get_img_dim_w(self):
        f = j(dm, "f.bmp")
        cid(f)
        put("gidw(f)", gidw(f))
        de(f)

        f = j(dm, "f.jpeg")
        cid(f)
        put("gidw(f)", gidw(f))
        de(f)

        f = j(dm, "f.jpg")
        cid(f)
        put("gidw(f)", gidw(f))
        de(f)

        f = j(dm, "f.png")
        cid(f)
        put("gidw(f)", gidw(f))
        de(f)

        f = n("./f.f")
        with self.assertRaises(EX_NAP): gidw(f)

        f = j(dm, "f.bmp")
        with self.assertRaises(EX_NEF): gidw(f)

        f = j(dm, "f.f")
        cr(f, False)
        with self.assertRaises(EX_NIMG): gidw(f)
        de(f)

if __name__ == "__main__": unittest.main()