from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_ex.urls')),
    path('auth/', include('authe.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
