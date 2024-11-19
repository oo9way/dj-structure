from rest_framework.generics import GenericAPIView
from .serializers import NewLoginConfirmSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.books.models import Book

class NewLoginConfirmAPIView(GenericAPIView):
    serializer_class = NewLoginConfirmSerializer

    def post(self, request, *args, **kwargs):
        data = self.serializer_class(data=request.data, context={"request": request})
        if data.is_valid():
            response = data.save()
            return Response(response)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)



__all__ = ['NewLoginConfirmAPIView']