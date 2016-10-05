from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from openpyxl import load_workbook
from django.core.urlresolvers import reverse
from devolucao.models import Livro
from devolucao.forms import ISBNForm


class DevolucaoView(FormView):
    # template_name = "base.html"
    form_class = ISBNForm

    def get_template_names(self):
        return ["form.html"]

    def form_valid(self, form):
        self.livro = Livro.objects.all().filter(isbn=form.cleaned_data['isbn'])
        for livro in self.livro:
            livro.quantidade_atual -= 1
            livro.save()
        return super(DevolucaoView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'devolucao_sucesso', 
            kwargs={
            'id':self.livro[0].id,
            })

    def get_context_data(self, **kwargs):
        context = super(DevolucaoView, self).get_context_data(**kwargs)
        try:
            if self.kwargs['id']:
                context['livro'] = Livro.objects.all().filter(id=self.kwargs['id'])
        except:
            pass
        return context

class TabelaView(TemplateView):
    def get_template_names(self):
        return ["tabela.html"]

    def get_context_data(self, **kwargs):
        context = super(TabelaView, self).get_context_data(**kwargs)
        context['livros'] = Livro.objects.all().exclude(
            quantidade_faltando=0,
            )
        return context
