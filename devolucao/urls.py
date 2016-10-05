from django.conf.urls import url
from django.conf import settings
from devolucao.views import *

urlpatterns = [
	url(r'^$',
        DevolucaoView.as_view(),
        name='devolucao',
        ),
    url(r'^id=(?P<id>[0-9]+)/$',
        DevolucaoView.as_view(),
        name='devolucao_sucesso',
        ),
    url(r'^tabela/$',
        TabelaView.as_view(),
        name='tabela',
        ),
]