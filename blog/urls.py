from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='post_list'),
    path('pub/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('pub/nueva', views.nueva_pub, name='nueva_pub'),
]