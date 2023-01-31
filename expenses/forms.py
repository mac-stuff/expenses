from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):

    from_date = forms.DateField(
       widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    categories = forms.ModelMultipleChoiceField( widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())

    class Meta:
        model = Expense
        fields = ('name', 'from_date', 'to_date', 'categories')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['from_date'].required = False
        self.fields['from_date'].label = "from"
        self.fields['to_date'].required = False
        self.fields['to_date'].label = "to"
        self.fields['categories'].required = False
        self.fields['categories'].label = "categories"

