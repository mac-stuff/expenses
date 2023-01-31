from django import forms
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):

    from_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ('name', 'from_date', 'to_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['from_date'].required = False
        self.fields['from_date'].label = "from"
        self.fields['to_date'].required = False
        self.fields['to_date'].label = "to"

