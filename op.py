""" Function to sort strings in a list alphabetically. """
def sort_lst(_l:list, _rev:bool=False) -> list:
    return _l.sort(key=str.lower, reverse=_rev)