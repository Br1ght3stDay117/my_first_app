from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index,name='index'),
        url(r'^servicios/$',views.servicios,name='servicios'),
        url(r'^contacto/$',views.contacto,name='contacto'),
        url(r'^galeria/$',views.galeria,name='galeria'),
        url(r'^acerca_de/$',views.acerca_de,name='about'),
        url(r'^iconos/$',views.iconos,name='iconos'),
        url(r'^tipografia/$',views.tipografia,name='tipografia')
]