"""
URL configuration for celebrity_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path
from celebrities.views import celebrity_list, detayl_celeb, create_celeb
from celebrities import views
from users.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', celebrity_list),
    path('celebrity/', views.celebrity_list),
    path('celebrity/<int:id>/', detayl_celeb, name='detail_celeb'),
    path('celebrity/create/', views.create_celeb),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


