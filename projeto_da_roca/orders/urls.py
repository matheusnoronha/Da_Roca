from django.urls import path

from .views import CartProductView, OrderView, RatingView


urlpatterns = [
    path('cart/', CartProductView.list, name='cart'),
    path('cart/create', CartProductView.create, name='create_cart'),
    path('cart/update', CartProductView.update, name='update_cart'),
    path('cart/delete', CartProductView.delete, name='remove_cart'),
    path('confirm/', OrderView.list, name='confirm_order'),
    path('order/list', OrderView.list_order, name='list_user_orders'),
    path('order/<int:order_id>', OrderView.view_order, name='view_order'),
    path('order/rate', RatingView.create, name='create_rating'),
]
