import warnings

class WarningExists(Warning)         : pass
class WarningMultipleMDFiles(Warning): pass
class WarningNoMDFile(Warning)       : pass
class WarningNotExists(Warning)      : pass

def wrn_exst()  : warnings.warn("", WarningExists         , stacklevel=3)
def wrn_m_md()  : warnings.warn("", WarningMultipleMDFiles, stacklevel=3)
def wrn_n_exst(): warnings.warn("", WarningNotExists      , stacklevel=3)
def wrn_n_md()  : warnings.warn("", WarningNoMDFile       , stacklevel=3)