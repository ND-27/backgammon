from django.urls import path

from .views import withdraw_page, deposit_page

urlpatterns = [
    path('withdraw-token', withdraw_page, name='withdraw_page'),

    path('deposit-token', deposit_page, name='deposit_page'),
]
