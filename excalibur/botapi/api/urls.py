from django.urls import path
from botapi.api.views import (
    ComplaintDetailView, ComplaintListView, postComplaint
    )

app_name = 'botapi-api'

urlpatterns = [
    path('', ComplaintListView.as_view(), name='list'),
    path('detail/<pk>', ComplaintDetailView.as_view(), name='detail'),
    # path('post/', ComplaintList.as_view(), name='postList'),
    path('post/', postComplaint, name='postList'),
]
