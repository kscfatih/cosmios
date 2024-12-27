
from django.contrib import admin
from django.urls import path, include
# bu urls dosyası tüm url yapılarının tanımlanması gereken yer. Proje url için buraya bakar
urlpatterns = [ # bu isimlendirme özel
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls'))
]
