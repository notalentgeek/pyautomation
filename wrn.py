import warnings

class WarningExists(Warning)         : pass
class WarningMultipleMDFiles(Warning): pass
class WarningNoMDFile(Warning)       : pass
class WarningNotAllString(Warning)   : pass
class WarningNotExists(Warning)      : pass
class WarningNotMDFile(Warning)      : pass

def wrn_exst()    : warnings.warn("", WarningExists         , stacklevel=3)
def wrn_m_md()    : warnings.warn("", WarningMultipleMDFiles, stacklevel=3)
def wrn_n_md()    : warnings.warn("", WarningNoMDFile       , stacklevel=3)
def wrn_nt_a_str(): warnings.warn("", WarningNotAllString   , stacklevel=3)
def wrn_nt_exst() : warnings.warn("", WarningNotExists      , stacklevel=3)
def wrn_nt_md()   : warnings.warn("", WarningNotMDFile      , stacklevel=3)