from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='post_list'),
    path('pub/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('pub/nueva', views.nueva_pub, name='nueva_pub'),
    path('pub/<int:pk>/edita/', views.editar_pub, name='editar_pub'),
    path('borradores/', views.listar_borradores, name='listar_borradores'),
    path('pub/<int:pk>/publicar/', views.publicar_pub, name='publicar_pub'),
    path('pub/<pk>/borrar/', views.borrar_pub, name='borrar_pub'),
]