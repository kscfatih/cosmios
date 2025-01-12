
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# bu urls dosyası tüm url yapılarının tanımlanması gereken yer. Proje url için buraya bakar
urlpatterns = [ # bu isimlendirme özel
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    # path('api/', include('blogapp.api.urls')),
    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
