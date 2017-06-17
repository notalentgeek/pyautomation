import subprocess

import difi
import dttz
import exc
import op
import pth
import var

""" A super function to append and write an .md file.

`_ap` is the absolute path.
`_ls` is the string list.
`_m` is the opening mode.
"""
def aw_md_(_ap:str, _ls:list, _m:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()
    if not all(isinstance(i, str) for i in _ls): raise exc.ExceptionListIsNotAllString()
    if not _m in var.opn_mode: raise exc.ExceptionNotExistsOpenMode()

    md = open(_ap, _m)
    for i in _ls(): print(i, end="", file=md)
    md.close()

    return True

""" Function to add `_ls` into the last line in `_ap`. """
def apnd_md(_ap:list, _ls:list): return aw_md_(_ap, _ls, "a")
""" Function to make blank `_ap` and then filled it back with `_ls`. """
def wrt_md(_ap:list, _ls:list): return aw_md_(_ap, _ls, "w")
""" Function to make blank `_ap`. """
def wrt_md_b(_ap:list): return wrt_md(_ap, [""])



""" Function to check if there is, at least, an .md file in `_ap`.

`_m` parameter meant if this function will return True only if there are at least more
than one .md files (basically to check if there are multiple .md file).
"""
def chk_exst_md(_ap:str, _m:bool=False) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst(_ap): raise exc.ExceptionNotExistsDirectory()

    m_cntr = 0 # Counter to check for multiple .md files in `_ap`.

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md":
            if _m: m_cntr = m_cntr + 1; if m_cntr > 1: return True
            else: return True

    return False



""" PENDING: Function to do ImageMagick conversion into proper 600 pixels image. """
def cnvrt_img_600(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)

    return True



""" Function to check if an .md file is blank/empty or not. """
def chk_md_b(_ap:str):
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    """ The function of `rd_md()` is used to read all lines in `_ap`. If it
    returns `0` it means the .md file in `_ap` has no line written in it.
    """
    return True if len(rd_md(_ap)) == 0 else False



""" Function to create an .md file at `_ap`. """
def crt_md(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()
    if not difi.chk_exst_di(pth.get_ap_1(_ap)): raise exc.ExceptionNotExistsDirectory()

    return difi.crt(_ap, False)



""" Function to create absolute path to the note, absolute path to
the note directory, and the note's name.
"""
def crt_nm() ->