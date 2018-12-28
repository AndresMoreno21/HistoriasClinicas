from django.contrib import admin
from django.urls import path, include
from TerapiaOcupacional import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('terapiaOcupacional_rest', views.TerapiaViewSet)


urlpatterns = [
	
    
	path('terapiaOcupacional/', views.terapia_base,name='terapia-lista'),
	path('terapiaOcupacional/<int:pk>/update/', views.TerapiaUpdate.as_view(), name='terapia-update'),
	path('terapiaOcupacional/create/', views.TerapiaCreate.as_view(), name='terapia-create'),
	path('terapiaOcupacional/<int:pk>/delete/', views.TerapiaDelete.as_view(), name='terapia-delete'),

	path('api/terapiaOcupacional', include(router.urls)),

]