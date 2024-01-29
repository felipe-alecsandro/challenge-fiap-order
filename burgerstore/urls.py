from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from order.views import OrderViewSet

router = routers.DefaultRouter()
router.register('order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('order_create/', order_create, name='order_create'),
    # path('order_retrieve/<int:pk>/', order_retrieve, name='order_retrieve'),
]
