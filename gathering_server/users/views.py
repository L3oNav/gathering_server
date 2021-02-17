from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src_gather.users.serializers import SignUpSerializer


class SignUpView(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = serializer.errors
            return Response(response, status=status.HTTP_409_CONFLICT)
