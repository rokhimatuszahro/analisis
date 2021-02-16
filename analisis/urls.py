from django.contrib import admin
from django.urls import path
from analisisSentimen.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard),
]
