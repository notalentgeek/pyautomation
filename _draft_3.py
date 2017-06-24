""" Function to make strings to attach file into the `.md` file. """
def create_apnm_attach(_ap:str, _prefix:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs_pth(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()

    nm = "{}-{}-{}".format(_prefix, _inx, pth.get_ap_innermst(_ap))
    inx = _inx + 1

    return op.struct(ap=pth.jo(_ap, nm), nm=nm, inx=inx)

""" Function to generate embed strings for file. At this point only images are allowed to be
embedded in the .md note.
"""
def create_apnm_embed(_ap:str, _prefix:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs_pth(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    nm = "{}-{}.{}".format(_prefix, _inx, pth.get_ext(_ap))
    inx = _inx + 1

    return op.struct(ap=pth.jo(_ap,nm), nm=nm, inx=inx)

""" Function to both generate strings for embed then attach image file. """
def create_apnm_image(_ap:str, _prefix:str, _inx:str) -> object:
    _ap = pth.ncnp(_ap)
    if not pth.chk_abs_pth(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_fi(_ap): raise exc.ExceptionNotExistsFile()
    if not bool(pth.get_ext(_ap)): raise exc.ExceptionNotExistsFileExtension()
    if not pth.get_ext(_ap) in var.img_ext: raise exc.ExceptionNotExistsImageFile()

    inx = _inx
    em = create_apnm_embed(_ap, _prefix, inx)
    inx = em.inx
    at = create_apnm_attach(_ap, _prefix, inx)

    return op.struct(apa=at.ap,ape=em.ap,nma=at.nm,nme=em.nm,inx=at.inx)