from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from django.conf import settings
from rest_framework import exceptions


class TokenExpiredAuthantication(TokenAuthentication):
    def authenticate(self, request):
        print('I am in TokenAuthentication')
        try:
            user, token=super().authenticate(request)
            print(user, token)
        except TypeError:
            print('I am in typeErorr')
            return None
        print('I passed try except')
        token_age = (timezone.now()-token.created).seconds # (timezone.now()-token.created) is of timedelta type
        if token_age > settings.TOKEN_EXPIRED_SECONDS:
            token.delete()
            msg='Token expired. Please login again.'
            raise exceptions.AuthenticationFailed(msg)
        print(user)
        print(token)
        return user, token
    
    
