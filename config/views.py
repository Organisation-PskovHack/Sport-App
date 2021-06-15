from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User


def init_user(request):
    """
    Получение пользователя по токену
    """
    user_id = Token.objects.get(key=request.headers.get("Authorization").replace("Token ", "")).user_id
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None


class BaseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'method': 'GET'})

    def post(self, request):
        return Response({'method': 'POST'})
