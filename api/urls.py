from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 

router = routers.DefaultRouter()
router.register(r'facility', views.FacilityViewSet)
# router.register(r'review', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]