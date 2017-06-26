""" `var.py` is used to hold all global variables. """

bak = "bak" # String used for all backup directory and/or file.

note_sp = "-" # Separator for note.
d_sp = "-" # Separator for date from `datetime.datetime.now()`.
t_sp = ":" # Separator for time from `datetime.datetime.now()`.

img_ext = ["bmp", "gif", "jpeg", "jpg", "png"]
opn_mode = ["a", "r+", "w"]

smpl_md = [
    "![./f1.bmp](./f1.bmp)\n\n\n\n",
    "![./f2.jpeg](./f2.jpeg)\n\n\n\n",
    "![./f3.jpg](./f3.jpg)\n\n\n\n",
    "![./f4.png](./f4.png)\n\n\n\n",
    "[./f5.fi](./f5.fi)\n\n\n\n",
    "[./f6.fi](./f6.fi)"
]

smpl_md_prefix = [
    "![./20010101-0000-cet-f1.bmp](./20010101-0000-cet-f1.bmp)\n\n\n\n",
    "![./f2.jpeg](./f2.jpeg)\n\n\n\n",
    "![./f3.jpg](./f3.jpg)\n\n\n\n",
    "![./f4.png](./f4.png)\n\n\n\n",
    "[./f5.fi](./f5.fi)\n\n\n\n",
    "[./f6.fi](./f6.fi)"
]

smpl_txt = [
    "Aenean mollis ligula quis tellus lobortis, ac luctus odio porta. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam nisl magna, fringilla a faucibus quis, pretium ut arcu. Donec orci justo, dignissim eu viverra nec, tincidunt sed metus. Integer posuere luctus faucibus. Pellentesque consectetur dictum tristique. Vestibulum varius mi quis finibus egestas. Praesent tincidunt elit eget mollis eleifend. Vivamus vel maximus risus, ut sagittis ante. Ut sollicitudin maximus ante ac semper. Sed eros nibh, maximus non maximus vitae, ullamcorper eu ex. Proin sed bibendum orci. Sed dictum tortor nec euismod luctus. Morbi a dolor tortor. Vivamus congue, lacus quis malesuada malesuada, dolor ipsum semper mauris, condimentum dignissim mi urna eget quam. Cras placerat sem tellus, facilisis euismod felis hendrerit vitae.",
    "Aenean sed laoreet nulla. Vestibulum fringilla velit nunc. Sed aliquam nulla ut dolor porttitor, nec tincidunt mi vehicula. Maecenas nibh magna, interdum in metus vel, venenatis porta nisi. Fusce sit amet fringilla diam. Duis nec molestie diam, in ornare enim. Etiam eu ligula lectus. Nullam interdum sed urna porta finibus. Aliquam tristique scelerisque gravida. Nulla aliquam tincidunt ullamcorper. Vivamus nulla massa, fermentum quis orci et, rutrum placerat felis. Vestibulum finibus ultricies massa eget ullamcorper.",
    "Curabitur pulvinar quis diam et volutpat. Nam pretium mauris a volutpat imperdiet. Quisque faucibus nec orci vitae tempus. Nam ac maximus leo. Praesent neque turpis, sodales consequat neque sit amet, rutrum condimentum mi. In sit amet velit interdum, hendrerit dui non, accumsan urna. Sed in massa eget nibh pretium gravida a in risus. Curabitur ullamcorper arcu id metus accumsan malesuada. Ut rutrum risus quis felis maximus ullamcorper. Suspendisse semper purus et mollis vulputate. Maecenas suscipit ex sed est posuere, vel dignissim eros accumsan. Aliquam erat volutpat.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus id commodo nunc. Morbi quis lectus placerat, interdum eros non, condimentum metus. Donec at feugiat lectus, in sagittis metus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Phasellus eu est ut urna egestas aliquam ut semper risus. Aliquam ipsum felis, convallis a tellus at, hendrerit molestie ipsum. Nam rhoncus justo egestas finibus placerat. Sed eu ultrices tortor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed laoreet est eget nisi fringilla, non aliquet odio interdum. Duis nibh lacus, efficitur luctus tempus at, porttitor id justo. Integer sagittis lacus felis, id vulputate ex tincidunt at. Duis ultrices congue malesuada.",
    "Phasellus laoreet libero in massa viverra commodo eget sed dolor. Cras ut mattis massa. Maecenas leo orci, tincidunt vitae quam vestibulum, sodales convallis ipsum. Praesent neque libero, dignissim nec odio nec, convallis venenatis sapien. Pellentesque ultrices varius mi, vel dapibus sem dapibus in. Nunc dapibus nisi nec mattis interdum. Praesent libero eros, vehicula sit amet tincidunt at, pretium non massa. Nam ultricies sed turpis vel molestie. Etiam placerat ipsum id est gravida feugiat. Ut semper purus diam, ut condimentum urna suscipit semper. Cras convallis tortor magna, eget egestas ante ultrices eu. Mauris et sollicitudin lacus, vitae vulputate justo. Donec ante justo, cursus in cursus eget, pellentesque nec libero. Vestibulum convallis orci non lectus ultricies pulvinar."
]