from django.urls import path

from token_api.views import get_balance

urlpatterns = [
    path('get_balance/', get_balance, name='get_balance'),
    # path('get_balance_batch/', get_balance_batch, name='get_balance_batch'),
    # path('get_top/<int:n>/', get_top_addresses, name='get_top_addresses'),
    # path('get_top_with_transactions/<int:n>/', get_top_addresses_with_transactions,
    #      name='get_top_addresses_with_transactions'),
    # path('get_token_info/<str:token_address>/', get_token_info, name='get_token_info'),
]
