from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user_profile.views import user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('django.contrib.auth.urls')),
    path('account/', include('account.urls', namespace='account')),
    path('profile/', include('user_profile.urls', namespace='user_profile')),
    path('', include('products.urls', namespace='products')),
    path('social-auth/', include('social_django.urls', namespace='social')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
