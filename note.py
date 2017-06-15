import difi
import dttz
import exc
import op
import pth
import var

def ar_md_(
    _ap:str,  # Absolute path to the .md file.
    _sl:list, # List of string.
    _m:str    # Writing mode (internal from Python's `open()`).
) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()
    if not all(isinstance(i, str) for i in _sl): raise exc.ExceptionListIsNotAllString()

    md = open(_ap, _m)
    for i in _sl: print(i, end="", file=md)
    md.close()

    return True

def append_md(_ap:str, _sl:list): return ar_md_(_ap, _sl, "a") # Append (add new) lines into the .md file.
def write_md(_ap:str, _sl:list): return ar_md_(_ap, _sl, "w") # Make the .md file to be empty and then write some lines.
def write_b_md(_ap:str): return write_md(_ap, [""]) # Make the .md file to be empty.

""" Function to check if there are multiple .md files in `_ap`. """
def chk_exst_m_md(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    c = 0
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": c = c + 1
    return True if c > 1 else False



""" Function to check if there is an .md file in `_ap`. """
def chk_exst_md(_ap:str,) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": return True
    return False



""" Function to check if the .md file is empty or not. """
def chk_md_b(_ap:str) -> bool: _ap = pth.ncnp(_ap); return True if len(read_md(_ap)) == 0 else False



""" Function to create .md file. """
def crt_md(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(pth.get_ap_1(_ap)): raise exc.ExceptionNotExistsDirectory()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    difi.crt(_ap, False)
    return True



""" Function to create .md file name.
Set `_ret_pth` to `True` for this function to
return the path to the .md directory and file.

PENDING: Use the directory/file creation name instead
         of when this name is generated.
"""
def crt_nm(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    pre = dttz.crt_prefix_n_ms() # Create prefix.
    fod = pth.get_ap_innermst(_ap).lower().replace(" ", var.note_sp) # File or folder.
    nm = "{}{}{}".format(pre, var.note_sp, fod)
    di = pth.jo(pth.get_ap_1(_ap), nm)
    fi = pth.jo(di, "{}{}".format(nm, ".md"))

    """ Return path to directory, path to .md file, and general note name. """
    return [di, fi, nm]



""" Function to list all available files in in the `_ap`.
This function fails if there is at least a directory in `_ap`.
This function fails if there are multiple .md files.
"""
def get_lst_n_md(_ap:str) -> list:
    if not pth.chk_abs(_ap): exc.ExceptionNotAbsolutePath()
    if difi.chk_exst_di(_ap): exc.ExceptionNotExistsDirectory()
    if chk_exst_m_md(_ap): raise exc.ExceptionExistMultipleMDFiles()
    if difi.chk_exst_dnd(_ap): raise exc.ExceptionExistsDirectory()

    l = difi.get_lst(_ap)
    for i in l:
        if pth.get_ext(i) == "md": l.remove(i)

    return l




""" Get absolute path to the first .md file. """
def get_md(_ap:str) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    l = []
    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": l.append(i)
    if len(l) == 0: return "" # If there is no .md file in `_ap` then return a `False` string.
    if len(l) >= 1: return pth.jo(_ap, op.sort_lst(l)[0]) # If there are more than one .md files in `_ap` sort `l` alphabetically.



"""
PENDING: Function to initiate note.
PENDING: This function fails if there are multiple .md files.
"""
def init(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_m_md(_ap): raise exc.ExceptionExistsMultipleMDFiles()

    inmst = pth.get_ap_innermst(_ap) # Get the note folder name.
    nm = crt_nm(_ap)

    """ Check if the note folder has proper naming (check the prefix). """
    if not dttz.chk_prefix(inmst):
        difi.ren(_ap, nm[2]) # Do not forget the second argument of `difi.ren()` is the directory/file name, not the full absolute path!
        _ap =  nm[0] # Update the _ap.

    """ .md file processing.
    If the .md file is not exist.
    If the .md file is exists but blank.
    """
    if not chk_exst_md(_ap):
        """ Create the .md file. """
        md = pth.jo(_ap, "{}{}".format(nm[2], ".md"))
        crt_md(md)

        print("\n{}".format("="*50))
        print(_ap)
        print("there is no md file" if md == "" else md)
        print("md file is not exist")
        print("="*50)

        return True

    else:
        """ Get the .md file. """
        md = get_md(_ap)

        """ Check of the note folder has correct naming convention. """
        print("\n{}".format("="*50))
        if not dttz.chk_prefix(md):
            print("folder prefix convention is wrong")

        if chk_md_b(md):
            print(_ap)
            print("there is no md file" if md == "" else md)
            print("md file is exist but blank")
            print("="*50)

            return True

        else:
            print(_ap)
            print("there is no md file" if md == "" else md)
            print("md file is exists but not blank")
            print("="*50)

            return False



""" Read lines in the .md file. In this case please make sure this
function only able to read from an .md file.
"""
def read_md(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    md = open(_ap, "r")
    mdl = md.readlines() # Read the content of the .md file.
    md.close()

    return mdl