""" Some functions I used for debugging. """

def print_lst(_lst:list) -> None:
    for i in _lst: print(i)



def print_ut(
    _mthd:str, # Method name.
    _out:str   # Output from the method.
) -> None: print("\nmethod: {}, output: {}".format(_mthd, _out))