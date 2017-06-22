import subprocess

import difi
import dttz
import exc
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
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()
    if not all(isinstance(i, str) for i in _ls): raise exc.ExceptionListNotAllString()
    if not _m in var.opn_mode: raise exc.ExceptionNotExistsOpenMode()

    md = open(_ap, _m)
    for i in _ls: print(i, file=md)
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
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()

    m_cntr = 0 # Counter to check for multiple .md files in `_ap`.

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md":
            if _m: m_cntr = m_cntr + 1
            else: return True
            if _m and m_cntr > 1: return True

    return False



""" A function to convert image in place. The `ip` in this function name
stands for in position.

`_w` parameter is used to determine height.
`_h` parameter is used to determine width.
One of these parameter can be set to `0` and the other parameter will
adjust while the `0` - ed parameter will adjust in proportion.

PENDING: If later necessary please move this function into
specific ImageMagick Python file.
"""
def cnvrt_img_ip(_ap:str, _w:int=0, _h:int=0) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    _w = "" if _w <= 0 else _w
    _h = "" if _h <= 0 else _h
    nm_fi = crt_nm_img(_ap)
    difi.ren(_ap, nm_fi.nm_bak)
    _ap = nm_fi.ap_bak

    """ Convert `_ap` into `nm_fi.ap_cn`. The original `_ap` is retained. """
    com = "convert \"{}\" -resize {}x{} \"{}\"".format(_ap, _w, _h, nm_fi.ap_cn)
    subprocess.run(com, shell=True)

    """ CAUTION: Make sure to check if conversion failed (I created file with image
    extension although it is not image file per se). I only use this for debugging purposes.
    """
    if not difi.chk_exst_fi(nm_fi.ap_cn): difi.ren(_ap, nm_fi.nm_cn)
    else: difi.de(_ap) # Because ImageMagick's `convert` create a new copy of the converted
                       # image, this program needs to delete the backup file.

    return nm_fi.ap_cn

def cnvrt_img_ip_600(_ap:str) -> str: return cnvrt_img_ip(_ap, 600)



""" Function to check if an .md file is blank/empty or not. """
def chk_md_b(_ap:str):
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    """ The function of `rd_md()` is used to read all lines in `_ap`. If it
    returns `0` it means the .md file in `_ap` has no line written in it.
    """
    return True if len(rd_md(_ap)) == 0 else False



""" Function to create an .md file at `_ap`. There could be a check if the
.md file is alredy exists or not.
"""
def crt_md(_ap:str) -> bool:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    return difi.crt(_ap, False)



