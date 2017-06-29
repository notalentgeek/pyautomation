from enum import Enum

import difi
import dttz
import exc
import img
import op
import pth
import var

class s_type(Enum): attach = 1; embed = 2; nothing = 3;

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



""" Function to check string for .md file attach or embed. """
def chk_s_md(_s:str) -> s_type:
    if _s[:4] == "![./": return s_type.embed
    if _s[:3] == "[./": return s_type.attach
    return s_type.nothing



""" Function to generate string for renaming for attaching and embedding
image file in the note directory.
"""
def crt_apnm_attach(_ap:str, _nm_note:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()

    nm = "{}-{}-{}".format(_nm_note, _inx, dttz.rm_prefix(pth.get_ap_innermst(_ap)))
    inx = _inx + 1

    """ `pth.get_ap_1(_ap)` because the `_ap` refer to the file. The absolute path used
    \in `return` should refer to the note directory.
    """
    return op.struct(ap=pth.jo(pth.get_ap_1(_ap), nm), nm=nm, inx=inx)



""" Function to generate string for copying and renaming for embedding
file in the note directory.
"""
def crt_apnm_embed(_ap:str, _nm_note:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    nm = "{}-{}.{}".format(_nm_note, _inx, pth.get_ext(_ap))
    inx = _inx + 1

    """ `pth.get_ap_1(_ap)` because the `_ap` refer to the file. The absolute path used
    \in `return` should refer to the note directory.
    """
    return op.struct(ap=pth.jo(pth.get_ap_1(_ap), nm), nm=nm, inx=inx)



""" Function to generate string for copying and renaming for attaching
file in the note directory.
"""
def crt_apnm_img(_ap:str, _nm_note:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    nm_fi = pth.get_ap_innermst(_ap)

    em = crt_apnm_embed(_ap, _nm_note, _inx)
    at = ""
    if get_s_lst(nm_fi).isnumeric(): at = "{}-{}-{}.{}".format(_nm_note, _inx, var.bak, pth.get_ext(nm_fi))
    else: at = "{}-{}-{}-{}.{}".format(_nm_note, _inx, pth.rm_ext(dttz.rm_prefix(nm_fi), pth.get_ext(nm_fi)), var.bak, pth.get_ext(nm_fi))

    return op.struct(apa=pth.jo(pth.get_ap_1(_ap), at),  ape=em.ap, nma=at, nme=em.nm, inx=_inx)



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
    nm_fi = "{}.{}".format(nm, "md") # PENDING: `nm` is actually the folder name. Fix later please.
    fi = pth.jo(di, nm_fi) # Absolute path into the .md file in the note directory.

    return op.struct(ap_di=di, ap_md=fi, nm_di=nm, nm_md=nm_fi)



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



""" Function to get file's relative position to the note folder from the
attached/embedded string in the .md file.
"""
def get_fi_rp(_s:str) -> str: return _s.split("[")[1].split("]")[0][2:]



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



""" Function to get file index number in the .md file. """
def get_s_inx(_s:str) -> int:
    try: return int(_s.split("-")[3].split(".")[0])
    except: return -1



""" Function to get last name before last note separator in a file string. """
def get_s_lst(_s:str):
    _s = pth.rm_ext(dttz.rm_prefix(_s), pth.get_ext(_s)) # No prefix.
    sl = dttz.rm_prefix(_s).split("-")
    sl = sl[len(sl) - 1]
    return sl



""" This is a function to do not initialization if
the .md file does not exists  or if .md file is blank.
"""
def init(_ap:str) -> str:
    _ap = pth.ncnp(_ap)

    print(_ap)

    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()
    if chk_exst_md(_ap):
        if not chk_md_b(get_md(_ap)): raise exc.ExceptionMDFileContent()

    nm = crt_apnm_note(_ap)
    org_di_nm = pth.get_ap_innermst(_ap)
    print("+"*50)
    print(_ap)
    print(org_di_nm)
    print("+"*50)
    org_md_nm = "{}.{}".format(org_di_nm, "md")
    org_md_ap = pth.jo(_ap, org_md_nm)

    """ Check if prefix is already in directory. """
    if not dttz.chk_prefix(org_di_nm):
        difi.ren(_ap, nm.nm_di)

        """ Set back some variables that used `_ap`. """
        _ap = pth.jo(pth.get_ap_1(_ap), nm.nm_di)
        org_di_nm = pth.get_ap_innermst(_ap)
        org_md_nm = "{}.{}".format(org_di_nm, "md")
        org_md_ap = pth.jo(_ap, org_md_nm)

    """ Check if an .md file is already exists in the note directory. """
    if not chk_exst_md(_ap): crt_md(org_md_ap)

    """ Get the .md file. """
    md = get_md(_ap) # Absolute path to the .md file.
    md_nm = pth.get_ap_innermst(md) # The name of the .md file with the extension.
    md_nmnext = pth.rm_ext(md_nm, pth.get_ext(md_nm)) # The name of the .md file without the extension.

    """ The name of .md file should be the same with the note directory.
    If the name is not the same then rename the .md file.
    """
    if not org_di_nm == md_nmnext:
        difi.ren(md, "{}.md".format(org_di_nm))

        """ Set back every parameters that use `md`. """
        md = pth.jo(_ap, "{}.md".format(org_di_nm))
        md_nm = pth.get_ap_innermst(md) # The name of the .md file with the extension.
        md_nmnext = pth.rm_ext(md_nm, "md") # The name of the .md file without the extension.

    inx = 1 # Index number for files.
    lst = [] # List of strings that will be put into `md`.
    prefix = dttz.get_prefix(org_di_nm)
    for i in get_lst_n_md(_ap):
        iap = pth.jo(_ap, i)
        iext = pth.get_ext(i)

        if pth.get_ext(i) in var.img_ext:
            apnmi = crt_apnm_img(iap, org_di_nm, inx)
            inx = apnmi.inx + 1 # PENDING: Put this into `crt_...()` function.

            """ Constructing sized image file for embedding and original file for attachment. """
            difi.ren(iap, apnmi.nme) # Renaming file before converting.
            difi.cpy(apnmi.ape, apnmi.apa) # This is the original file. Copied before conversion.

            cnvrt = img.cnvrt_img_ip_600(apnmi.ape) # Convert!

            """ The first line break is for each line itself. The next three
            line breaks are meant for empty space to write the notes.
            """

            """ Put this file into the .md file in `md`. """
            lst.append("{}{}".format(crt_s_md(pth.get_ap_innermst(cnvrt), True), "\n\n"))
            lst.append("{}{}".format(crt_s_md(apnmi.nma, False), "\n\n\n\n"))
        else:
            apnma = crt_apnm_attach(iap, org_di_nm, inx)
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



""" Function to repair note by checking each of its lines. """
def repair(_ap:str) -> str:
    _ap = pth.ncnp(_ap)

    print(_ap)

    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()
    if not chk_exst_md(_ap): raise exc.ExceptionNotExistsMDFile()
    if chk_exst_md(_ap):
        if chk_md_b(get_md(_ap)): raise exc.ExceptionMDFileNoContent()

    nm_note_folder = pth.get_ap_innermst(_ap)

    """ Check if there is prefix in the note's folder. """
    if not dttz.chk_prefix(nm_note_folder):
        st_note_folder = crt_apnm_note(_ap) # Struct name.

        """ Change the name of the note's folder. """
        difi.ren(_ap, st_note_folder.nm_di)

        """ Set back all variables that use `_ap`. """
        _ap = st_note_folder.ap_di
        nm_note_folder = pth.get_ap_innermst(_ap)

    prefix_note_folder = dttz.get_prefix(nm_note_folder)
    ap_md = get_md(_ap)
    nm_md = "{}.{}".format(nm_note_folder, "md") # .md file name. Taken
                                                 # from the note's folder.

    """ Rename the .md file directly. If the name is already
    proper then this proces goes to `except`.
    """
    try:
        difi.ren(ap_md, nm_md)
        ap_md = pth.jo(_ap, nm_md) # Get the .md file back.
    except exc.ExceptionSamePath: pass

    line_md = rd_md(ap_md) # Read the content of the .md file.

    i = 0 # Index for looping.
    inx = 1 # Index for attaching and embedding file in .md file.

    while i < len(line_md):
        if chk_s_md(line_md[i]) == s_type.attach or\
        chk_s_md(line_md[i]) == s_type.embed:
            nm_fi = get_fi_rp(line_md[i]) # File name.
            ap_fi = pth.jo(_ap, nm_fi) # Absolute path to the file.

            if not difi.chk_exst(ap_fi):
                print("note folder: {}".format(_ap))
                print("file: {}".format(ap_fi))
                raise exc.ExceptionNotExistsDirectoryOrFile()

            """ Flags. """
            fl_attach = False
            fl_embed = False
            fl_img = False
            fl_img_600 = False # If image file is 600 pixels width.
            fl_img_png = False # If image file is .png.
            fl_nm_number = False # If file named as a number (for example, 1.jpg, 1.pdf, ...).

            """ Set up flags. """
            if chk_s_md(line_md[i]) == s_type.attach: fl_attach = True
            if chk_s_md(line_md[i]) == s_type.embed:
                fl_embed = True
                if pth.get_ext(nm_fi) in var.img_ext:
                    fl_img = True
                    if img.get_img_dim_w(ap_fi) == 600: fl_img_600 = True
                    if pth.get_ext(nm_fi) == "png": fl_img_png = True
            if get_s_lst(nm_fi).isnumeric(): fl_nm_number = True

            if fl_attach and not fl_nm_number:
                """ If the file name is a number then display the index number. """
                if fl_nm_number: nm_fi_attach = "{}-{}.{}".format(nm_note_folder, inx, pth.get_ext(nm_fi))
                else: nm_fi_attach = "{}-{}-{}".format(nm_note_folder, inx, dttz.rm_prefix(nm_fi))

                """ PENDING: Stopped increasing index on back up file, because I am afraid of file
                conflict with the next file in this iteration in case the name is the same.
                """

                """ Rename the file with proper proper index number and prefix. """
                difi.ren(ap_fi, nm_fi)
                ap_fi = pth.jo(_ap, nm_fi)

                """ Make this lines back into the main list to be inputted
                to the opened .md file.
                """
                line_md[i] = "{}{}".format(crt_s_md(nm_fi, False), "\n")

            elif fl_embed: # PENDING: Please check this `if`.
                """ Only embed image file. """
                if not fl_img:
                    print(ap_fi)
                    raise exc.ExceptionNotExistsImageFile()

                if not fl_img_600 or not fl_img_png:
                    nm_fi_attach = ""
                    if fl_nm_number: nm_fi_attach = "{}-{}-{}.{}".format(nm_note_folder, inx, var.bak, pth.get_ext(nm_fi))
                    else: nm_fi_attach = "{}-{}-{}-{}.{}".format(nm_note_folder, inx, pth.rm_ext(dttz.rm_prefix(nm_fi), pth.get_ext(nm_fi)), var.bak, pth.get_ext(nm_fi))

                """ Constructing attach string for file name. """
                nm_fi = "{}-{}.{}".format(nm_note_folder, inx, pth.get_ext(nm_fi))
                if not fl_img_600 or not fl_img_png: inx = inx + 1

                """ Rename the file with proper proper index number and prefix. """
                difi.ren(ap_fi, nm_fi)
                ap_fi = pth.jo(_ap, nm_fi)

                if not fl_img_600 or not fl_img_png:
                    ap_fi_attach = pth.jo(_ap, nm_fi_attach)
                    difi.cpy(ap_fi, ap_fi_attach) # Copy into the attachment file.

                    """ Convert into .png with 600 pixels width. """
                    ap_fi_convert = img.cnvrt_img_ip_600(ap_fi)
                    nm_fi_convert = pth.get_ap_innermst(ap_fi_convert)

                    """ Put back to the lines. """
                    line_md[i] = "{}{}".format(crt_s_md(nm_fi_attach, False), "\n")
                    line_md.insert(i, "{}{}".format(crt_s_md(nm_fi_convert, True), "\n\n"))
                    i = i + 1
                else: line_md[i] = "{}{}".format(crt_s_md(nm_fi, True), "\n")

            inx = inx + 1

        i = i + 1

    line_md[len(line_md) - 1] = line_md[len(line_md) - 1].rstrip() # Remove the last line line breaks.
    wrt_md(ap_md, line_md)

    """ This line below is to debug and to show the .md file in Linux and Windows. """
    #if nm_note_folder == "20010101-0000-cet-d": import os; os.system("{} {}".format("xdg-open", ap_md))
    #if nm_note_folder == "20010101-0000-cet-d": import os; os.system(ap_md)
    #import os; os.system("{} {}".format("xdg-open", ap_md))
    #import os; os.system(ap_md);

    return _ap