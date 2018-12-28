from django.contrib import admin
from django.urls import path,include
from Psicologia import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('psicologia_rest', views.PsicoViewSet)


urlpatterns = [
	
  
	path('Psicologia/',views.psico_base,name='psico-lista'),
    path('Psicologia/<int:pk>/detalles',views.PsicologiaUpdate.as_view(),name='psico-update'),
    path('Psicologia/crearHistoriaPsico',views.PsicologiaCreate.as_view(),name='psico-create'),
    

    path('api/psicologia', include(router.urls)),
   

]