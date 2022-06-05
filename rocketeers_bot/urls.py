from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('vk_bot/', include('vk_bot.urls')),
    path('admin/', admin.site.urls),
]
