from sys import platform
import os
import exc
import var

"""
`chk` refers to "check".
`ap` refers to absolute path.
`sp` refers to system separator. "/" in Unix or "\" in Windows.
"""

""" This is a function to check if a provided path is an absolute path or a
relative path.
"""
def chk_abs(_p:str) -> bool: return os.path.isabs(ncnp(_p))



""" Function to check if a file name is an image file. """
def chk_ext_img(_s:str) -> bool:
    if not bool(get_ext(_s)): raise exc.ExceptionNotExistsFileExtension()
    if get_ext(_s) in var.img_ext: return True

    return False



""" This function is to check if two one upped absolute paths are the same
or not.
"""
def chk_s_ap_1(_ap_1:str, _ap_2:str) -> bool:
    if not chk_abs(_ap_1) or not chk_abs(_ap_2): raise exc.ExceptionNotAbsolutePath()
    return ncnp(get_ap_1(_ap_1)) == ncnp(get_ap_1(_ap_2))



""" This function is to check if two `x` upped absolute paths are the same
or not.
"""
def chk_s_ap_x(_ap_1:str, _ap_2:str, _x:int) -> bool:
    if not chk_abs(_ap_1) or not chk_abs(_ap_2): raise exc.ExceptionNotAbsolutePath()
    return ncnp(get_ap_x(_ap_1, _x)) == ncnp(get_ap_x(_ap_2, _x))



""" Get one upped path from the provided path. n"""
def get_ap_1(_ap:str) -> str:
    if not chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()

    if len(_ap) == 1: return get_sp() # If `_ap` is the root directory then return the separator.

    ap = rm_sp_lst(_ap) # Remove the last separator (for example, from `/home/user/` into `/home/user`).
    el = get_ap_innermst(ap)
    el = len(el) + 1 # Determine how long we need to erase the characters from behind.
    ap = ap[:-el] # Erase the innermost directory or file.

    return (get_sp() if len(rm_sp_lst(ap)) == 1 else rm_sp_lst(ap))



""" Get `x` upped path from the provided path. """
def get_ap_x(
    _ap:str,
    _x:int,
    _c:int=0 # Counter parameter, but usually should never be provided and left 0.
) -> str:
    if not chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()

    c = _c + 1
    di = get_ap_1(_ap)

    """ If `di` is only a character then return `di` itself. """
    if len(di) == 1: return di

    """ Keep recursing if `c` is not yet equal `_x`. """
    if _x == c: return di
    else: return get_ap_x(di, _x, c)



""" Get the innermost directory or file from the provided path. """
def get_ap_innermst(_ap:str) -> str:
    if not chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.basename(_ap)



""" Function to get file extension. """
def get_ext(_p:str) -> str:
    ext = os.path.splitext(_p)[1]
    return ext[1:] if len(ext) > 1 else ""



""" Function to get filename without the extension. """
def get_no_ext(_s:str):
    if not bool(get_ext(_s)): return _s # If there is no extension then return `_s` back.
    s_ext = get_ext(_s)

    return _s.replace(".{}".format(s_ext), "")



""" Get the system separator. """
def get_sp() -> str:
    if platform == "darwin" or platform == "linux" or platform == "linux2": return "/"
    elif platform == "cygwin" or platform == "win32": return "\\"
    else: return ""



""" Function to join two paths. """
def jo(_ap:str, _p:str) -> str:
    if not chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()

    """ If there is a system separator as the first character then remove it.
    System separator at the first character ruins `os.path.join()`.
    """
    _p = rm_sp_fst(_p)

    return ncnp(os.path.join(_ap, _p))



""" Function to normalize path according operating system's convention. """
def ncnp(_ap:str) -> str:
    return os.path.normcase(os.path.normpath(_ap))



""" Function to remove file extension. Please put the extension
without the ".". For example, please input ".jpg" as just "jpg".


PENDING: This function is not yet unit tested.
"""
def rm_ext(_s:str, _ext:str) -> str:
    if not bool(get_ext(_s)): raise exc.ExceptionNotExistsFileExtension()
    return _s.replace(".{}".format(_ext), "")

def rm_ext_bak(_s:str) -> str: return rm_ext(_s, "bak")
def rm_ext_md(_s:str) -> str: return rm_ext(_s, "md")



""" Remove the last appending system separator in a supplied path. """
def rm_sp_fst(_ap:str) -> str:
    if _ap[:1] == get_sp() and len(_ap) > 1: return _ap[1:]
    else: return _ap



""" Remove the last appending system separator in a supplied path. """
def rm_sp_lst(_ap:str) -> str:
    if _ap[-1:] == get_sp() and len(_ap) > 1: return _ap[:-1]
    else: return _ap