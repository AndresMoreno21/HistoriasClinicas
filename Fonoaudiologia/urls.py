from django.contrib import admin
from django.urls import path, include
from Fonoaudiologia import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fonoaudiologia_rest', views.FonoViewSet)


urlpatterns = [
	
    
	path('fonoaudiologia/',views.fono_base,name='fono-lista'),
    path('fonoaudiologia/<int:pk>/detales',views.FonoUpdate.as_view(),name='fono-update'),
    path('fonoaudiologia/crearFonoaudiologia',views.FonoCreate.as_view(),name='fono-create'),

    path('api/fonoaudiologia', include(router.urls)),

]