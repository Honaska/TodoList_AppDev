from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import AuthToken

class SimpleTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Token '):
            return None

        token = auth_header.split('Token ')[1]

        try:
            auth_token = AuthToken.objects.get(key=token)
        except AuthToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        # You’re not tying the token to a user, so just use None
        return (None, None)

