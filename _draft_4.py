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
def crt_nm(_ap:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if difi.chk_exst_dnd(_ap): raise exc.ExceptionExistsDirectoryInDirectory()

    pre = dttz.crt_prefix_n_ms() # Create prefix name without millisecond.
    """ For the file name, make sure to have everything in lower letter and
    to replace space with the separator.
    """
    nm_fi = pth.get_ap_innermst(_ap).lower().replace(" ", var.note_sp)
    nm = "{}{}{}".format(pre, var.note_sp, nm_fi)
    di = pth.jo(pth.get_ap_1(_ap), nm) # Absolute path into the note folder.
    fi = pth.jo(di, "{}.{}".format(nm, "md")) # Absolute path into the .md file in the note folder.

    return struct(fi=fi , di=di, nm=nm)



""" Create naming convention for original, backup, and converted file name.

PENDING: This function is not yet unit tested.
"""
def crt_nm_fi(_ap:str) -> object:
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()

    """ Original image file. """
    org_ap_1 = pth.get_ap_1(_ap)
    org = pth.get_ap_innermst(_ap)
    org_ext = pth.get_ext(org)
    org_n_ext = org.replace(".{}".format(org_ext), "")

    """ Backup image file. """
    bnm = "{}.{}".format(org, var.bak)
    bnm_ap = pth.jo(org_ap_1, bnm)

    """ Converted image file. """
    cnvrt = "{}.{}".format(org_n_ext, "png")
    cnvrt_ap = pth.jo(org_ap_1, cnvrt)

    return struct(bak_nm=bnm, bak_ap=bnm_ap, cn_nm=cnvrt, cn_ap=cnvrt_ap)



""" Function to create .md file embedded image string. The last
parameter of `_img` is used to determine if the file is an image file.
"""
def crt_nm_md(_nm_fi:str, _img:bool) -> str:
    if not bool(pth.get_ext(_nm_fi)): raise exc.ExceptionNotExistsFileExtension()

    if _img: return "![./{0}](./{0})".format(_nm_fi)
    else: return "[./{0}](./{0})".format(_nm_fi)



""" Function to get list of directories and files inside
`_ap` without any .md file.
"""
def get_lst_n_md(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.get_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()
    if difi.chk_exst_dnd(_ap): raise exc.ExceptionExistsDirectoryInDirectory()

    l = difi.get_lst(_ap)
    for i in l:
        if pth.get_ext(i) == "md": l.remove(i)

    return l



""" Function to get the absolute path to the first
.md file in `_ap` directory.
"""
def get_md(_ap:str) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.get_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if not chk_exst_md(_ap): raise exc.ExceptionNotExistsMDFile()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": return pth.jo(_ap, i)

    return ""


""" PENDING: Function to initiate the note file. """
def init(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.get_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    return True



""" Function to read lines in an .md file. """
def rd_md(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.get_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    md = open(_ap, "r")
    l = md.readlines()
    md.close()

    return l