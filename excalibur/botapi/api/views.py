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
