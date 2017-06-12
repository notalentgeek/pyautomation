import difi
import dttz
import exc
import op
import pth
import wrn

""" Function to check if there are multiple .md files in `_ap`. """
def chk_m_md(_ap:str) -> bool:
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotDirectory()
    if not pth.chk_abs(_ap)     : raise exc.ExceptionNotAbsolutePath()

    c = 0
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": c = c + 1
    return True if c > 1 else False



""" Function to check if there is an .md file in `_ap`. """
def chk_md(_ap:str,) -> bool:
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotDirectory()
    if not pth.chk_abs(_ap)     : raise exc.ExceptionNotAbsolutePath()

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": return True
    return False



""" Get absolute path to the first .md file. """
def get_md(_ap:str) -> str:
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotDirectory()
    if not pth.chk_abs(_ap)     : raise exc.ExceptionNotAbsolutePath()

    l = []
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": l.append(i)
    if len(l) == 0: return ""                             # If there is no .md file in `_ap`
                                                          # then return a `False` string.
    if len(l) >= 1: return pth.jo(_ap, op.sort_lst(l)[0]) # If there are more than one .md
                                                          # files in `_ap` sort `l` alphabetically.



""" Function to initiate note. """
def init(_ap:str) -> bool:
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotDirectory()
    if not pth.chk_abs(_ap)     : raise exc.ExceptionNotAbsolutePath()
    if chk_m_md(_ap)            : wrn.wrn_m_md(); return False;

    """ This function is split into when the .md file is exists and
    when the .md file is not exists.
    """
    if chk_md(_ap): pass
    else: pass