from django.urls import path, include
from Fisioterapia import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fisioterapia_rest', views.FisioViewSet)


urlpatterns = [
	
    path('',views.base,name='base'),
	path('Fisioterapia/',views.fisio_base,name='fisio-lista'),
    path('Fisioterapia/<int:pk>/detalles',views.FisioUpdate.as_view(),name='fisio-update'),
    path('Neuropsicologia/crearHistoriaFisio',views.FisioCreate.as_view(),name='fisio-create'),

     path('api/fisioterapia', include(router.urls)),
   

]