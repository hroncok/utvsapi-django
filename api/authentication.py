from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from rest_framework import authentication, exceptions
from utvsapitoken import TokenClient


class CtuTokenAuthentication(authentication.TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.

    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Token '.  For example:

        Authorization: Token 956e252a-513c-48c5-92dd-bfddc364e812
    '''

    def authenticate_credentials(self, key):
        c = TokenClient(**getattr(settings, 'UTVSAPITOKEN', {}))
        try:
            info = c.token_to_info(key)
        except:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
        return (None, info)
