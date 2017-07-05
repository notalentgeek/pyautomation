#!/bin/bash

cd ~/pyautomation &&

python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "project-log-personal" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "project-log" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "project-log-personal" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "project-log" "" &&

python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "brp" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "document" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "gmt+2" "cet" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "link" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "list" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "summary" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" "youtube" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "brp" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "document" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "gmt+2" "cet" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "link" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "list" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "summary" "" &&
python3 -B aut.py rr "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" "youtube" "" &&

python3 -B aut.py aut "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" &&
python3 -B aut.py aut "/home/mikael/Dropbox/notalentgeek/notalentgeek-note" &&
python3 -B aut.py aut "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private" &&
python3 -B aut.py aut "/home/mikael/Dropbox/notalentgeek/notalentgeek-note-private"