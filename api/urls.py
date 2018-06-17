from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token,
)

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('bucketlists/', CreateView.as_view(), name='create'),
    path('bucketlists/<int:pk>/', DetailsView.as_view(), name='details'),
    path('jwt-token/', obtain_jwt_token),
    path('jwt-token-refresh/', refresh_jwt_token),
    path('jwt-token-verify/', verify_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)