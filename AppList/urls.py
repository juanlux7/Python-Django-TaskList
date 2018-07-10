from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^crearTarea/$', views.crearTarea, name="crearTarea"),
    url(r'^tarea/(?P<id>\w{0,50})/$', views.borrarTarea, name="borrarTarea"),
]