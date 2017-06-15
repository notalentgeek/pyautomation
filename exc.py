# PENDING:  Change `ExceptionNotAbsolutePath` change `ExceptionNotAbsolutePath`.
# PENDING:  Change `ExceptionNotExistsDirectory` change `ExceptionNotExistsDirectory`.
# PENDING:  Change `ExceptionNotExistsFile` change `ExceptionNotExistsFile`.
# PENDING:  Change `ExceptionNotSamePath` change `ExceptionNotSamePath`.
# PENDING:  Change `ExceptionSamePath` change `ExceptionSamePath`.
# PENDING:  Change `WarningExists` change `ExceptionExistsDirectoryOrFile`.
# PENDING:  Change `WarningExistsDirectory` change `ExceptionExistsDirectory`.
# PENDING:  Change `WarningMultipleMDFiles` change `ExceptionExistsMultipleMDFiles`.
# PENDING:  Change `WarningNoMDFile` change `ExceptionNotExistsMDFile`.
# PENDING:  Change `WarningNotAllString` change `ExceptionListIsNotAllString`.
# PENDING:  Change `WarningNotExists` change `ExceptionNotExistsDirectoryOrFile`.
# PENDING:  Change `WarningNotMDFile` change `ExceptionNotExistsMDFile`.

class ExceptionExistMultipleMDFiles(Exception): pass
class ExceptionExistsDirectory(Exception): pass
class ExceptionExistsFile(Exception): pass
class ExceptionExistsDirectoryOrFile(Exception): pass
class ExceptionListIsNotAllString(Exception): pass
class ExceptionNotAbsolutePath(Exception): pass
class ExceptionNotExistsDirectory(Exception): pass
class ExceptionNotExistsFile(Exception): pass
class ExceptionNotExistsDirectoryOrFile(Exception): pass
class ExceptionNotExistsMDFile(Exception): pass
class ExceptionNotSamePath(Exception): pass
class ExceptionSamePath(Exception): pass