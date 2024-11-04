from django.shortcuts import render
from django.views import generic
from . models import Item


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "Index.html"

    def get_context_data(self):
        context = {'meals': 'Pizza'}
        return context


class MenuItemDetails(generic.DetailView):
    model = Item
    template_name = "item_details.html"