""" Function to create absolute path to the note, absolute path to
the note directory, and the note's name.
"""
def crt_nm(_ap:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if difi.chk_exst_dnd(_ap): raise exc.ExceptionExistsDirectoryInDirectory()

    pre = dttz.crt_prefix_n_ms("cet") # Create prefix name without millisecond.
    """ For the file name, make sure to have everything in lower letter and
    to replace space with the separator.
    """
    nm_fi = pth.get_ap_innermst(_ap).lower().replace(" ", var.note_sp)
    nm = "{}{}{}".format(pre, var.note_sp, nm_fi)
    di = pth.jo(pth.get_ap_1(_ap), nm) # Absolute path into the note folder.
    fi = pth.jo(di, "{}.{}".format(nm, "md")) # Absolute path into the .md file in the note folder.

    return op.struct(fi=fi , di=di, nm=nm)



""" Create naming convention for original, backup, and converted file name. With
this note taking convention, the `_ap` provided here should be already be
the renamed version of the file (with prefix).

PENDING: This function is not yet unit tested.
"""
def crt_nm_img(_ap:str) -> object:
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    """ Original image file. """
    org_ap1 = pth.get_ap_1(_ap)
    org = pth.get_ap_innermst(_ap)
    orge = pth.get_ext(org)
    orgne = pth.rm_ext(org, orge)

    """ Backup image file. """
    bnm = "{}_{}.{}".format(orgne, var.bak, orge)
    bnm_ap = pth.jo(org_ap1, bnm)

    """ Converted image file. """
    cnvrt = "{}.{}".format(orgne, "png")
    cnvrt_ap = pth.jo(org_ap1, cnvrt)

    return op.struct(ap_bak=bnm_ap, ap_cn=cnvrt_ap, nm_bak=bnm, nm_cn=cnvrt)



""" Function to create .md file embedded image string. The last
parameter of `_img` is used to determine if the file is an image file.
"""
def crt_nm_md(_nm_fi:str, _img:bool) -> str:
    if not bool(pth.get_ext(_nm_fi)): raise exc.ExceptionNotExistsFileExtension()

    if _img: return "![./{0}](./{0})".format(_nm_fi)
    else: return "[./{0}](./{0})".format(_nm_fi)



""" Function to get list of directories and files inside
`_ap` without any .md file.
"""
def get_lst_n_md(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
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
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if not chk_exst_md(_ap): raise exc.ExceptionNotExistsMDFile()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()

    for i in difi.get_lst(_ap):
        if pth.get_ext(i) == "md": return pth.jo(_ap, i)

    return ""


""" PENDING: Function to initiate the note file.

General note:
* Check if an .md file is exists or not.
"""
def init(_ap:str) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()

    print("\n")

    ap1 = pth.get_ap_1(_ap)
    innermst = fix_su(pth.get_ap_innermst(_ap))
    prefix = dttz.crt_prefix_n_ms("cet")

    """ PENDING: Make a function to construct note directory and note .md file name. """
    nm_di = "{}-{}".format(prefix, innermst)
    nm_fi = "{}.{}".format(nm_di, "md")
    ap_di = pth.jo(ap1, nm_di)
    ap_fi = pth.jo(ap_di, nm_fi)

    """ Check prefix in the note folder. """
    if not dttz.chk_prefix(innermst): difi.ren(_ap, nm_di); _ap = ap_di
    """ Check if there is an .md file exists in the note folder. """
    if not chk_exst_md(_ap): crt_md(ap_fi) # Create .md file.

    """ Get the .md file and check if the naming convention in the
    .md file is correct.
    """
    md = get_md(_ap) # This variable could be filled with `ap_fi` as well.
    mdi = pth.get_ap_innermst(md) # Get the .md file file name.
    if not dttz.chk_prefix(mdi): difi.ren(md, nm_fi); md = ap_fi;

    inx = 1 # File index number.
    nomd = get_lst_n_md(_ap) # All files that are not .md files.
    for i in nomd:
        iap = pth.jo(_ap, i)

        if pth.get_ext(i) in var.img_ext:
            """ PENDING: I could make this into separate function. """
            inew = "{}-{}.{}".format(prefix, inx, pth.get_ext(i)); inx = inx + 1; # Image file that will be converted and resized.
            inewap = pth.jo(_ap, inew)
            ianew = "{}-{}-{}".format(prefix, inx, i); inx = inx + 1; # Image file wihtout any conversion.
            ianewap = pth.jo(_ap, ianew)
            
            difi.ren(iap, inew)
            difi.cpy(inewap, ianewap)
            
            converted = cnvrt_img_ip_600(inewap)
            print(converted)
        else:
            """ PENDING: I could make this into separate function. """
            ianew = "{}-{}-{}".format(prefix, inx, i); inx = inx + 1;
            ianewap = pth.jo(_ap, ianew)
            difi.ren(iap, ianew)

    return _ap



""" Function to fix space and underscore in directory/file name. """
def fix_su(_s:str) -> str:
    return _s.replace(" ", "-").replace("_", "-")



""" Function to read lines in an .md file. """
def rd_md(_ap:str) -> list:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) == "md": raise exc.ExceptionNotExistsMDFile()

    md = open(_ap, "r")
    l = md.readlines()
    md.close()

    return l