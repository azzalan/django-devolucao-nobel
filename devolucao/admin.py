from django.contrib import admin
from devolucao.models import *

class LivroAdmin(admin.ModelAdmin):
	list_display = []
	for field in Livro._meta.fields :
		list_display.append(field.name)
	list_editable = ('quantidade_total_a_devolver','quantidade_faltando')
	search_fields = ['isbn', 'titulo']
	save_on_top = True

admin.site.register(Livro, LivroAdmin)