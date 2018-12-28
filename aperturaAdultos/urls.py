from django.contrib import admin
from django.urls import path, include
from aperturaAdultos import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register('aperturaAdultos_rest', views.AdultosViewSet)


urlpatterns = [
	
    path('',views.base,name='base'),
	path('aperturaAdultos/',views.adultos_base,name='adulto-lista'),
    path('aperturaAdultos/<int:pk>/detalles',views.AdultoUpdate.as_view(),name='adulto-update'),
    path('aperturaAdultos/crearHistoriaAdulto',views.AdultoCreate.as_view(),name='adulto-create'),
    path('aperturaAdultos/<int:pk>/eliminar/', views.AdultoDelete.as_view(), name='adulto-delete'),
    

    path('api/aperturaAdultos', include(router.urls)),
]