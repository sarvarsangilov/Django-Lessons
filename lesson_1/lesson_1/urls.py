from django.contrib import admin
from django.urls import path
from helloworld.views import hello

urlpatterns = [
    path("", hello),
    path("admin/", admin.site.urls),
]
