""" aut
Usage:
    aut.py (--help)
    aut.py (--version)
    aut.py aut <ap>
    aut.py frmt <ap> <ap_trg>
    aut.py rr <ap> <s> <snew>

Options:
    <ap> Absolute path.
    <ap_trg> Target absolute path.
    <s> String.
    <sn> New string.
    aut Automate note directories with `init()` or `repair()`.
    frmt Format file structure to MKDocs file structure.
    rr Recursive renaming.
"""
from docopt import docopt

import difi
import dttz
import exc
import note
import pth
import var

def aut(_ap:str) -> bool:
    lst = difi.wlk_get_note(_ap)

    for i in lst:
        if note.chk_exst_md(i, True):
            print(i)
            raise exc.ExceptionExistMultipleMDFiles()
        if note.chk_exst_md(i):
            md = note.get_md(i)
            if note.chk_md_b(md): note.init(i)
            else: note.repair(i)
        else: note.init(i)

    return True

if __name__ == "__main__":
    doc = docopt(__doc__, version="0.0.1")

    automate = doc["aut"]
    frmt = doc["frmt"]
    rr = doc["rr"]

    ap = doc["<ap>"]
    ap_trg = doc["<ap_trg>"]
    s = doc["<s>"]
    snew = doc["<snew>"]

    """ Create a backup directory or file for automating and renaming. """
    if automate or rr:
        """ Make a backup copy first. """
        nm_di = pth.get_ap_innermst(ap)
        ap_1_di = pth.get_ap_1(ap)
        nm_bk = "{}_{}_{}".format(nm_di, dttz.get_now_n_ms(), var.bak)
        ap_bk = pth.jo(ap_1_di, nm_bk)
        difi.cpy(ap, ap_bk)

    """ Creating backup directory or file for formating file
    structures into MKDocs.
    """
    if frmt:
        """ Make a backup copy first. """
        nm_di = pth.get_ap_innermst(ap)
        ap_1_di = pth.get_ap_1(ap)
        nm_bk = "{}_{}_{}".format(nm_di, dttz.get_now_n_ms(), "note")
        ap_note = pth.jo(ap_1_di, nm_bk)
        difi.cpy(ap, ap_note)

    if frmt:
        difi.frmt_mkdocs(ap_note) # For format please format the backup folder.
        difi.ren(ap_note, "note")
        ap_note = pth.jo(pth.get_ap_1(ap_note), "note")
        difi.mov(ap_note, pth.jo(ap_trg, "note"))
    if automate: aut(ap)
    if rr: difi.ren_recr(ap, s, snew)