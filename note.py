import difi
import exc
import pth
import wrn
import op

""" Function to check if there are multiple .md files in `_ap`. """
def chk_m_md(_ap:str) -> bool:
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    c = 0
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": c = c + 1
    return True if c > 1 else False



""" Function to check if there is an .md file in `_ap`. """
def chk_md(_ap:str,) -> bool:
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": return True
    return False


""" Get absolute path to the first .md file. """
def get_md(_ap:str) -> str:
    l = []
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": l.append(i)
    if len(l) > 1: op.sort_lst(l)
    return pth.jo(_ap, l[0])


""" Function to initiate note. """
def init(_ap:str, _nm:str) -> bool:
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if chk_m_md(_ap)       : wrn.wrn_m_md(); return False;

    md = None
    if chk_md(_ap):
        md = get_md(_ap)
    if not chk_md(_ap):
        md = pth.jo(_ap, _nm)
        difi.crt(pth.jo(_ap, _nm), True)

    print(md)