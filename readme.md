# Description.
This is a set of Python script for aiding my note taking hobby. It has a function to initiate notes from loose files, repair function to automatically format files and rename files according to my own convention, a function to rename folder recursively, and a function to format the directories structure into MKDocs [http://www.mkdocs.org/](http://www.mkdocs.org/) understandable structure. There are other useful system IO (check, create, delete, and read) and path manipulation functions as well that I am pretty can be useful in my other Python project.

The function to initiate note and to repair note will be set in a function called `aut()`. This `aut()` function is meant to automatically determine if a note folder is going to be initiated or to be repaired. The function will check if there is no .md file exists in a directory or if there is an .md file but is blank then `aut()` will initiate that directory as the note directory. Initiating happen by creating an .md file and attaching/embedding all files in that directory to the .md file. Otherwise repair the note directory.

Function to do recursive naming is useful to remove unnecessary name in the directories/files. The caveat though, it will remove any strings into the newly provided string. For example to remove "a" from "asdabc", this rename function will return "sdbc" (the rename works in all "a"). Hence, this function needs to be used with caution.

MKDocs has different format with my current note directories structure. In my note directories structure a note is in a folder. Whereas, for MKDocs a note will be jumbled together other notes in a folder with many files (.md files and their attachments).

Example of my note directories structure.

* root
    * note-1
        * a.md
        * image-1.png
    * note-2
        * b.md
        * image-2-1.png
        * image-2-2.png
    * note-3
        * c.md
        * image-3.png

Example of MKDocs directories structure.

* root
    * a.md
    * image-1.png
    * b.md
    * image-2-1.png
    * image-2-2.png
    * c.md
    * image-3.png

# To - Do List.
* Change `"cet"` to become a parameter for `init()` or `repair()` functions.
    * [20170629-0239-NTG] At this point the time zone is inputted as default to `"cet"`. I want that the time zone inputted manually but as a parameter in both `init()` and `repair()`.
* Change `_snew` in `ren_recr()` to be inputted as a string or a list (or perhaps a matching dictionary or tuple).
* Create a function to check if there are less/more file between those attached/embedded in the .md file and those who are exist in the same directory with the .md file.
* Create a function to check missing attached/embedded link (recursively, but make a function to check a single folder first).
* Create a function to do indexing of all image files.
    * [20170729-0322-NTG] This method is inside `init()` and `repair()` please make it as a separate function.
* Create a function to get directory or file creation time.
* Create a function to list all available images in the note directory.
* Create a function to list all available non - images files in the note directory.
* Create a function to shorten file name.
* Make sure every file manipulations in unit test happen in sub - folder.
* Make sure to have every successful assertion happen in the end of a unit test.
* Re - factor `ren_recr()` to make it more agnostic and not only for this note naming format (please check the `....replace("--", "-")` function).
* Re - factor dttz.py and make sure to have all `chk_...()` (check function) `crt_...()` (create function) `get_...()` for all variables returned (year, month, day, ...).
* Re - factor every unit test. But, perhaps keep the pending unit test as it is.
* Re - factor note.py.
* [DONE] Create a Python file to hold all ImageMagicks related functions.
    * [20170729-0314-NTG] The file mentioned here is img.py. This file is mentioned for all image operations (although, there is one function to create debug image in dbg.py).
* [DONE] Create a function to automatically rename directories and files automatically.
* [DONE] Create a function to check .md file and automatically resize any attached and embedded files mentioned in that .md file.
* [DONE] Create a function to check if a directory or a file has a timezone pattern on its name.
* [DONE] Create a function to confirm the availability of time zone in `dttz.py`.
* [DONE] Create a function to generate absolute path and file name for both note directory and the .md file in `note.py`.
    * [20170629-0317-NTG] This need to be re - factored and make clear in regard to the format and all possible combinations.
* [DONE] Create a function to initiate an .md file with all file in the same directory if there is no .md file exists nor there is an .md file but is blank.
    * [20170629-0318-NTG] The function is `init()`. This function needs to be re - factored.
* [DONE] Create a function to recursively format the whole notes directories into MKDocs structured directories.
    * [20170629-0318-NTG] The function is `frmt_mkdocs()` in difi.py.
* [DONE] Create a function to recursively rename folder. For example from "19900101-0000-gmt+2-project-log-1" into "19900101-0000-gmt+2".
    * [20170629-0318-NTG] The function is `ren_recr()` in difi.py. Although this function are very specific to the name format (due to `....replace("--", "-")`).
* [DONE] Manage exceptions and warnings.
    * [20170629-0239-NTG] I have done it temporarily with removing all warnings and use all exceptions. It is not the best idea, but for now I will keep it that way.

## [DONE] Create a function to initiate an .md file with all file in the same directory if there is no .md file exists nor there is an .md file but is blank.
* [DONE] Create a function to check if .md file exists in a directory.
* [DONE] Create a function to check if there are multiple .md files in a directory.
* [DONE] Create a function to make and format date and time.
* [DONE] Create a function to write `![]()` and `[]()`.