def init(_ap:str) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()

    nm = crt_nm(_ap)

    """ Check prefix in the note folder. """
    if not dttz.chk_prefix(nm.nm_di): difi.ren(_ap, nm.nm_di); _ap = nm.ap_di
    """ Check if there is an .md file exists in the note folder. """
    if not chk_exst_md(_ap): crt_md(nm.ap_md) # Create .md file.

    """ Get the .md file and check if the naming convention in the
    .md file is correct.
    """
    md = get_md(_ap) # This variable could be filled with `nm.ap_md` as well.
    mdi = pth.get_ap_innermst(md) # Get the .md file file name.
    if not dttz.chk_prefix(mdi): difi.ren(md, nm.nm_md); md = nm.ap_md;

    inx = 1 # File index number.
    lst = [] # List of all lines that will be pushed into initiated .md file.
    nomd = get_lst_n_md(_ap) # All files that are not .md files.
    for i in nomd:
        iap = pth.jo(_ap, i)

        if pth.get_ext(i) in var.img_ext:
            """ PENDING: I could make this into separate function. """
            prefix = dttz.crt_prefix_n_ms("cet")
            inew = "{}-{}.{}".format(prefix, inx, pth.get_ext(i)); inx = inx + 1; # Image file that will be converted and resized.
            inewap = pth.jo(_ap, inew)
            ianew = "{}-{}-{}".format(prefix, inx, i); inx = inx + 1; # Image file wihtout any conversion.
            ianewap = pth.jo(_ap, ianew)
            
            difi.ren(iap, inew)
            difi.cpy(inewap, ianewap)
            
            cnvrt_img_ip_600(inewap)

            """ The first line break is for each line itself. The next three
            line breaks are meant for empty space to write the notes.
            """

            lst.append("{}{}".format(crt_nm_md(inew, True), "\n\n\n\n"))
            lst.append("{}{}".format(crt_nm_md(ianew, False), "\n\n\n\n"))
        else:
            """ PENDING: I could make this into separate function. """
            prefix = dttz.crt_prefix_n_ms("cet")
            ianew = "{}-{}-{}".format(prefix, inx, i); inx = inx + 1;
            ianewap = pth.jo(_ap, ianew)
            difi.ren(iap, ianew)
            lst.append("{}{}".format(crt_nm_md(ianew, False), "\n\n\n\n"))
    
    lst[len(lst) - 1] = lst[len(lst) - 1].rstrip() # Remove the last line line breaks.
    wrt_md(md, lst)
    
    """ This line below is to debug and to show the .md file in Windows. """
    #import os; os.system(md);

    return _ap