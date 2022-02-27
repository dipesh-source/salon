from django.contrib import admin
from django.urls import path, include
from adminapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view,name='loginv'),
    path('myadmin/',include('adminapp.urls')),
    path('client/',include('client.urls')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

handler404 = 'client.views.error_404_view'