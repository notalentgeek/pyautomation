from   sys import platform
import os
import exc

"""
`chk` refers to "check".
`ap`  refers to absolute path.
`sp`  refers to system separator. "/" in Unix or "\" in Windows.
"""

""" This is a function to check if a provided path is an absolute path or a
relative path.
"""
def chk_abs(_p:str) -> bool: return os.path.isabs(ncnp(_p))



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


""" Get the innermost directory or file from the provided path. """
def get_ap_innermst(_ap:str) -> str:
    if not chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.basename(_ap)



""" Get one upped path from the provided path. n"""
def get_ap_1(_ap:str) -> str:
    if not chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()

    if len(_ap) == 1: return get_sp()        # If `_ap` is the root directory then
                                             # return the separator.

    ap = rm_sp_lst(_ap)                      # Remove the last separator (for example,
                                             # from `/home/user/` into `/home/user`).
    ap = ap.replace(get_ap_innermst(ap), "") # Erase the innermost directory or file.

    return (get_sp() if len(rm_sp_lst(ap)) == 1 else rm_sp_lst(ap))



""" Get `x` upped path from the provided path. """
def get_ap_x(
    _ap:str,
    _x:int,
    _c:int=0 # Counter parameter, but usually should
             # never be provided and left 0.
) -> str:
    if not chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()

    c  = _c + 1
    di = get_ap_1(_ap)

    """ If `di` is only a character then return `di` itself. """
    if len(di) == 1: return di

    """ Keep recursing if `c` is not yet equal `_x`. """
    if   _x == c: return di
    else        : return get_ap_x(di, _x, c)



""" Get the system separator. """
def get_sp() -> str:
    if   platform == "darwin" or platform == "linux" or platform == "linux2": return "/"
    elif platform == "cygwin" or platform == "win32"                        : return "\\"
    else                                                                    : return ""



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



""" Remove the last appending system separator in a supplied path. """
def rm_sp_fst(_ap:str) -> str:
    if _ap[:1] == get_sp() and len(_ap) > 1: return _ap[1:]
    else: return _ap



""" Remove the last appending system separator in a supplied path. """
def rm_sp_lst(_ap:str) -> str:
    if _ap[-1:] == get_sp() and len(_ap) > 1: return _ap[:-1]
    else: return _ap