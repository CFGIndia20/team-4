from rest_framework.generics import (
    CreateAPIView, UpdateAPIView, DestroyAPIView,
    ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny, IsAuthenticated,
    IsAdminUser, IsAuthenticatedOrReadOnly
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from django.db.models import Q
from .serializers import (
    ComplaintDetailSerializer, ComplaintListSerializer, CategoryListSerializer
)
from botapi.models import Complaint, Category
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.decorators import api_view

class ComplaintDetailView(RetrieveAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintDetailSerializer
    permission_class = [AllowAny]
    search_fields = ['track_id', 'username', 'phonenumber','timestamp', 'location', 'description','category','category_id', 'source', 'image']

class ComplaintListView(ListAPIView):
    serializer_class  = ComplaintListSerializer
    queryset = Complaint.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['track_id', 'username', 'phonenumber','timestamp', 'location', 'description','category','category_id', 'source', 'image']
    permission_class = [AllowAny]

@api_view(['POST'])
@csrf_exempt
def postComplaint(request):
    serializer_context = {
        'request': request,
    }
    serializer = ComplaintListSerializer(data=request.data, context=serializer_context)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)