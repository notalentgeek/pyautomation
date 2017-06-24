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



""" Move a directory or a file. """
def mov(
    _ap:str, # Source path or file directory.
    _ap_trg:str, # Target path or file directory.
    _rep:bool=True # Replace (not merge) existing duplicate at target directory.
) -> bool:
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
    _nm:str,
    _rep:bool=True # Replace (not merge) existing duplicate at target directory.
) -> bool:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not chk_exst(_ap): raise exc.ExceptionNotExistsDirectoryOrFile()
    ap_1 = pth.get_ap_1(_ap); ap_trg = pth.jo(ap_1, _nm)
    if _ap == ap_trg: raise exc.ExceptionSamePath()
    if _rep and chk_exst(ap_trg): de(ap_trg)
    elif not _rep and chk_exst(ap_trg): return False

    shutil.move(_ap, ap_trg)

    return True
