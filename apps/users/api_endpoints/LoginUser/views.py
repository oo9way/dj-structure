from rest_framework.generics import GenericAPIView
from .serializers import LoginUserSerializer
from rest_framework.response import Response
from rest_framework import status

class UserLoginAPIView(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        data = self.serializer_class(data=request.data, context={"request": request})
        if data.is_valid():
            response = data.save()
            return Response(response)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)



__all__ = ['UserLoginAPIView']