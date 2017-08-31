import django.forms as forms
import simulation.models.accounting_models as acc


class FormsetForm(forms.Form):
    title = forms.CharField()
    pages = forms.IntegerField()


class TradesSheetForm(forms.ModelForm):
    class Meta:
        model = acc.Trade
        fields = ['trader', 'item', 'month', 'quantity']
        widgets = {
            'month':forms.Select()
        }

TradesSheetFormset = forms.formset_factory(TradesSheetForm, extra=2)
FormsetFormFormset = forms.formset_factory(FormsetForm)