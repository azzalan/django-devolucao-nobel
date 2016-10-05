from django import forms
from devolucao.models import Livro


class ISBNForm(forms.Form):
    isbn = forms.CharField(
        max_length=15, 
        widget=forms.TextInput(attrs={'autofocus': 'autofocus'}),
        label='ISBN',
        )

    def clean(self):
        try:
            isbn = self.cleaned_data['isbn']
        except:
            isbn = "Vazio"
        livro = Livro.objects.all().filter(isbn=isbn)
        if isbn=="Vazio":
            raise forms.ValidationError("Preencha o isbn antes de enviar.")
        elif not livro:
            raise forms.ValidationError("Não devolver, esse isbn não está na lista.")
        elif livro[0].quantidade_atual<1:
            raise forms.ValidationError("Não devolver, quantidade de livros devolvidos já atingida.")
        return self.cleaned_data