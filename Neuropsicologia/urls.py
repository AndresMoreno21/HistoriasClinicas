from django.contrib import admin
from django.urls import path, include
from Neuropsicologia import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('neuropsicologia_rest', views.NeuroViewSet)


urlpatterns = [
	
    path('',views.base,name='base'),
	path('Neuropsicologia/',views.neuro_base,name='neuro-lista'),
    path('Neuropsicologia/<int:pk>/detalles',views.NeuroUpdate.as_view(),name='neuro-update'),
    path('Neuropsicologia/crearHistoriaNeuro',views.NeuroCreate.as_view(),name='neuro-create'),
   
   path('api/neuropsicologia', include(router.urls)),

]