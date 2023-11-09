from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from blog import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'tasks',views.postTableview,'blog')
router.register(r'tvseries',views.tvtableview,'blog')
router.register(r'register',views.registerformview,'blog')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
