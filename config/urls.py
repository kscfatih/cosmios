
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView

# bu urls dosyası tüm url yapılarının tanımlanması gereken yer. Proje url için buraya bakar
urlpatterns = [ # bu isimlendirme özel
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    # path('api/', include('blogapp.api.urls')),
    path('accounts/', include('accounts.urls')),
    path('rest-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/black-list/',TokenBlacklistView.as_view() )

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
