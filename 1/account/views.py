from django.shortcuts import render

# Create your views here.


def index(request):
    return 'account'


def add_bill(request):
    return render(request, 'account/add_bill.html')