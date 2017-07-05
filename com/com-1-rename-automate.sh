#!/bin/bash

cd ~/pyautomation &&

python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "project-log-personal" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "project-log" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "project-log-personal" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "project-log" "" &&

python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "brp" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "document" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "gmt+2" "cet" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "link" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "list" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "summary" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note" "youtube" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "brp" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "document" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "gmt+2" "cet" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "link" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "list" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "summary" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/ntg/ntg-note-private" "youtube" "" &&

python3 -B aut.py aut "/home/mikael/Dropbox/ntg/ntg-note" &&
python3 -B aut.py aut "/home/mikael/Dropbox/ntg/ntg-note" &&
python3 -B aut.py aut "/home/mikael/Dropbox/ntg/ntg-note-private" &&
python3 -B aut.py aut "/home/mikael/Dropbox/ntg/ntg-note-private"