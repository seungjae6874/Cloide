from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('mypage/',views.mypage,name='mypage'),
    path('intro/',views.intro,name='intro'),
    path('mycloset/',views.mycloset,name='mycloset'),
    path('update/', views.update, name="update"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)