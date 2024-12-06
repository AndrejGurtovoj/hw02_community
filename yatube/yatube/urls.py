# yatube/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # импорт правил из приложения posts
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('auth/', include('django.contrib.auth.urls')),
]
