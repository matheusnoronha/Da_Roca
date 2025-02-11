from django.urls import path

from .views import SellerOrderView
from .views import CartProductView, OrderView, RatingView


urlpatterns = [
    path('cart/', CartProductView.list, name='cart'),
    path('cart/create', CartProductView.create, name='create_cart'),
    path('cart/update', CartProductView.update, name='update_cart'),
    path('cart/delete', CartProductView.delete, name='remove_cart'),
    path('confirm/', OrderView.list, name='confirm_order'),
    path('seller/', SellerOrderView.list, name='seller_orders'),
    path('seller/datails', SellerOrderView.index, name='seller_order_detail'),
    path('cancel/<int:order_id>', SellerOrderView.cancel, name='cancel_order'),
    path('update/status/<int:order_id>', SellerOrderView.update, name='update_status_order'),
    path('order/list', OrderView.list_order, name='list_user_orders'),
    path('order/<int:order_id>', OrderView.view_order, name='view_order'),
    path('order/rate', RatingView.create, name='create_rating'),
]
