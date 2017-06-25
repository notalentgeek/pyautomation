""" Some functions I used for debugging. """

import subprocess

import difi
import exc
import pth
import var

""" Function to create dummy image for testing purposes.

PENDING: I could may be put every ImageMagick specific functions into different Python file.
"""
def crt_img_dbg(_ap:str) -> None:
    if not pth.chk_ap(_ap): raise exc.ExceptionNotAbsolutePath()
    if difi.chk_exst_fi(_ap): raise exc.ExceptionExistsFile()
    if not pth.get_ext(_ap) in var.img_ext: raise ExceptionNotExistsImageFile()

    com = "convert -size 32x32 xc:black {}".format(_ap)
    subprocess.call(com, shell=True)



""" Function to print the contents of list in separate lines. """
def print_lst(_lst:list) -> None:
    for i in _lst: print(i)



""" Function to print result from a function used in unit test. """
def print_ut(
    _mthd:str, # Method name.
    _out:str, # Output from the method.
    _endln:bool=True # End with line break.
) -> None: print("\nmethod: {}, output: {}".format(_mthd, _out), end=(None if _endln else ""))