from django.urls import path
from . import views
from . views import MenuList, MenuItemDetails

urlpatterns = [
    path('', views.MenuList.as_view(), name='MenuList'),
    path('', views.MenuItemDetails.as_view(), name='MenuItemDetails'),
]