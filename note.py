import difi
import dttz
import exc
import op
import pth
import wrn

def ar_md_(
    _ap:str,  # Absolute path to the .md file.
    _sl:list, # List of string.
    _m:str    # Writing mode (internal from Python's `open()`).
) -> bool:
    if not pth.chk_abs(_ap)                    : raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap)               : wrn.wrn_nt_exst();  return False;
    if not pth.get_ext(_ap) == "md"            : wrn.wrn_nt_md();    return False;
    if not all(isinstance(i, str) for i in _sl): wrn.wrn_nt_a_str(); return False;

    md = open(_ap, _m)
    for i in _sl: print(i, end="", file=md)
    md.close()

    return True

def append_md (_ap:str, _sl:list): return ar_md_(_ap, _sl , "a") # Append (add new) lines into the .md file.
def write_md  (_ap:str, _sl:list): return ar_md_(_ap, _sl , "w") # Make the .md file to be empty and then write some lines.
def write_b_md(_ap:str)          : return write_md(_ap, [""])    # Make the .md file to be empty.

""" Function to check if there are multiple .md files in `_ap`. """
def chk_exst_m_md(_ap:str) -> bool:
    if not pth.chk_abs(_ap)     : raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotDirectory()

    c = 0
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": c = c + 1
    return True if c > 1 else False



""" Function to check if there is an .md file in `_ap`. """
def chk_exst_md(_ap:str,) -> bool:
    if not pth.chk_abs(_ap)     : raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotDirectory()

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": return True
    return False



""" Function to check if the .md file is empty or not. """
def chk_md_b(_ap:str) -> bool: return True if len(read_md(_ap)) == 0 else False



""" Function to create .md file. """
def crt_md(_ap:str) -> bool:
    if not pth.chk_abs(_ap)                   : raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(pth.get_ap_1(_ap)): raise exc.ExceptionNotDirectory()
    if not pth.get_ext(_ap) == "md"           : wrn.wrn_nt_md(); return False

    difi.crt(_ap, False)
    return True



""" Get absolute path to the first .md file. """
def get_md(_ap:str) -> str:
    if not pth.chk_abs(_ap)     : raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotDirectory()

    l = []
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": l.append(i)
    if len(l) == 0: return ""                             # If there is no .md file in `_ap`
                                                          # then return a `False` string.
    if len(l) >= 1: return pth.jo(_ap, op.sort_lst(l)[0]) # If there are more than one .md
                                                          # files in `_ap` sort `l` alphabetically.


""" PENDING: Function to initiate note. """
def init(_ap:str) -> bool:
    if not pth.chk_abs(_ap)     : raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotDirectory()
    if chk_exst_m_md(_ap)       : wrn.wrn_m_md(); return False;

    p  = dttz.create_prefix_n_ms()
    md = get_md(_ap)

    """ This function split into two big ways.
    If the .md file not exist.
    If the .md file is exists but blank.
    """
    if not chk_exst_md(_ap):
        print("\n{}".format("="*50))
        print(_ap)
        print("there is no md file" if md == "" else md)
        print("md file is not exist")
        print("="*50)

        crt_md(_ap)

        return True

    elif chk_exst_md(_ap) and chk_md_b(md):
        print("\n{}".format("="*50))
        print(_ap)
        print("there is no md file" if md == "" else md)
        print("md file is exist but blank")
        print("="*50)

        return True

    else:
        print("\n{}".format("="*50))
        print(_ap)
        print("there is no md file" if md == "" else md)
        print("md file is exists but not blank")
        print("="*50)

        return False


""" Read lines in the .md file. In this case please make sure this
function only able to read from an .md file.
"""
def read_md(_ap:str) -> list:
    if not pth.chk_abs(_ap)         : raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap)    : raise exc.ExceptionNotFile()
    if not pth.get_ext(_ap) == "md" : wrn.wrn_nt_md(); return False

    md  = open(_ap, "r")
    mdl = md.readlines() # Read the content of the .md file.
    md.close()

    return mdl