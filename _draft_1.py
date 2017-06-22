    inx = 1
    lsnmd = get_lst_n_md(_ap) # List of all files without the.md file.
    for i in lsnmd:
        iap = pth.jo(_ap, i)

        """ PENDING: Prefix checking. """
        if not i[:len(prefix)] == prefix:


        if pth.get_ext(i) in var.img_ext:
            npa = "{}-{}-{}".format(prefix, inx, i) # Attach!
            npa_ap = pth.jo(_ap, npa)
            inx = inx + 1
            npi = "{}-{}.{}".format(prefix, inx, pth.get_ext(i)) # Show the image.
            npi_ap = pth.jo(_ap, npi)
            difi.ren(iap, npa)
            i = npa_ap
            iap = pth.jo(_ap, i)
            cnvrt_img_ip_600(iap)
            print(npa)
            print(npa_ap)
            print(npi)
            print(npi_ap)

        print(i)
        print(iap)

        inx = inx + 1

        """
        if pth.get_ext(i) in var.img_ext:
            cnvrt_img_ip_600(iap)
        """