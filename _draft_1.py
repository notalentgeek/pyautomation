def repair(_ap:str) -> str:
    _ap = pth.ncnp(_ap)
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if not difi.chk_exst_di(_ap): raise exc.ExceptionNotExistsDirectory()
    if chk_exst_md(_ap, True): raise exc.ExceptionExistMultipleMDFiles()
    if not chk_exst_md(_ap): raise exc.ExceptionNotExistsMDFile()
    if chk_exst_md(_ap):
        if chk_md_b(get_md(_ap)): raise exc.ExceptionMDFileNoContent()

    ap_1 = pth.get_ap_1(_ap)
    ap_innermst = pth.get_ap_innermst(_ap)

    """ Bypassing index error if the note's folder name is improper. """
    try: prefix = dttz.get_prefix(ap_innermst)
    except: pass

    print("{}{}".format("\n", "*"*50))
    print("{}: {}".format("_ap", _ap))
    print("{}: {}".format("ap_1", ap_1))
    print("{}: {}".format("ap_innermst", ap_innermst))
    print("{}: {}".format("dttz.chk_prefix(ap_innermst)", dttz.chk_prefix(ap_innermst)))

    if not dttz.chk_prefix(ap_innermst):
        nm_note = crt_apnm_note(_ap)
        difi.ren(_ap, nm_note.nm_di)

        _ap = nm_note.ap_di
        ap_1 = pth.get_ap_1(_ap)
        ap_innermst = pth.get_ap_innermst(_ap)
        prefix = dttz.get_prefix(ap_innermst)

        print("{}: {}".format("nm_note.ap_di", nm_note.ap_di))
        print("{}: {}".format("nm_note.ap_md", nm_note.ap_md))
        print("{}: {}".format("nm_note.nm_di", nm_note.nm_di))
        print("{}: {}".format("nm_note.nm_md", nm_note.nm_md))

    md = get_md(_ap)
    mdnm = "{}.{}".format(ap_innermst, "md")

    difi.ren(md, mdnm)

    md = pth.jo(_ap, mdnm)
    lines = rd_md(md)

    i = 0
    inx = 1
    print(len(lines))
    while i < len(lines):
        print("{}: {}".format("rd_md(md)[...]", lines[i]).rstrip())
        print("{}: {}".format("chk_s_md(lines[i])", chk_s_md(lines[i])))

        if chk_s_md(lines[i]) == s_type.attach or chk_s_md(lines[i]) == s_type.embed:
            nm_fi = get_fi_rp(lines[i]) # File name.
            ap_fi = pth.jo(_ap, nm_fi) # File absolute path.

            print("{}: {}".format("get_fi_rp(lines[i])", nm_fi))
            print("{}: {}".format("pth.jo(_ap, nm_fi)", ap_fi))

            """ If the attached/embedded file is not exists then quit the whole program.

            PENDING: This is not good but we will think about this later.
            """
            if not difi.chk_exst_fi(ap_fi):
                print(_ap); print(lines[i]);
                raise exc.ExceptionNotExistsFile()

            if chk_s_md(lines[i]) == s_type.attach:
                if not dttz.chk_prefix(nm_fi):
                    nm_fi = "{}-{}-{}".format(ap_innermst, inx, nm_fi)
                    difi.ren(ap_fi, nm_fi)
                    ap_fi = pth.jo(_ap, nm_fi)
                    print("="*50)
                    print("file is not properly named")
                    print("{}: {}".format("\"{}-{}-{}\".format(ap_innermst, i, nm_fi)", nm_fi))
                    print("{}: {}".format("pth.jo(_ap, nm_fi)", ap_fi))
                    print("{}: {}".format("difi.chk_exst_fi(ap_fi)", difi.chk_exst_fi(ap_fi)))
                    print("="*50)

            print("="*50)
            if chk_s_md(lines[i]) == s_type.embed:
                if not dttz.chk_prefix(nm_fi):
                    if not img.get_img_dim_w(ap_fi) == 600:

                        print("{}: {}".format("dttz.get_prefix(ap_innermst)", prefix))
                        print("PENDING: here")
                        print(nm_fi)
                        print(i)

                        enm = "{}-{}.{}".format(prefix, inx, pth.get_ext(ap_fi))
                        print(enm)
                        eap = pth.jo(_ap, enm)
                        print(eap)
                        inx = inx + 1
                        anm = "{}-{}-{}".format(prefix, inx, nm_fi)
                        print(anm)
                        aap = pth.jo(_ap, anm)
                        print(aap)
                        difi.ren(ap_fi, enm)
                        difi.cpy(eap, aap)
                        img.cnvrt_img_ip_600(eap)

                    print("image file is not properly named")
                    print("{}: {}".format("\"{}-{}-{}\".format(ap_innermst, i, nm_fi)", nm_fi))
                    print("{}: {}".format("pth.jo(_ap, nm_fi)", ap_fi))
                    print("{}: {}".format("difi.chk_exst_fi(ap_fi)", difi.chk_exst_fi(ap_fi)))
                    print("="*50)
                    """ PENDING: Add check if the image dimension is correct. """

            inx = inx + 1

        i = i + 1

    print("{}: {}".format("md", md))
    print("{}: {}".format("difi.chk_exst_fi(md)", difi.chk_exst_fi(md)))
    print("*"*50)

    return _ap