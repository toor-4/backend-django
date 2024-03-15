from django.urls import path
from shop.views import OrderView

urlpatterns = [
    
    path('order/', OrderView.as_view(), name='order'),
]