from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin', admin.site.urls),
    path('api/v1/', include('api.urls')),  
    path('api/v1/', include('account.urls')),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
