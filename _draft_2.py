            if chk_s_md(lines[i]) == s_type.attach:
                apnm_fi = crt_apnm_attach(ap_fi, prefix, inx)
                lines[i] = "{}{}".format(crt_s_md(apnm_fi.nm, False), "\n")

            elif chk_s_md(lines[i]) == s_type.embed:
                #print(nm_fi)
                #print(ap_fi)
                #print(img.get_img_dim_w(ap_fi))
                if not img.get_img_dim_w(ap_fi) == 600 or not pth.get_ext(ap_fi) == "png":

                    apnm_img = crt_apnm_img(ap_fi, prefix, inx)
                    inx = inx + 1

                    """ Constructing sized image file for embedding and original file for attachment. """
                    difi.ren(ap_fi, apnm_img.nme) # Renaming file before converting.
                    difi.cpy(apnm_img.ape, apnm_img.apa) # This is the original file. Copied before conversion.

                    cnvrt = img.cnvrt_img_ip_600(apnm_img.ape) # Convert!

                    print(pth.get_ap_innermst(cnvrt))

                    lines[i] = "{}{}".format(crt_s_md(apnm_img.nma, False), "\n")
                    lines.insert(i, "{}{}".format(crt_s_md(pth.get_ap_innermst(cnvrt), True), "\n"))
                    i = i + 1