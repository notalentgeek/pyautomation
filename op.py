""" Sample struct like notion like in C/C++. I got this reference from an StackOverflow thread
(https://stackoverflow.com/questions/5943425/is-there-a-dataset-in-python-similar-to-structs-in-c).

PENDING: This is not yet unit tested. I am not sure about the mutability of this
         method just yet!
"""
class struct(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)



""" Function to convert integer/string from "1"
into "01" based on the specified length.
"""
def add_0_x(_in, _x:int) -> str:
    """ Check if `_in` is integer. If so, convert it into string. """
    if isinstance(_in, int): _i = str(_i)
    lin = len(_in); df = _x - lin;
    return _in if lin >= _x else "{}{}".format("0"*df, _in)



""" Function to check limit for both integer and string.
This function operates `1` and `"01"` as the same.
"""
def chk_limit_strint(_v, _limit_lower:int, _limit_upper:int) -> bool:
    iint = None; istr = None;
    try: iint= int(_v); istr= str(_v)
    except ValueError: return False
    listr = len(istr)

    if iint > _limit_upper or iint < _limit_lower: return False;

    return True



""" Function to sort strings in a list alphabetically. """
def sort_lst(_l:list, _rev:bool=False) -> list:
    return sorted(_l, key=str.lower, reverse=_rev)
