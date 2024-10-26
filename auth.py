class Auth:
    __attrs = None
    __is_auth = False
    __is_admin = False
    def set_attrs(__attrs):
        Auth.__attrs = __attrs

    def get_attrs():
        Auth.__attrs = __attrs

    def set_is_auth():
        Auth.__is_auth = True

    def reset_is_auth():
        Auth.__is_auth = False

    def get_is_admin():
        return Auth.__is_admin