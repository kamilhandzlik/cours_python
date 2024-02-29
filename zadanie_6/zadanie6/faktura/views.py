from django.shortcuts import render
from django.db.models import Sum
from .models import Invoice


def invoice_list(request):
    invoices = Invoice.objects.all()
    sum_of_quotas = Invoice.objects.aggregate(Sum("quota"))["sum_of_quotas"]
    return render(request, {"invoices": invoices, "sum of quotas": sum_of_quotas})
