from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('items', views.get_items_list, name='item-list'),
    path('item/<int:id>', views.get_items, name='item-page'),
]
