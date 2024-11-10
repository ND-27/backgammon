from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Withdraw, Deposit


def withdraw_page(request):
    player = request.user

    context = {
        'status': "Your deposits in progress",
    }
    return render(request, 'withdraw_page.html', context)


def deposit_page(request):
    player = request.user

    context = {
        'status': "Your deposits in progress",
    }
    return render(request, 'deposit_page.html', context)
