from django.contrib import admin
from django.urls import path
from Access01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
]
