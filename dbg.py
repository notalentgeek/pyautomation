""" Some functions I used for debugging. """

""" Function to print the contents of list in separate lines. """
def print_lst(_lst:list) -> None:
    for i in _lst: print(i)



""" Function to print result from a function used in unit test. """
def print_ut(
    _mthd:str,       # Method name.
    _out:str,        # Output from the method.
    _endln:bool=True # End with line break.
) -> None: print("\nmethod: {}, output: {}".format(_mthd, _out), end=(None if _endln else ""))