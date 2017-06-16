
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