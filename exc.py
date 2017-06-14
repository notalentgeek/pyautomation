class ExceptionNotAbsolutePath(Exception): pass
class ExceptionNotDirectory(Exception): pass # Also used if the is not directory exist.
class ExceptionNotFile(Exception): pass # Also used if the is not file exist.
class ExceptionNotSamePath(Exception): pass
class ExceptionSamePath(Exception): pass