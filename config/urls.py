"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from page.views import home_view , adaklik_view , urunlerimiz_view, post_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('adaklik/',adaklik_view, name='adaklik_view'),
    path('urunlerimiz/', urunlerimiz_view, name='urunlerimiz_view'),
    path('post/', post_view, name="post_view")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
