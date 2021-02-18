# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from gathering_server.refining.serializers import RefiningCalculatorSerializer


class RefiningCalculatorView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = RefiningCalculatorSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = serializer.errors
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
