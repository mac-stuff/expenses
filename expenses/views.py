from django.views.generic.list import ListView

from django.db.models import Count
from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category, total_amount, total_summary_per_year_month

class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

            from_date = form.cleaned_data.get('from_date')
            if from_date:
                queryset = queryset.filter(date__gte=from_date)

            to_date = form.cleaned_data.get('to_date')
            if to_date:
                queryset = queryset.filter(date__lte=to_date)

            categories = form.cleaned_data.get('categories')
            if categories:
                queryset = queryset.filter(category__in=categories)
            
        dir = self.request.GET.get("dir")
        if dir == "asc":
            queryset = queryset.order_by('date')
        if dir == "desc":
            queryset = queryset.order_by('-date')

        return super().get_context_data(
            object_list=queryset,
            form=form,
            summary_per_category=summary_per_category(queryset),
            total_amount=total_amount(queryset),
            total_summary_per_year_month=total_summary_per_year_month(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        return super().get_context_data(
            object_list=queryset
            .annotate(number_of_expenses=Count('expense')),
            **kwargs)

