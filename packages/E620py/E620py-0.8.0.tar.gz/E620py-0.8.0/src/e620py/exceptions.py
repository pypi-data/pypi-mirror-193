"""
Contains exceptions used in bingus lib
"""
#* for now the exceptions are very bare bones as i have no need for them to do any extra error handling currently

class BingusException(Exception):
    """Root class for all bingus lib exceptions."""

class NoResults(BingusException):
    """Raise this exception when there are no results for a search (eg. post_get) and handle it accordingly."""

class NetworkError(BingusException):
    """Exception for any network related errors."""

class InvalidServerResponse(NetworkError):
    """Used for cases when a request is returned in non json data"""
    # and those cases will most likely be caused by me

class AuthError(BingusException):
    """Used for any authorization errors (such as not using auth for a favorites fetch)"""