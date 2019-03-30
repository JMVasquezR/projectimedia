from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from app_correos.views import *

urlpatterns = [
    url(r'^registro_envio/', ContactView.as_view(), name='registro'),
    url(r'^listado_usuarios/', UsuariosViewSet.as_view(), name='listado'),
    url(r'^perfil/(?P<pk>\d+)/$', PerfilView.as_view(), name='perfil'),
    url(r'^eliminar/(?P<pk>\d+)/$', EliminarViewSet.as_view(), name='eliminar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
