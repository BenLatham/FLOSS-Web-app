from django import forms
from simulation.models import Enterprise

class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['name']

class FormsetForm(forms.Form):
    title = forms.CharField()
    pages = forms.IntegerField()

FormsetFormFormset = forms.formset_factory(FormsetForm)