import difi
import dttz
import exc
import img
import op
import pth
import var

""" A super function to append and write an .md file.

`_ap` is the absolute path.
`_ls` is the string list.
`_m` is the opening mode.
"""
def aw_md_(_ap:str, _ls:list, _m:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()
    if not all(isinstance(i, str) for i in _ls): raise exc.ExceptionListNotAllString()
    if not _m in var.opn_mode: raise exc.ExceptionNotExistsOpenMode()

    md = open(_ap, _m)
    for i in _ls: print(i, end="", file=md)
    md.close()

    return True

""" Function to add `_ls` into the last line in `_ap`. """
def apnd_md(_ap:list, _ls:list): return aw_md_(_ap, _ls, "a")
""" Function to make blank `_ap` and then filled it back with `_ls`. """
def wrt_md(_ap:list, _ls:list): return aw_md_(_ap, _ls, "w")
""" Function to make blank `_ap`. """
def wrt_md_b(_ap:list): return wrt_md(_ap, [""])



""" Function to check if there is, at least, an .md file in `_ap`.

`_m` parameter meant if this function will return True only if there are at least more
than one .md files (basically to check if there are multiple .md file).
"""
def chk_exst_md(_ap:str, _m:bool=False) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    m_cntr = 0 # Counter to check for multiple .md files in `_ap`.

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md":
            if _m: m_cntr = m_cntr + 1
            else: return True
            if _m and m_cntr > 1: return True

    return False



""" Function to check if an .md file is blank/empty or not. """
def chk_md_b(_ap:str):
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    """ The function of `rd_md()` is used to read all lines in `_ap`. If it
    returns `0` it means the .md file in `_ap` has no line written in it.
    """
    return True if len(rd_md(_ap)) == 0 else False



""" Function to generate string for renaming for attaching and embedding
image file in the note directory.
"""
def crt_apnm_attach(_ap:str, _prefix:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()

    nm = "{}-{}-{}".format(_prefix, _inx, pth.get_ap_innermst(_ap))
    inx = _inx + 1

    """ `pth.get_ap_1(_ap)` because the `_ap` refer to the file. The absolute path used
    \in `return` should refer to the note directory.
    """
    return op.struct(ap=pth.jo(pth.get_ap_1(_ap), nm), nm=nm, inx=inx)



""" Function to generate string for copying and renaming for embeddeding
file in the note directory.
"""
def crt_apnm_embed(_ap:str, _prefix:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    nm = "{}-{}.{}".format(_prefix, _inx, pth.get_ext(_ap))
    inx = _inx + 1

    """ `pth.get_ap_1(_ap)` because the `_ap` refer to the file. The absolute path used
    \in `return` should refer to the note directory.
    """
    return op.struct(ap=pth.jo(pth.get_ap_1(_ap), nm), nm=nm, inx=inx)



""" Function to generate string for copying and renaming for attaching
file in the note directory.
"""
def crt_apnm_img(_ap:str, _prefix:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    inx = _inx
    em = crt_apnm_embed(_ap, _prefix, inx)
    inx = em.inx
    at = crt_apnm_attach(_ap, _prefix, inx)

    return op.struct(apa=at.ap,  ape=em.ap,nma=at.nm, nme=em.nm, inx=at.inx)



""" Function to generate string for copying and renaming for note directory. """
def crt_apnm_note(_ap:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if difi.chk_exst_dnd(_ap): raise exc.ExceptionExistsDirectoryInDirectory()

    pre = dttz.crt_prefix_n_ms("cet") # Create prefix name without millisecond.
    
    """ For the file name, make sure to have everything in lower letter and
    to replace space with the separator.
    """
    nm_fi = pth.get_ap_innermst(_ap).lower().replace(" ", var.note_sp)
    nm = "{}{}{}".format(pre, var.note_sp, nm_fi)
    di = pth.jo(pth.get_ap_1(_ap), nm) # Absolute path into the note directory.
    fi = pth.jo(di, "{}.{}".format(nm, "md")) # Absolute path into the .md file in the note directory.

    return op.struct(ap_di=di, ap_md=fi, nm_di=nm, nm_md=fi)



""" Function to create an .md file at `_ap`. There could be a check if the
.md file is alredy exists or not.
"""
def crt_md(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    return difi.crt(_ap, False)



""" Function to generate string for embedding and attaching file into the .md note. """
def crt_s_md(_nm_fi:str, _img:bool) -> str:
    if not bool(pth.get_ext(_nm_fi)): raise exc.ExceptionNotExistsFileExtension()

    if _img: return "![./{0}](./{0})".format(_nm_fi)
    else: return "[./{0}](./{0})".format(_nm_fi)



""" Function to fix space and underscore in directory/file name. """
def fix_su(_s:str) -> str:
    return _s.replace(" ", "-").replace("_", "-")



""" Function to get list of directories and files inside
`_ap` without any .md file.
"""
def get_lst_n_md(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()
    if difi.chk_exst_dnd(_ap): raise exc.ExceptionExistsDirectoryInDirectory()

    l = difi.get_lst(_ap)
    for i in l:
        if pth.get_ext(i) == "md": l.remove(i)

    return l



""" Function to get the absolute path to the first
.md file in `_ap` directory.
"""
def get_md(_ap:str) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if not chk_exst_md(_ap): raise exc.ExceptionNotExistsMDFile()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": return pth.jo(_ap, i)

    return ""



""" This is a function to do not initialization if
the .md file does not exists  or if .md file is blank.

PENDING: Please add manual time zone input as a parameter.
"""
def init(_ap:str) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()
    if chk_exst_md(_ap):
        if not chk_md_b(get_md(_ap)): raise exc.ExceptionMDFileContent()

    nm = crt_apnm_note(_ap)
    org_di_nm = pth.get_ap_innermst(_ap)
    org_md_nm = "{}.{}".format(org_di_nm, "md")
    org_md_ap = pth.jo(_ap, org_md_nm)

    """ Check if prefix is alredy in directory. """
    if not dttz.chk_prefix(org_di_nm):
        difi.ren(_ap, nm.nm_di)

        """ Set back some variables that used `_ap`. """
        _ap = nm.ap_di
        org_di_nm = pth.get_ap_innermst(_ap)
        org_md_nm = "{}.{}".format(org_di_nm, "md")
        org_md_ap = pth.jo(_ap, org_md_nm)

    """ Check if an .md file is alredy exists in the note directory. """
    if not chk_exst_md(_ap): crt_md(org_md_ap)

    """ Get the .md file. """
    md = get_md(_ap) # Absolute path to the .md file.
    md_nm = pth.get_ap_innermst(md) # The name of the .md file with the extension.
    md_nmnext = pth.rm_ext(md_nm, "md") # The name of the .md file without the extension.

    """ The name of .md file should be the same with the note directory.
    If the name is not the same then rename the .md file.
    """
    if not org_di_nm == md_nmnext:
        difi.ren(md, nm.nm_md)

        """ Set back every parameters that use `md`. """
        md = nm.ap_md
        md_nm = pth.get_ap_innermst(md) # The name of the .md file with the extension.
        md_nmnext = pth.rm_ext(md_nm) # The name of the .md file without the extension.

    inx = 1 # Index number for files.
    lst = [] # List of strings that will be put into `md`.
    prefix = dttz.crt_prefix_n_ms("cet")
    for i in get_lst_n_md(_ap):
        iap = pth.jo(_ap, i)
        iext = pth.get_ext(i)

        if pth.get_ext(i) in var.img_ext:
            apnmi = crt_apnm_img(iap, prefix, inx)
            inx = apnmi.inx

            """ Constructing sized image file for embedding and original file for attachment. """
            difi.ren(iap, apnmi.nme) # Renaming file before converting.
            difi.cpy(apnmi.ape, apnmi.apa) # This is the original file. Copied before conversion.
        
            img.cnvrt_img_ip_600(apnmi.apa) # Convert!

            """ The first line break is for each line itself. The next three
            line breaks are meant for empty space to write the notes.
            """

            """ Put this file into the .md file in `md`. """
            lst.append("{}{}".format(crt_s_md(apnmi.nme, True), "\n"))
            lst.append("{}{}".format(crt_s_md(apnmi.nma, False), "\n\n\n\n"))
        else:
            apnma = crt_apnm_attach(iap, prefix, inx)
            inx = apnma.inx

            difi.ren(iap, apnma.nm) # Renaming file before converting.
            lst.append("{}{}".format(crt_s_md(apnma.nm, False), "\n\n\n\n")) # Put this file into .md file.

    lst[len(lst) - 1] = lst[len(lst) - 1].rstrip() # Remove the last line line breaks.
    wrt_md(md, lst) # Write the `lst` into `md`.
    
    """ This line below is to debug and to show the .md file in Linux and Windows. """
    #import os; os.system("{} {}".format("xdg-open", md))
    #import os; os.system(md);

    return _ap



""" Function to read lines in an .md file. """
def rd_md(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    md = open(_ap, "r")
    l = md.readlines()
    md.close()

    return l



""" Function to repair note by checking it lines.

PENDING: Please add manual time zone input as a parameter.
"""
def repair(_ap:str) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()
    if not chk_exst_md(_ap): raise exc.ExceptionNotExistsMDFile()
    if chk_exst_md(_ap):
        if chk_md_b(get_md(_ap)): raise exc.ExceptionMDFileNoContent()

    ap_innermst = pth.get_ap_innermst(_ap)
    ap_1 = pth.get_ap_1(_ap)
    nm_note = crt_apnm_note(_ap)

    print("{}{}".format("\n", "*"*50))
    print("{}: {}".format("_ap", _ap))
    print("{}: {}".format("ap_1", ap_1))
    print("{}: {}".format("ap_innermst", ap_innermst))
    print("{}: {}".format("dttz.chk_prefix(ap_innermst)", dttz.chk_prefix(ap_innermst)))

    if not dttz.chk_prefix(ap_innermst):
        difi.ren(_ap, nm_note.nm_di)

        _ap = nm_note.ap_di
        ap_innermst = pth.get_ap_innermst(_ap)
        ap_1 = pth.get_ap_1(_ap)

        print("{}: {}".format("nm_note.ap_di", nm_note.ap_di))
        print("{}: {}".format("nm_note.ap_md", nm_note.ap_md))
        print("{}: {}".format("nm_note.nm_di", nm_note.nm_di))
        print("{}: {}".format("nm_note.nm_md", nm_note.nm_md))

    md = get_md(_ap)
    mdnm = "{}.{}".format(ap_innermst, "md")
    difi.ren(md, mdnm)
    md = pth.jo(_ap, mdnm)

    print("{}: {}".format("md", md))
    print("{}: {}".format("difi.chk_exst_fi(md)", difi.chk_exst_fi(md)))
    print("*"*50)

    return _ap