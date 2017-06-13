from django import forms

class FormsetForm(forms.Form):
    title = forms.CharField()
    pages = forms.IntegerField()

FormsetFormFormset = forms.formset_factory(FormsetForm)