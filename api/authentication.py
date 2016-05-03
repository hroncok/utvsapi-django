from django.utils.translation import ugettext_lazy as _
from rest_framework import authentication, exceptions
from utvsapitoken import TokenClient


class CtuTokenAuthentication(authentication.TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.

    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Token '.  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    '''

    def authenticate_credentials(self, key):
        c = TokenClient(check_token_uri='http://localhost:8080/token',
                        usermap_uri='http://localhost:8080/user')
        try:
            info = c.token_to_info(key)
        except:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
        return (None, info)
