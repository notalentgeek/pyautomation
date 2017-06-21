""" Python file to help to determine date,
time, and time zone for naming convention.
"""

from tzlocal import get_localzone
import datetime
import time

import op
import var

def chk_dm_(_i, _limit_lower:int, _limit_upper:int) -> bool:
    try: return True if int(_i) > _limit_lower and int(_i) <= _limit_upper else False
    except ValueError: return False
def chk_y(_i) -> bool: # PENDING: Try to use 3rd party library.
    try: return True if int(_i) >= 2000 else False
    except ValueError: return False
def chk_d(_i) -> bool: return chk_dm_(_i, 0, 31) # PENDING: Try to use 3rd party library.
def chk_m(_i) -> bool: return chk_dm_(_i, 0, 12) # PENDING: Try to use 3rd party library.
def chk_hmns_(_v, _limit_upper:int) -> bool: return op.chk_limit_strint(_v, 0, _limit_upper)
def chk_h(_v) -> bool: return chk_hmns_(_v, 23) # PENDING: Try to use 3rd party library.
def chk_mn(_v) -> bool: return chk_hmns_(_v, 59) # PENDING: Try to use 3rd party library.
def chk_s(_v) -> bool: return chk_hmns_(_v, 59) # PENDING: Try to use 3rd party library.
def get_now() -> str: return str(datetime.datetime.now())
def get_now_n_ms() -> str: return str(get_now()).split(".")[0]
def get_tz() -> str: return str(time.tzname[0]) # Get the name of the time zone (for example: CET or CEST).
def get_tz_loc() -> str: return str(get_localzone()) # Get the location of the time zone (for example: Amsterdam).
def get_d_n(_n:str) -> str: return _n.split(" ")[0].split(var.d_sp)[2] # Get date from now.
def get_h_n(_n:str) -> str: return _n.split(" ")[1].split(var.t_sp)[0] # Get hour from now.
def get_m_n(_n:str) -> str: return _n.split(" ")[0].split(var.d_sp)[1] # Get month from now.
def get_mn_n(_n:str) -> str: return _n.split(" ")[1].split(var.t_sp)[1] # Get minute from now.
def get_s_n(_n:str) -> str: return _n.split(" ")[1].split(var.t_sp)[2].split(".")[0] # Get second from now.
def get_y_n(_n:str) -> str: return _n.split(" ")[0].split(var.d_sp)[0] # Get year from now.

""" There is no "second" in prefix. """
def get_p_(_in:str, _out:str) -> str:
    if _in == _out: return ""
    try: return _out
    except IndexError: return ""
def get_d_p(_p:str) -> str: return get_p_(_p, _p.split(var.d_sp)[0][6:8]) # Get date from prefix.
def get_h_p(_p:str) -> str: return get_p_(_p, _p.split(var.d_sp)[1][:2]) # Get hour from prefix
def get_m_p(_p:str) -> str: return get_p_(_p, _p.split(var.d_sp)[0][4:6]) # Get month from prefix.
def get_mn_p(_p:str) -> str: return get_p_(_p, _p.split(var.d_sp)[1][2:4]) # Get second from prefix
def get_y_p(_p:str) -> str: return get_p_(_p, _p.split(var.d_sp)[0][:4]) # Get year from prefix.
def chk_sp_p(_p:str) -> bool: return True if _p[8:9] == var.note_sp else False

def chk_prefix(_s:str) -> bool:
    if not chk_d(get_d_p(_s)):
        #print("chk_d: {}".format(_s))
        return False
    if not chk_h(get_h_p(_s)):
        #print("chk_h: {}".format(_s))
        return False
    if not chk_m(get_m_p(_s)):
        #print("chk_m: {}".format(_s))
        return False
    if not chk_mn(get_mn_p(_s)):
        #print("chk_mn: {}".format(_s))
        return False
    if not chk_y(get_y_p(_s)):
        #print("chk_y: {}".format(_s))
        return False
    if not chk_sp_p(_s):
        #print("chk_sp_p: {}".format(_s))
        return False
    return True
def crt_prefix(_n:str) -> str: return "{1}{2}{3}{0}{4}{5}".format(var.note_sp, get_y_n(_n), get_m_n(_n), get_d_n(_n), get_h_n(_n), get_mn_n(_n))
def crt_prefix_n_ms() -> str: return crt_prefix(get_now_n_ms())