"""cloide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls import  include, url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.firstpage, name='firstpage'),
    path('mage/', views.mage, name ='mage'),
    path('mage/mten', views.mten, name ='mten'),
    #path('',views.mstyle, name='mstyle'),
    path('mstyle/', views.mstyle, name = 'mstyle'),
    path('wstyle/', views.wstyle, name = 'wstyle'),
    
    path('mstyle/mage/', views.mage, name ='mage'),
    
    path('wstyle/wage/', views.wage, name ='wage'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
