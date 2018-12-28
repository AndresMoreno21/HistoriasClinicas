from django.contrib import admin
from django.urls import path, include
from Psiquiatria import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('psiquiatria_rest', views.PsiquiatriaViewSet)


urlpatterns = [
	
    
	path('psiquiatria/', views.psiquiatria_base,name='psiquiatria-lista'),
	path('psiquiatria/<int:psiquiatria_id>/detail', views.psiquiatria_detail, name='psiquiatria-detail'),
	path('psiquiatria/<int:pk>/update/', views.PsiquiatriaUpdate.as_view(), name='psiquiatria-update'),
	path('psiquiatria/create/', views.PsiquiatriaCreate.as_view(), name='psiquiatria-create'),
	path('psiquiatria/<int:pk>/delete/', views.PsiquiatriaDelete.as_view(), name='psiquiatria-delete'),

	path('api/psiquiatria', include(router.urls)),

]