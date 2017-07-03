""" This file is for operation for directories and files. """

import os
import shutil
import unittest

import exc
import pth
import var

""" `ap` means absolute path. """

""" A function to check if a path exists. """
def chk_exst(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.exists(_ap)



""" Function to check if a path is exists and is a directory. """
def chk_exst_di(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.isdir(_ap)



""" Function to check if there is at least a directory in a directory. """
def chk_dnd(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    l = get_lst(_ap)
    for i in l:
        j = pth.jo(_ap, i)
        if chk_exst_di(j): return True
    return False



""" Function to check if a path is exists and is a file. """
def chk_exst_fi(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.isfile(_ap)



""" Function to copy a directory or a file. """
def cpy(
_ap:str,       # Source path of target directory.
_ap_trg:str,   # The target source.
_rep:bool=True # Whether this operation replace the
               # directory/file or not (if there is an existing one).
) -> bool:
    _ap = pth.ncnp(_ap)
    _ap_trg = pth.ncnp(_ap)
    if not pth.chk_ap(_ap) or not pth.chk_ap(_ap_trg): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if _ap == _ap_trg: raise exc.ExceptionSamePath()

    if _rep and chk_exst(_ap_trg): de(_ap_trg)
    elif not _rep and chk_exst(_ap_trg): return False

    """ Copy! """
    if chk_exst_di(_ap): shutil.copytree(_ap, _ap_trg); return True;
    elif chk_exst_fi(_ap) shutil.copyfile(_ap, _ap_trg); return False;

    return False



""" Function to create directory or file. """
def crt(
    _ap:str,
    _is_di:bool, # Set `True` to make a directory, set `False` to make a file.
    _rep:bool=True # Whether this operation replace the
                   # directory/file or not (if there is an existing one).
) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()

    """ If `_rep` is `True` while directory/file exists
    then delete the existing directory/file first.
    """
    if _rep and ((_is_di and chk_exst_di(_ap)) or (not _is_di and chk_exst_fi(_ap))): de(_ap)
    elif not _rep and ((_is_di and chk_exst_di(_ap)) or (not _is_di and chk_exst_fi(_ap))): return False

    """ Create directory or create file. """
    if _is_di: os.makedirs(_ap); return True; # Make directory.
    else: open(_ap, "w").close(); return True; # Make file.

    return False



""" Delete a directory or a file. """
def de(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst(_ap): return False

    """ Delete! """
    if chk_exst_di(_ap): shutil.rmtree(_ap); return True;
    elif chk_exst_fi(_ap): os.remove(_ap); return True;

    return False



""" Function to format into MKDocs directories structures. The last parameter (`_50MB`) is meant
if the formatting excluding note folder with size larger than 50 MB or not.
"""
def frmt_mkdocs(_ap:str, _50mb:bool=False) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    lst = wlk_get_note(_ap)

    """ This program need to do this from the last index. Because, if the
    upper directories changed first, the latter directories that reference
    that upper directory will not be found in the next loop.
    """
    while len(lst) > 0:
        lst_el = lst.pop() # The list element contains an absolute path
                           # to note folder.

        if _50mb:
            if get_size(lst_el) >= 50000000:
                de(lst_el) # Delete the folder.
                continue # Continue to next note folder.

        lst_el_ap1 = pth.get_ap_1(lst_el)
        content = get_lst(lst_el_ap1)

        for i in content: # Move back all files into one directory up.
            ap_i = pth.jo(lst_el, i) # File's original location.
            ap_itrg = pth.jo(lst_el_ap1, i) # File's target copy location.
            mov(ap_i, ap_itrg)

        de(lst_el)

    return True



""" Function to get all available directories
and files inside a folder (not recursive).
"""
def get_lst(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    return os.listdir(_ap)



""" Function to get size of a directory and a sub - directories. """
def get_size(_ap:str) -> int:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    tot = 0
    for i, j, k in os.walk(_ap):
        for l in k:
            apl = pth.jo(i, l)
            tot = tot + os.path.getsize(apl)

    return tot



""" Function to rename directory or file. """
def ren(
    _ap:str,
    _nm:str
) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst(_ap): raise exc.ExceptionNotExistsDirectoryOrFile()

    ap_1 = pth.get_ap_1(_ap); ap_trg = pth.jo(ap_1, _nm);

    """ Rename! """
    if _ap == ap_trg: return False # If both directory and file is the same name.
    shutil,move(_ap, _ap_trg)

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

        if lst_el_innermst_new[-1:] == var.note_sp:
            lst_el_innermst_new = lst_el_innermst_new[:-1]
        lst_el_innermst_new = lst_el_innermst_new.replace("--", "-")

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