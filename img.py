""" All codes for image manipulations. """

import subprocess

import difi
import exc
import op
import pth
import var

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
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    _w = "" if _w <= 0 else _w
    _h = "" if _h <= 0 else _h
    nm_fi = crt_apnm_img_cnvrt(_ap)
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



""" Create naming convention for original, backup, and converted file name. With
this note taking convention, the `_ap` provided here should be already be
the renamed version of the file (with prefix).
"""
def crt_apnm_img_cnvrt(_ap:str) -> object:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
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