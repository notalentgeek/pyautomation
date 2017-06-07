""" Operation for directory and file. """

import os
import shutil
import unittest

import exc
import pth
import wrn

""" `ap` refers to absolute path. """

""" Check if path is exists. """
def chk_exst(_ap:str) -> bool:
    """ Make sure the argument is an absolute path. """
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.exists(_ap)



""" Check if path is exists and is a directory. """
def chk_exst_di(_ap:str) -> bool:
    """ Make sure the argument is an absolute path. """
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.isdir(_ap)



""" Check if path is exists and is a file. """
def chk_exst_fi(_ap:str) -> bool:
    """ Make sure the argument is an absolute path. """
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    return os.path.isfile(_ap)



""" Create a directory or a file. """
def crt(
    _ap:str,
    _nm:str,      # Name of directory or file that will be made.
    _is_di:bool   # Set `True` to create directory. Set `False` to create file.
) -> bool:
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()

    """ Construct the soon - to - be created directory or file. """
    abs_pth_nm = pth.jo(_ap, _nm)

    """ If the soon - to - be create directory or file is already exists. """
    if (_is_di and chk_exst_di(abs_pth_nm)) or (not _is_di and chk_exst_fi(abs_pth_nm)):
        """ Give a warning and then return `False`. """
        wrn.wrn_exst()
        return False

    """ Create directory or create file. """
    if   _is_di: os.makedirs(abs_pth_nm);       return True
    else       : open(abs_pth_nm, "w").close(); return True

    return False



""" Copy a directory or a file. """
def cpy(
    _ap:str,       # Source path or file directory.
    _ap_trg:str,   # Target path or file directory.
    _rep:bool=True # Replace (not merge) existing duplicate at target directory.
) -> bool:
    if not pth.chk_abs(_ap) and not pth.chk_abs(_ap_trg):
        raise exc.ExceptionNotAbsolutePath()

    """ Check if the source path is an existing directory or file or not. """
    if not chk_exst(_ap_trg): wrn.wrn_n_exst(); return False;

    """ Check if both paths are the same. """
    if _ap == _ap_trg: raise exc.ExceptionSamePath()

    """ Replace the target directory or folder or nor. """
    if _rep and chk_exst(_ap_trg): del(_ap_trg)
    elif not _rep and chk_exst(_ap_trg): wrn.wrn_exst(); return False

    """ Copy! """
    if   chk_exst_di(_ap): shutil.copyfile(_ap, _ap_trg); return True
    elif chk_exst_fi(_ap): shutil.copytree(_ap, _ap_trg); return True

    return False



""" Delete a directory or a file. """
def de(_ap:str) -> bool:
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()

    """ Check if the source path is an existing directory or file or not. """
    if not chk_exst(_ap): wrn.wrn_n_exst(); return False;

    """ Delete! """
    if   chk_exst_di(_ap): shutil.rmtree(_ap); return True
    elif chk_exst_fi(_ap): os.remove(_ap);     return True

    return False



""" Move a directory or a file. """
def mov(
    _ap:str,       # Source path or file directory.
    _ap_trg:str,   # Target path or file directory.
    _rep:bool=True # Replace (not merge)
):
    if not pth.chk_abs(_ap) and not pth.chk_abs(_ap_trg):
        raise exc.ExceptionNotAbsolutePath()

    """ Check if the source path is an existing directory or file or not. """
    if not chk_exst(_ap_trg): wrn.wrn_n_exst(); return False;

    """ Check if both paths are the same. """
    if _ap == _ap_trg: raise exc.ExceptionSamePath()

    """ Replace the target directory or folder or nor. """
    if _rep and chk_exst(_ap_trg): del(_ap_trg)
    elif not _rep and chk_exst(_ap_trg): wrn.wrn_exst(); return False

    """ Move! """
    shutil.move(_ap, _ap_trg)

    return True


""" Rename a directory or a file. """
def ren(_ap:str, _nm:str) -> bool:
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()

    """ Check if the source path is an existing directory or file or not. """
    if not chk_exst(_ap_trg): wrn.wrn_n_exst(); return False;

    """ Rename! """
    ap_1   = pth.get_ap_1(_ap)
    ap_ren = pth.jo(ap_1, _nm)

    shutil.move(_ap, _ap_ren)
