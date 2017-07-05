#!/bin/sh

cd ~/Downloads/pyautomation &&
python3 -B aut.py aut "/home/mikael/Dropbox/ntg/ntg-note" &&
python3 -B aut.py aut "/home/mikael/Dropbox/ntg/ntg-note-private" &&
python3 -B aut.py frmt "/home/mikael/Dropbox/ntg/ntg-note" "/home/mikael/Dropbox/ntg/mkdoc/docs" &&
python3 -B aut.py frmt "/home/mikael/Dropbox/ntg/ntg-note-private" "/home/mikael/Dropbox/ntg/mkdoc-private/docs"