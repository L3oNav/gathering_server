
# django REST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# serializers
from gathering_server.gathering.serializers import (
    SpecCreateSerializer,
    SpecReadSerializer,
    SpecUpdateSerializer
)


class SpecCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = SpecCreateSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = serializer.errors
            return Response(response, status=status.HTTP_409_CONFLICT)

    def get(self, request):
        return Response({'hello': 'World'}, status=status.HTTP_200_OK)


class SpecReadView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {}
        data['user'] = request.user.email
        serializer = SpecReadSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = serializer.errors
            return Response(response, status=status.HTTP_409_CONFLICT)


class SpecUpdateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = SpecUpdateSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = serializer.errors
            return Response(response, status=status.HTTP_409_CONFLICT)

