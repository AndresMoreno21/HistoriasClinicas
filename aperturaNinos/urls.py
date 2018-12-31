from django.contrib import admin
from django.urls import path, include
from aperturaNinos import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('aperturaNiños_rest', views.NiñoViewSet)


urlpatterns = [
	
    #path('',views.base,name='bienvenida'),
	path('aperturaNino/',views.niños_base, name='nino-lista'),
    path('aperturaNino/<int:pk>/detalles',views.NiñoUpdate.as_view(),name='nino-update'),
    path('aperturaNino/crearHistoriaMenor',views.NiñoCreate.as_view(),name='nino-create'),
    path('aperturaNino/<int:pk>/eliminarHistoriaMenor',views.NiñoDelete.as_view(),name='nino-delete'),
    

    path('api/aperturaNiños', include(router.urls)),

]