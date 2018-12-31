from django.contrib import admin
from django.urls import path,include
from PsicologiaMenores import views
from rest_framework import routers




urlpatterns = [
	
    path('',views.base,name='base'),
	path('PsicologiaMenores/',views.psicoMenor_base,name='psicoMenor-lista'),
    path('PsicologiaMenores/<int:pk>/detalles',views.PsicologiaMenorUpdate.as_view(),name='psicoMenor-update'),
    path('PsicologiaMenores/<int:pk>/eliminar',views.PsicologiaMenorDelete.as_view(),name='psicoMenor-delete'),
    path('PsicologiaMenores/crearHistoriaPsicoMenor',views.PsicologiaMenorCreate.as_view(),name='psicoMenor-create'),

   

]