from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from BestSite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('Women', include('user.urls')),
    path('Kids', include('user.urls')),
    path('men', include('user.urls')),
    path('model', include('user.urls')),
    path('basket',  include('user.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # path(r'^login/', include('user.urls')),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)