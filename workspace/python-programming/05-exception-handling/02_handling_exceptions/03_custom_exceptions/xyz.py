class InvalidAccessTokenError(Exception):
    """May raise InvalidAccessTokenError"""
    pass

class AccessNetwork:
    def get_token(self, access_key):
        """May raise InvalidAccessTokenError"""
        if len(access_key) < 3:
            raise InvalidAccessTokenError("Token expired")
        else:
            return "Granted"