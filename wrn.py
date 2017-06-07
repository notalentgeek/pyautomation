import warnings

class WarningExists(Warning)   : pass
class WarningNotExists(Warning): pass

def wrn_exst()  : warnings.warn("", WarningExists   , stacklevel=3)
def wrn_n_exst(): warnings.warn("", WarningNotExists, stacklevel=3)