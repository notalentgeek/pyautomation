from unittest import TestCase as TC
import unittest

from dbg import print_ut as put
from dttz import chk_d as cd
from dttz import chk_dm_ as cdm_
from dttz import chk_h as ch
from dttz import chk_hmns_ as chmns_
from dttz import chk_m as cm
from dttz import chk_mn as cmn
from dttz import chk_prefix as cp
from dttz import chk_s as cs
from dttz import chk_y as cy
from dttz import crt_prefix as crp
from dttz import crt_prefix as crp
from dttz import crt_prefix_n_ms as crpnms
from dttz import get_d_n as dn
from dttz import get_d_p as dp
from dttz import get_h_n as hn
from dttz import get_h_p as hp
from dttz import get_m_n as mn
from dttz import get_m_p as mp
from dttz import get_mn_n as mnn
from dttz import get_mn_p as mnp
from dttz import get_now as n
from dttz import get_now_n_ms as nnms
from dttz import get_p_ as gp
from dttz import get_prefix as gp
from dttz import get_s_n as sn
from dttz import get_tz as gtz
from dttz import get_tz_loc as gtlc
from dttz import get_y_n as yn
from dttz import get_y_p as yp
from dttz import rm_prefix as rmp

class unit_test(TC):
    def test_chk_y(self):
        self.assertFalse(cy("!@#"))
        self.assertFalse(cy("1999"))
        self.assertFalse(cy(1999))
        self.assertTrue(cy("2000"))
        self.assertTrue(cy(2000))

    def test_chk_dm_(self): put("cdm_(...)", "PENDING: not yet unit tested")

    def test_chk_d(self):
        self.assertFalse(cd("!@#"))
        self.assertFalse(cd("32"))
        self.assertFalse(cd(32))
        self.assertTrue(cd("31"))
        self.assertTrue(cd(31))

    def test_chk_m(self):
        self.assertFalse(cm("!@#"))
        self.assertFalse(cm("13"))
        self.assertFalse(cm(13))
        self.assertTrue(cm("12"))
        self.assertTrue(cm(12))

    def test_chk_hmns_(self): put("chmns_(...)", "PENDING: not yet unit tested")

    def test_chk_h(self):
        self.assertFalse(ch("24"))
        self.assertTrue(ch("0"))
        self.assertTrue(ch(0))

    def test_chk_mn(self):
        self.assertFalse(cmn("60"))
        self.assertTrue(cmn("0"))
        self.assertTrue(cmn(0))

    def test_chk_s(self):
        self.assertFalse(cs("60"))
        self.assertTrue(cs("0"))
        self.assertTrue(cs(0))

    def test_get_now(self): put("get_now()", n())

    def test_get_now_n_ms (self): put("get_now_n_ms()", nnms())

    def test_get_tz(self): put("get_tz(n())", gtz())

    def test_get_tz_loc(self):  put("gtlc(...)", "PENDING: not yet unit tested")

    def test_get_d_n(self): put("get_d_n(n())", dn(n()))

    def test_get_h_n(self): put("get_h_n(n())", hn(n()))

    def test_get_m_n(self): put("get_m_n(n())", mn(n()))

    def test_get_mn_n(self): put("get_mn_n(n())", mnn(n()))

    def test_get_s_n(self): put("get_s_n(n())", sn(n()))

    def test_get_y_n(self): put("get_y_n(n())", yn(n()))

    def test_get_p_(self):  put("gp(...)", "PENDING: not yet unit tested")

    def test_create_prefix(self): put("crt_prefix(n())", crp(n(), "cet"))

    def test_get_d_p(self): put("get_d_p(crp(n(), \"cet\"))", dp(crp(n(), "cet")))

    def test_get_h_p(self): put("get_h_p(crp(n(), \"cet\"))", hp(crp(n(), "cet")))

    def test_get_m_p(self): put("get_m_p(crp(n(), \"cet\"))", mp(crp(n(), "cet")))

    def test_get_mn_p(self): put("get_mn_p(crp(n(), \"cet\"))", mnp(crp(n(), "cet")))

    def test_get_y_p(self): put("get_y_p(crp(n(), \"cet\"))", yp(crp(n(), "cet")))

    def test_chk_prefix(self):
        self.assertFalse(cp("19990101-0000"))
        self.assertFalse(cp("asd"))
        self.assertTrue(cp("20000101-0000"))
        self.assertTrue(cp("20000101-0000-test-note"))

    def test_crt_prefix(self):  put("crp(...)", "PENDING: not yet unit tested")

    def test_crt_prefix_n_ms(self):  put("crpnms(...)", "PENDING: not yet unit tested")

    def test_get_prefix(self):  put("gp(...)", "PENDING: not yet unit tested")

    def test_rm_prefix(self): put("rmp(...)", "PENDING: not yet unit tested")

if __name__ == "__main__": unittest.main()