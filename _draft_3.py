def crt_nm_proper(
    _nm:str, # Note name.
    _f_nm:str, # File name and not the absolute directory.
    _inx:int # File index name.
) -> str:
    return "{1}{0}{2}{0}{3}".format(var.note_sp, _nm, )

def crt_nm_proper_img(_nm:str, _inx:int, _ext:str) -> str:
    return "{1}{0}{2}.{3}".format(var.note_sp, _nm, inx, _ext)

def crt_nm_proper_n_img(_nm:str, _inx: int, _nm_fi:str) -> str:
    return "{1}{0}{2}{0}{3}".format(var.note_sp, _nm, _inx, _nm_fi)