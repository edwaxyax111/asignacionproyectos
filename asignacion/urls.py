from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'^$', views.post_list),
    url(r'^$', views.proyecto_lista, name='proyecto_lista'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,  name='post_detail'),
    url(r'^proyecto/(?P<pk>[0-9]+)/$', views.proyecto_detalle, name='proyecto_detalle'),
    url(r'^proyecto/nuevo/$', views.proyecto_nuevo, name='proyecto_nuevo'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^proyecto/(?P<pk>[0-9]+)/editar/$', views.proyecto_editar, name='proyecto_editar'),
    #url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    #url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    #url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^proyecto/(?P<pk>\d+)/remover/$', views.proyecto_remover, name='proyecto_remover'),
    #visttas de empleados
    url(r'^empleado/lista/$', views.empleado_lista, name='empleado_lista'),
    url(r'^empleado/(?P<pk>[0-9]+)/$', views.empleado_detalle, name='empleado_detalle'),
    url(r'^empleado/nuevo/$', views.empleado_nuevo, name='empleado_nuevo'),
    url(r'^empleado/(?P<pk>[0-9]+)/editar/$', views.empleado_editar, name='empleado_editar'),
    url(r'^empleado/(?P<pk>\d+)/remover/$', views.empleado_remover, name='empleado_remover'),

]
