
# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Serializers
from gathering_server.gathering.serializers import (
    GatheringCreateSerializer,
    GatheringListSerializer,
    GatheringListByIdSerializer,
    GatheringDeleteSerializer,
    GatheringUpdateSerializer
)


class GatheringCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializers = GatheringCreateSerializer(data=data)
        if serializers.is_valid():
            response = serializers.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = serializers.errors
            return Response(response, status=status.HTTP_409_CONFLICT)


class GatheringListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {}
        data['user'] = request.user.email
        serializer = GatheringListSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = serializer.errors
            return Response(response, status=status.HTTP_409_CONFLICT)


class GatheringByIdView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = GatheringListByIdSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = serializer.errors
            return Response(response, status=status.HTPP_409_CONFLICT)


class GatheringDeleteView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = GatheringDeleteSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = serializer.errors
            return Response(response, status=status.HTTP_409_CONFLICT)


class GatheringUpdateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = GatheringUpdateSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = serializer.errors
            return Response(response, status=status.HTTP_409_CONFLICT)
