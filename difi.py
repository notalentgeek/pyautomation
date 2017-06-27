""" Operation for directory and file. """

import os
import shutil
import unittest

import exc
import pth

""" `ap` refers to absolute path. """

""" Check if path is exists. """
def chk_exst(_ap:str) -> bool:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.exists(_ap)



""" Check if path is exists and is a directory. """
def chk_exst_di(_ap:str) -> bool:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.isdir(_ap)



""" Function to check if there is a directory inside a directory. """
def chk_exst_dnd(_ap:str) -> bool:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    l = get_lst(_ap)
    for i in l:
        j = pth.jo(_ap, i)
        if chk_exst_di(j): return True

    return False



""" Check if path is exists and is a file. """
def chk_exst_fi(_ap:str) -> bool:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.isfile(_ap)



""" Copy a directory or a file. """
def cpy(
    _ap:str, # Source path or file directory.
    _ap_trg:str, # Target path or file directory.
    _rep:bool=True # Replace (not merge) existing duplicate at target directory.
) -> bool:
    if not pth.chk_ap(_ap) or not pth.chk_ap(_ap_trg): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst(_ap): raise exc.ExceptionNotExistsDirectoryOrFile()
    if _ap == _ap_trg: raise exc.ExceptionSamePath()
    if _rep and chk_exst(_ap_trg): de(_ap_trg)
    elif not _rep and chk_exst(_ap_trg): return False

    """ Copy! """
    if   chk_exst_di(_ap): shutil.copytree(_ap, _ap_trg); return True;
    elif chk_exst_fi(_ap): shutil.copyfile(_ap, _ap_trg); return True;

    return False



""" Create a directory or a file. """
def crt(
    _ap:str,
    _is_di:bool # Set `True` to create directory. Set `False` to create file.
) -> bool:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if (_is_di and chk_exst_di(_ap)) or (not _is_di and chk_exst_fi(_ap)): return False

    """ Create directory or create file. """
    if _is_di: os.makedirs(_ap); return True;
    else: open(_ap, "w").close(); return True;

    return False



""" Delete a directory or a file. """
def de(_ap:str) -> bool:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst(_ap): return False

    """ Delete! """
    if chk_exst_di(_ap): shutil.rmtree(_ap); return True;
    elif chk_exst_fi(_ap): os.remove(_ap); return True;

    return False



""" Function to get list of all items (non - recursive
directories and files) from a provided absolute path.
"""
def get_lst(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    return os.listdir(_ap)



""" Function to format my personal note folder into MKDocs formatted file structures. """
def frmt_mkdocs(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()


    lst = wlk_get_note(_ap)

    """ Need to do this from last index. Because if the upper directories changed
    first it won't be found in the next loops.
    """
    while len(lst) > 0:
        lst_el = lst.pop()
        lst_el_ap_1 = pth.get_ap_1(lst_el)
        content = get_lst(lst_el)

        for i in content:
            ap_i = pth.jo(lst_el, i)
            ap_i_trg = pth.jo(lst_el_ap_1, i)
            if not chk_exst(ap_i): print(i)
            mov(ap_i, ap_i_trg)

        de(lst_el)

    return True



""" Move a directory or a file. """
def mov(
    _ap:str, # Source path or file directory.
    _ap_trg:str, # Target path or file directory.
    _rep:bool=True # Replace (not merge) existing duplicate at target directory.
) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap) or not pth.chk_ap(_ap_trg): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst(_ap): raise exc.ExceptionNotExistsDirectoryOrFile()
    if _ap == _ap_trg: raise exc.ExceptionSamePath()
    if _rep and chk_exst(_ap_trg): de(_ap_trg)
    elif not _rep and chk_exst(_ap_trg): return False

    """ Move! """
    shutil.move(_ap, _ap_trg)

    return True



""" Rename a directory or a file. """
def ren(
    _ap:str,
    _nm:str
) -> bool:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst(_ap): raise exc.ExceptionNotExistsDirectoryOrFile()
    ap_1 = pth.get_ap_1(_ap); ap_trg = pth.jo(ap_1, _nm);
    #if _ap == ap_trg: raise exc.ExceptionSamePath() # PENDING: Perhaps put warning instead as this line.
    
    if _ap == ap_trg: return False
    shutil.move(_ap, ap_trg)

    return True



""" Function to do recursive rename.

CAUTION: Be careful because if there more than 1 `_s` will also be replaced with `_s_new`.
"""
def ren_recr(_ap:str, _s:str, _s_new:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    lst = wlk_get_note(_ap)

    """ Need to do this from last index. Because if the upper directories changed
    first it won't be found in the next loops.
    """
    while len(lst) > 0:
        lst_el = lst.pop()
        lst_el_innermst = pth.get_ap_innermst(lst_el)
        lst_el_innermst_new = lst_el_innermst.replace(_s, _s_new)
        ren(lst_el, lst_el_innermst_new)

    return True



""" Walk function to go all directories in a mentioned root directory `_ap`. """
def wlk_get_note(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    lst = os.walk(_ap)
    lst_ret = []

    for i, j, k in lst:
        if ".git" in j: j.remove(".git") # Exclude .git directory.
        if not bool(j): lst_ret.append(i)

    return lst_ret



if __name__ == "__main__":
    #frmt_mkdocs("C:\\Users\\mikael\\Downloads\\notalentgeek-wiki-test")
    #ren_recr("C:\\Users\\mikael\\Downloads\\notalentgeek-wiki-test", "cet", "gmt+2")
    #ren_recr("C:\\Users\\mikael\\Downloads\\notalentgeek-wiki-test", "gmt+2", "cet")
    pass