from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('cryptocurrency/', include('cryptocurrencies.urls')),
    path('api/', include('cryptocurrencies_api.urls'))
]
