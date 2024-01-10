
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views import index, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('post/<int:id>', post_detail, name="post_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)